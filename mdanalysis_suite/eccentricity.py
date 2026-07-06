import MDAnalysis as mda
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize

from mdanalysis_suite.common import compute_eccentricity

DEFAULT_WINDOW = 5

def compute(u, select="protein"):
    return compute_eccentricity(u, select=select)

def plot_eccentricity(eccentricity, *, name, out_filename, window=DEFAULT_WINDOW):
    data = np.asarray(eccentricity)

    smoothdata = sliding_window_view(data, window).mean(axis=1)

    time_ns = np.arange(len(data)) / 10.0
    time_smooth = time_ns[:len(smoothdata)]

    points = np.array([time_smooth, smoothdata]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = Normalize(vmin=0.0, vmax=1.0)
    lc = LineCollection(segments, cmap="magma", norm=norm)  # type: ignore
    lc.set_array(smoothdata)
    lc.set_linewidth(1)


    fig, ax = plt.subplots(figsize=(6, 4))
    ax.add_collection(lc)

    ax.set_ylim(0, 1)
    ax.set_xlim(0, 2000)
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Eccentricity")
    ax.set_title(name)

    cbar = fig.colorbar(lc, ax=ax)
    cbar.set_label("Eccentricity")

    plt.savefig(out_filename, dpi=300, bbox_inches="tight")
    plt.close()

def run(*, top, traj, out, title, window=DEFAULT_WINDOW):
    name = f"Eccentricity - {title}"
    out_filename = f"{out}_ecc.png"

    u = mda.Universe(top, traj)
    eccentricity = compute(u)
    plot_eccentricity(eccentricity, name=name, out_filename=out_filename, window=window)