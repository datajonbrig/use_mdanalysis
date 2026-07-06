import matplotlib.pyplot as plt
import seaborn as sns

def heatmap(
    data,
    *,
    xticklabels,
    yticklabels,
    xlabel,
    ylabel,
    title,
    out_filename,
    cbar_label="Contact Frequency",
    vmin=0,
    vmax=1,
    cmap="magma",
    figsize=(8, 8),
    dpi=300,
    bbox_inches="tight",
):
    plt.figure(figsize=figsize)
    sns.heatmap(
        data,
        xticklabels=xticklabels,
        yticklabels=yticklabels,
        cmap=cmap,
        cbar_kws={"label": cbar_label},
        vmin=vmin,
        vmax=vmax,
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.tight_layout()
    plt.savefig(out_filename, dpi=dpi, bbox_inches=bbox_inches)
    plt.close()