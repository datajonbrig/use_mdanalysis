"""
helpers used across many files
"""

import numpy as np
from MDAnalysis.analysis.align import AlignTraj

"""
Subunit stuff
"""
def split_residue_index(prot_resids, subunit_length):
    prot_resids = np.asarray(prot_resids)
    subunit = (prot_resids - 1) // subunit_length + 1
    local_resi = ((prot_resids - 1) % subunit_length) + 1
    return subunit, local_resi

def collapse_across_subunits(contact_freq, local_resi):
    n_local = local_resi.max()
    n_contacts = contact_freq.shape[1]

    collapsed = np.zeros((n_local, n_contacts))

    for r in range(1, n_local +1):
        mask = local_resi == r
        collapsed[r - 1] = np.max(contact_freq[mask], axis=0)
    
    return collapsed

def interacting_subunits(contact_freq, local_resi, subunit, threshold=0.80):
    interactions = {}

    for r in np.unique(local_resi):
        mask = local_resi == r
        interacting = np.any(contact_freq[mask] > threshold, axis=1)
        interactions[r] = sorted(subunit[mask][interacting])

    return interactions

def compact_subunits(subunits):
    if not subunits:
        return ""
    
    ranges = []
    start = prev = subunits[0]

    for s in subunits[1:]:
        if s == prev + 1:
            prev = s
        else:
            ranges.append((start, prev))
            start = prev = s
    ranges.append((start, prev)) #probably not wrong, but i dont understand

    formatted = []
    for a, b in ranges:
        if a == b:
            formatted.append(f"S{a}")
        else:
            formatted.append(f"S{a}\u2013{b}") #i swapped to unicode variable here
    
    return ", ".join(formatted)

def build_residue_labels(prot_resi, local_resi, interacting_map):
    labels = []

    for r in range(1, int(local_resi.max()) + 1):
        idx = np.where(local_resi == r)[0][0]
        res = prot_resi[idx]

        base = f"{res.resname}{r}"
        subs = interacting_map[r]

        if subs:
            base += f" ({compact_subunits(subs)})"

        labels.append(base)
    
    return labels

"""
POPX stuff
"""
def build_moiety_map(popx_atoms):
    atom_to_moiety = []
    moiety_names = ["Headgroup", "Palmitoyl", "Oleoyl"]

    palmitoyl = {
        "C3", "C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39",
        "C310", "C311", "C312", "C313", "C314", "C315", "C316",
    }
    oleoyl = {
        "C2", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29",
        "C210", "C211", "C212", "C213", "C214", "C215", "C216", "C217", "C218",
    }

    for atom in popx_atoms:
        if atom.name in palmitoyl:
            atom_to_moiety.append("Palmitoyl")
        elif atom.name in oleoyl:
            atom_to_moiety.append("Oleoyl")
        else:
            atom_to_moiety.append("Headgroup")

    return atom_to_moiety, moiety_names

"""
Eccentricity (since this is shared by single-rep and analysis, i've moded it here)
"""
def compute_eccentricity(u, select="protein"):
    ag = u.select_atoms(select)

    AlignTraj(u, u, select=select).run()

    eccentricity = []
    for ts in u.trajectory:
        p = ag.moment_of_inertia()
        e1, e2, e3 = np.linalg.eigvalsh(p)
        etop = e1 + e2 - e3
        ebot = -e1 + e2 + e3
        e = np.sqrt((1 - (etop / ebot)))
        eccentricity.append(e)

    return np.array(eccentricity)