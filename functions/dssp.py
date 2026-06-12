#Written by Audrey D. Prendergast
#UNTESTED
#needed: process only protein not all atoms, global dssp, plotting for resi and global

import mdtraj as mdt
import numpy as np
import matplotlib.pyplot as plt

def calculate_dssp_resi():
    trajectory = mdt.load(traj, top=top)
    dssp = mdt.compute_dssp(trajectory, simplified=True)

    structures = ['H', 'E', 'C']

    n_residues = trajectory.n_residues
    residx = np.arange(n_residues)

    percent_array = np.zeros((len(structures, n_residues)))

    for i, type in enumerate(structures):
        percent_array[i] = (dssp == type).sum(axis=0) / trajectory.n_frames * 100