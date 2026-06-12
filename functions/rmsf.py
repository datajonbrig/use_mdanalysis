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