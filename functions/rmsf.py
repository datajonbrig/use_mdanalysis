#Written by Audrey D. Prendergast
#UNTESTED
#NEEDS: modifications to plot residues nicely with multiple chains per rep and averaged
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis import align, rms
import rmsd

def calculate_rmsf():
    avg = align.AverageStructure(u, u, select='protein and name CA', ref_frame=0)
    ref = avg.results.universe
    
    #align trajectory to reference (average) conformation
    align.AlignTraj(u, ref, select='protein and name CA')
    
    CA = u.select_atoms('protein and name CA')

    rmsf = rms.RMSF(CA)
    return rmsf

def plot_rmsf():
    rmsf = rmsf.rmsd.T
    time = rmsf[1]/1000
    name = f"RMSF - {title}"
    plt.figure()
    plt.plot(time, rmsf, color, linestyle='-')
    plt.title(name)
    plt.xlabel("Residue Index", fontsize=12)
    plt.ylabel("RMSF (Å)", fontsize=12)
    plt.savefig(out)
    plt.close()