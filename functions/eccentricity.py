#Written by Audrey D. Prendergast 
#Fully functional as of 4/6/2026

import MDAnalysis as mda
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from MDAnalysis.analysis import align
from MDAnalysis.analysis.align import AlignTraj
import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize

# Change only these items
replicates=[1,2,3]
in_top = "rep1/production.tpr" # topology file (path) that matches trajectory (.tpr, .pdb, .gro)
traj_template = "rep{}/traj/cat_pbc.xtc"
title = "Hexamer Eccentricity (w/ Free Lipids)" # Title to go on figure
out_filename = "hexavg_ecc.png" # Name for figure .png file
window = 100 #window size for smoothed data, 50 is usually good

#CHANGE NOTHING BELOW THIS LINE
#------------------------------
def calculate_eccentricity_all_reps():
    for i in replicates:
        print(f"Processing replicate {i}")
        
        #load in trajectories
        traj_file = traj_template.format(i)
        u = mda.Universe(in_top, traj_file)
        ag = u.select_atoms("protein")

        # Align whole trajectory
        aligner = AlignTraj(u, u, select="protein")
        aligner.run()

        ecc = []

        for ts in u.trajectory:  
            p=ag.moment_of_inertia()
            e1,e2,e3 = np.linalg.eigvalsh(p)
            etop=e1+e2-e3
            ebot=-e1+e2+e3
            e = np.sqrt((1 - (etop / ebot)))
            ecc.append(e)
        ecc=np.array(ecc)
        np.save(f"eccentricity_rep{i}.npy",ecc)
        print(f"  Saved eccentricity_rep{i}.npy")

def plot_eccentricity_rep():
    for i in replicates:
        data = np.load(f"eccentricity_rep{i}.npy")

        smoothdata = sliding_window_view(data,window).mean(axis=1)

        # Time axis correction to correspond to smoothed data
        time_ns = np.arange(len(data)) / 10.0
        time_smooth = time_ns[:len(smoothdata)]

        #color the line by eccentricity value
        points = np.array([time_smooth, smoothdata]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        norm = Normalize(vmin=0.0, vmax=1.0)
        lc = LineCollection(segments, cmap="magma", norm=norm)
        lc.set_array(smoothdata)
        lc.set_linewidth(1)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.add_collection(lc)

        ax.set_ylim(0, 1)
        ax.set_xlim(0,2000)
        ax.set_xlabel("Time (ns)")
        ax.set_ylabel("Eccentricity")
        ax.set_title(name)

        cbar = fig.colorbar(lc, ax=ax)
        cbar.set_label("Eccentricity")
        outname = f'ecc_rep{i}.png'
        plt.savefig(outname, dpi=300, bbox_inches="tight")
        plt.close()


def plot_eccentricity_avg():
    
    ecc_stack = []

    for i in replicates:
        data = np.load(f"eccentricity_rep{i}.npy")
        smooth = sliding_window_view(data, window).mean(axis=1)
        ecc_stack.append(smooth)

    ecc_stack = np.array(ecc_stack)

    mean_ecc = ecc_stack.mean(axis=0)
    std_ecc = ecc_stack.std(axis=0)

    # Time axis correction to correspond to smoothed data
    time_ns = np.arange(len(mean_ecc)) / 10.0

    #color the line by eccentricity value
    points = np.array([time_ns, mean_ecc]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = Normalize(vmin=0.0, vmax=1.0)
    lc = LineCollection(segments, cmap="magma", norm=norm)
    lc.set_array(mean_ecc)
    lc.set_linewidth(1)

    fig, ax = plt.subplots(figsize=(6, 4))
    plt.fill_between(
        time_ns,
        mean_ecc+std_ecc,
        mean_ecc-std_ecc,
        color='navajowhite',
        alpha=0.25,
        label='± 1 SD')
    ax.add_collection(lc)

    ax.set_ylim(0, 1)
    ax.set_xlim(0,2000)
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Eccentricity")
    ax.set_title(title)

    cbar = fig.colorbar(lc, ax=ax)
    cbar.set_label("Eccentricity")

    plt.savefig(out_filename, dpi=300, bbox_inches="tight")
    plt.close()

def plot_eccentricity_heatmap():

    ecc_stack = []

    for i in replicates:
        data = np.load(f"eccentricity_rep{i}.npy")
        smooth = sliding_window_view(data, window).mean(axis=1)
        ecc_stack.append(smooth)

    ecc_stack = np.array(ecc_stack)
    mean_ecc = ecc_stack.mean(axis=0)[np.newaxis, :]  # shape: (1, time)

    dt = 0.1  # ns per frame
    tmax = mean_ecc.shape[1] * dt

    plt.figure(figsize=(7,2))

    im = plt.imshow(
        mean_ecc,
        aspect="auto",
        origin="lower",
        cmap="magma",
        vmin=0.0,
        vmax=1.0,
        extent=[0, tmax, 0, 1]
    )

    plt.colorbar(im, label="Eccentricity")
    plt.xlabel("Time (ns)")
    plt.yticks([])
    plt.title(title + " (Mean over replicates)")

    plt.xlim(0, 2000)
    outname = f'ecc_heatmap.png'
    plt.savefig(outname, dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
 calculate_eccentricity_all_reps()
 plot_eccentricity_rep()
 plot_eccentricity_avg()
 plot_eccentricity_heatmap()