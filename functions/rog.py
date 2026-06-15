#Written by Audrey D. Prendergast
#UNTESTED
import pandas as pd
import MDAnalysis as mda
import matplotlib.pyplot as plt

def calculate_rog():
    bb = u.select_atoms('protein and name CA')
    times = []
    rog = []
    for ts in u.trajectory:
        times.append((ts.time)/1000)
        rog.append(bb.radius_of_gyration())
    rog_data = pd.DataFrame({'Time (ns)': times, 
                             'Radius of Gyration (Å)':rog})
    return rog_data

def plot_rog(rog_data):
    name = f"Radius of Gyration - {title}"
    rog_data.plot(x='Time (ns)', y='Radius of Gyration (Å)', kind='line', color=color)
    plt.xlabel('Time (ns)')
    plt.ylabel('Radius of Gyration (Å)')
    plt.title(name)
    plt.savefig()
    plt.close()