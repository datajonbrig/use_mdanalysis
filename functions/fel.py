#Written by Audrey D. Prendergast
#UNTESTED
#This MUST go AFTER rmsd and rog calculations - it will use that data to perform calcs. 
#Also requires variable T to be defined in the arguments
import glob
import numpy as np
import pandas as pd
import scipy.ndimage
import MDAnalysis as mda
import matplotlib.pyplot as plt
from MDAnalysis.analysis import rms
from matplotlib.colors import LogNorm

def gen_fel():
    prot = u.select_atoms('protein')
    rog_path = glob.glob('./rog_*.csv')[0]
    rmsd_path = glob.glob('./rmsd_*.csv')[0]
    rog = pd.read_csv(rog_path)
    rmsd = pd.read_csv(rmsd_path)
    R = 0.0083144626 #kcal/mol R constant
    kT = R * T
    
    counts, xedges, yedges = np.histogram2d(rmsd, rog, bins=60)
    counts = np.where(counts == 0, np.nan, counts) #mask empty bins to prevent div by 0 errors
    
    prob = counts/np.nansum(counts)

    FE = -kT * np.log(prob)

    FE -= np.nanmin(FE) #put minimum at kcal/mol 0

    #smooth pixelation in the grid 
    e_cap = np.nanmax(FE)+2.0
    filled_e = np.where(np.isnan(FE), e_cap, FE)
    smooth_e = scipy.ndimage.gaussian_filter(filled_e, sigma = 1.0)

    outname = f'fel_{out}.csv'
    np.savetxt(outname, smooth_e, delimiter=',')

    xcenter = (xedges[:-1] + xedges[1:])/2
    ycenter = (yedges[:-1] + yedges[1:])/2
    x,y = np.meshgrid(xcenter, ycenter)

    ### Identifying minima and saving representative pdb files
    min_idx = np.unravel_index(np.nanargmin(FE), FE.shape)
    minx = xcenter[min_idx[0]]
    miny = ycenter[min_idx[1]]
    print(f'Deepest minimum coordinates found at:')
    print(f' --> RMSD: {minx:.2f} Å')
    print(f' --> RoG: {miny:.2f} Å')

    #tolerance window for ranges to pull structures from
    rmsd_tol = 0.2
    rog_tol = 0.2

    frames = np.where((np.abs(rmsd - minx) <= rmsd_tol) & (np.abs(rog-miny) <= rog_tol))[0]

    print(f'Found {len(frames)} frames matching the tolerance window')

    nstructures = 3
    indices = np.linspace(0, len(frames) - 1, nstructures)
    target_frames = frames[indices]

    u.trajectory[0]

    for idx, nth_frame in enumerate(target_frames):
        u.trajectory[nth_frame]

        pdbname = f'fel_minima_frame{nth_frame}.pdb'

        with mda.Writer(pdbname, prot.n_atoms) as W:
            W.write(prot)
        
        print(f'Saved frame {nth_frame} as {pdbname}')

    return smooth_e, x, y 

def plot_fel(smooth_e, x, y):
    fig, ax = plt.subplots(6,4)
    contour = ax.contour(x,y, smooth_e.T, levels=25, cmap="seismic")

    cbar = fig.colorbar(contour, ax=ax)
    cbar.set_label("Free Energy (kcal/mol)", fontsize=12)
    ax.set_xlabel("RMSD (Å)", fontsize=12)
    ax.set_ylabel("RoG (Å)", fontsize=12)
    ax.set_title("Free Energy Landscape (RMSD v RoG)", fontsize=14, fontweight="bold")
    name = f'fel_{out}.png'
    plt.savefig(name)
    plt.close()