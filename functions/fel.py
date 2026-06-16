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

    #PLOT
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