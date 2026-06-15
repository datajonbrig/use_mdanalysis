#Written by Audrey D. Prendergast
#UNTESTED
import numpy as np
import pandas as pd
import MDAnalysis as mda
import matplotlib.pyplot as plt

def prot_popx_mindist():
    prot = u.select_atoms("protein")
    popx = u.select_atoms("resname POPX")

    dist = []
    time = []

    for ts in u.trajectory:
        dist_array = mda.analysis.distances.distance_array(prot.positions, popx.positions, box=u.dimensions)
        dist.append(np.min(dist_array))
        time.append((ts.time)/1000)
    
    mindist = pd.DataFrame({'Time':time,'Distance (Å)':dist})
    outname = f'prot_popx_mindist_{out}.csv'
    mindist.to_csv(outname, index=False)

    return dist, time

def plot_maxdist(time, dist):
    name = f'Minimum Protein-POPX Distance {title}'
    outname = f'prot_popx_mindist_{out}.png'
    plt.plot(time, dist, color=color)
    plt.xlabel('Time (ns)')
    plt.ylabel('Distance (Å)')
    plt.title(name)
    plt.savefig(outname)
    plt.close()