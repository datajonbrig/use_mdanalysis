#Written by Audrey D. Prendergast
#UNTESTED
import mdtraj as mdt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_dssp_resi():
    trajectory = mdt.load(traj, top=top)
    protein = trajectory.atom_slice(trajectory.topology.select("protein"))
    dssp = mdt.compute_dssp(protein, simplified=True)

    prot_resi = [res for res in trajectory.topology.residues if res.is_protein]

    structures = ['H','E','C']
    data = {}

    for type in structures:
        data[type] = np.mean(dssp == type, axis=0)
    
    data['resSeq'] = [res.resSeq for res in prot_resi]
    data['resName'] = [res.name for res in prot_resi]

    dsspdf = pd.DataFrame(data)
    avg_dssp = dsspdf.groupby(['resSeq','resName']).mean().reset_index()

    name = f'residue_dssp_{out}.csv'
    avg_dssp.to_csv(name, index=False)
    
    return protein, dssp

def calculate_dssp_global(protein, dssp):
    nres = protein.n_residues
    helix = np.sum(dssp == 'H', axis=1) / nres * 100
    sheet = np.sum(dssp == 'E', axis=1) / nres * 100
    coil = np.sum(dssp == 'C', axis=1) / nres * 100
    ns = protein.time / 1000

    gdssp = pd.DataFrame({'Time (ns)':ns,'Helix':helix,'Sheet':sheet,'Coil':coil})
    name = f'global_dssp_{out}.csv'
    gdssp.to_csv(name, index=False)

    return helix, sheet, coil, ns

def plot_dssp(ns, helix, sheet, coil):
    plt.plot(ns, helix, label='Helix', color='r')
    plt.plot(ns, sheet, label='Beta Sheet', color='b')
    plt.plot(ns, coil, label='Coil',color='g')
    name = f'Global DSSP {title}'
    plt.title(name)
    plt.legend(loc = "best")
    plt.xlabel('Time (ns)')
    plt.ylabel('Secondary Structure Percentage (%)')
    outname = f'global_dssp_{out}.png'
    plt.savefig(outname)
    plt.close()