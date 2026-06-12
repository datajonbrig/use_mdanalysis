#Written by Audrey D. Prendergast
#UNTESTED
import mdtraj as mdt
import matplotlib.pyplot as plt

def sasa():
    trajectory = mdt.load(traj)
    chains = (u.select_atoms('protein').residues)/length
    atom_sasa = (mdt.shrake_rupley(trajectory))/chains
    sasa = atom_sasa.sum(axis=1)
    return trajectory,sasa

def plot_sasa(trajectory, sasa):
    time = (trajectory.time)/1000
    name = f"Solvent Accessible Surface Area - {title}"
    plt.figure()
    plt.plot(time, sasa, color, linestyle='-')
    plt.title(name)
    plt.xlabel("Time (ns)", fontsize=12)
    plt.ylabel("SASA (nm^2)", fontsize=12)
    plt.savefig()
    plt.close()