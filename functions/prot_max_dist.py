#Written by Audrey D. Prendergast
#UNTESTED
import numpy as np
import pandas as pd
import MDAnalysis as mda
import matplotlib.pyplot as plt

def prot_maxdist():
    prot = u.select_atoms("protein")

    dist = []
    time = []

    for ts in u.trajectory:
        dist_array = mda.analysis.distances.distance_array(prot.positions, prot.positions, box=u.dimensions)
        dist.append(np.max(dist_array))
        time.append((ts.time)/1000)
    
    maxdist = pd.DataFrame({'Time':time,'Distance (Å)':dist})
    outname = f'max_prot_dist_{out}.csv'
    maxdist.to_csv(outname, index=False)

    return dist, time

def plot_maxdist(time, dist):
    name = f'Maximum Protein-Protein Distance {title}'
    outname = f'max_prot_dist_{out}.png'
    plt.plot(time, dist, color=color)
    plt.xlabel('Time (ns)')
    plt.ylabel('Distance (Å)')
    plt.title(name)
    plt.savefig(outname)
    plt.close()