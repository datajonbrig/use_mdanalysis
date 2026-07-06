import MDAnalysis as mda
import numpy as np
from MDAnalysis.lib.distances import distance_array

from mdanalysis_suite.common import build_moiety_map
from mdanalysis_suite.plotting import heatmap

def prep(top, traj):
    u = mda.Universe(top, traj)
    popx_atoms = u.select_atoms("resname POPX and not name H*")
    return u, popx_atoms

"""
Contact Calcs
"""
def build_atom_to_lipid_map(popx_atoms):
    resid_indices = popx_atoms.resindices
    _, atom_to_lipid = np.unique(resid_indices, return_inverse=True)
    return atom_to_lipid

def calculate_popx_popx_contacts(u, popx_atoms, atom_to_lipid, cutoff):
    contact_matrix = np.zeros((len(popx_atoms), len(popx_atoms)))
    nframes = 0

    for ts in u.trajectory:
        nframes += 1

        dists = distance_array(popx_atoms.positions, popx_atoms.positions)

        same_lipid = atom_to_lipid[:, None] == atom_to_lipid[None, :]
        atom_contacts = (dists < cutoff) & ~same_lipid

        contact_matrix += atom_contacts.astype(int)

    contact_freq = contact_matrix / nframes
    return contact_freq

"""
Moiety Stuff
"""
def collapse_contacts_moiety_to_moiety(contact_freq_atom, atom_to_moiety, moiety_names):
    n_moiety = len(moiety_names)
    collapsed = np.zeros((n_moiety, n_moiety))

    for i, mi in enumerate(moiety_names):
        idx_i = [k for k, m in enumerate(atom_to_moiety) if m == mi]
        for j, mj in enumerate(moiety_names):
            idx_j = [k for k, m in enumerate(atom_to_moiety) if m ==mj]

            if idx_i and idx_j:
                collapsed[i, j] = np.max(contact_freq_atom[np.ix_(idx_i, idx_j)])
    
    return collapsed

def write_moiety_table(popx_atoms, atom_to_moiety, outfile="moiety_assignments.dat"):
    with open(outfile, "w") as f:
        f.write("# resid resname atomname moiety\n")
        for atom, moiety in zip(popx_atoms, atom_to_moiety):
            f.write(
                f"{atom.resid:5d} {atom.resname:6s} "
                f"{atom.name:8s} {moiety}\n" 
            )

"""
Plotting
"""
def plot_moiety_contacts(moiety_names, collapsed_contacts, *, name, out_filename):
    heatmap(
        collapsed_contacts,
        xticklabels=moiety_names,
        yticklabels=moiety_names,
        xlabel="POPC Moiety",
        ylabel="POPC Moiety",
        title=name,
        out_filename=out_filename,
        cbar_label="Contact Frequency",
        vmin=0,
        vmax=0.25, # type: ignore
    )

def run(*, top, traj, out, title, cutoff=4.0, write_table=False):
    name = f"Free Lipid Interactions - {title}"
    out_filename = f"{out}-popx-int.png"

    u, popx_atoms = prep(top, traj)

    atom_to_lipid = build_atom_to_lipid_map(popx_atoms)
    contact_freq = calculate_popx_popx_contacts(u, popx_atoms, atom_to_lipid, cutoff)

    atom_to_moiety, moiety_names = build_moiety_map(popx_atoms)

    if write_table:
        write_moiety_table(popx_atoms, atom_to_moiety)

    collapsed = collapse_contacts_moiety_to_moiety(
        contact_freq, atom_to_moiety, moiety_names
    )

    plot_moiety_contacts(moiety_names, collapsed, name=name, out_filename=out_filename)
    return collapsed