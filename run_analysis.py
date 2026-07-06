import argparse

import MDAnalysis as mda

from mdanalysis_suite import (
    eccentricity,
    popx_popx
)

def system_contains_popx(top, traj):
    u = mda.Universe(top, traj)
    return len(u.select_atoms("resname POPX")) > 0

def parse_args():
    p = argparse.ArgumentParser(description="MD Analysis Driver")

    # trajectory, structure, and system
    p.add_argument("-f", "--traj", required=True,
                   help="Trajectory file (path), preferrably concatenated, pbc corrected, and without waters.")
    p.add_argument("-s", "--top", required=True,
                   help="Topology file (path), should match the atoms in traj (no waters)")
    p.add_argument("-o", "--out", required=True,
                   help="System name to append to outfile names (e.g. Hex1_lipids)")
    p.add_argument("-t", "--title", required=True,
                   help="System name for title of plots, contained within quotes "
                        "(i.e. 'Hexamer (Rep 1, W/ Free Lipids)')")

    # other required variables
    p.add_argument("-l", "--length", required=True, type=int,
                   help="Chain length of protein. All subunits must be identical")
    p.add_argument("-c", "--cutoff", required=False, default=4.0, type=float,
                   help="Cutoff distance (A) for interactions")

    return p.parse_args()

def main():
    args = parse_args()

    base = dict(top=args.top, traj=args.traj, out=args.out, title=args.title)

    has_popx = system_contains_popx(args.top, args.traj)
    if not has_popx:
        print("[!] POPX not detected - skipping POPX analyses.")

    #eccentricity
    eccentricity.run(**base)

    #popx-popx
    if has_popx:
        popx_popx.run(**base, cutoff=args.cutoff)


if __name__ == "__main__":
    main()