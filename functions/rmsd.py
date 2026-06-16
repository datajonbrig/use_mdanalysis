#Written by Audrey D. Prendergast
#UNTESTED
#NEEDS: modifications to plot nicely with multiple chains both independent and averaged
from MDAnalysis.analysis import rms
import matplotlib.pyplot as plt
import numpy as np

def run_rmsd():
    rmsd = rms.RMSD(u, start, select='backbone', groupselections=['protein'])
    name = f'rmsd_{out}.csv'
    np.savetxt(name, rmsd, delimiter=',')
    return rmsd

def plot_rmsd():
    rmsd = rmsd.rmsd.T
    time = rmsd[1]/1000
    name = f"RMSD - {title}"
    plt.figure()
    plt.plot(time, rmsd, color, linestyle='-')
    plt.title(name)
    plt.xlabel("Time (ns)", fontsize=12)
    plt.ylabel("RMSD (Å)", fontsize=12)
    plt.savefig()
    plt.close()