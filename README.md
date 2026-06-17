# use_mdanalysis
Available analysis: dssp, eccentricity, free energy landscape, rmsd, rmsf, rog, sasa, ligand-protein interactions, max protein-protein distance (aggregation indicator), protein-popx min distance, protein-popx interactions, popx-popx interactions, protein-protein interactions by chain and residue, protein-membrane lipid interactions (moieties), min distance of protein to membrane midplane (perturbation indicator)

USAGE:

-f, --traj = Trajectory file (path), preferrably concatenated, pbc corrected, and without waters.

-s, --top = Topology file (path), should match the atoms in traj (no waters)

-o,--out = System name to append to outfile names (e.g. Hex1_lipids)

-t,--title = System name for title of plots, contained within quotes (i.e. 'Hexamer (Rep 1, W/ Free Lipids)')

-l,--length = Chain length of protein. All subunits must be identical

-c,--cutoff = Cutoff distance (A) for interactions (optional, default = 4.0)

--color = color to use for line plots
(default = maroon)

p.add_argument("--ligand", help="name of ligand as shown in MD structure files")
p.add_argument("-k","--temp", help='Temperature of the system, in Kelvin', default = 310, type=float)
p.add_argument("-a","--analysis",help="Which sets of analysis to run? All, membrane, protein, free lipids.")
p.add_argument("-m","-memb", help="indicates a membrane is present in the system", action='store true')



### Issues

If there is additional analysis you would like added, submit an issue labeled "enhancement"

If there is an issue you encounter in any scripts, submit an issue labeled "bug"

If you uncover a problem with script logic/calculations/etc, submit an issue labeled "invalid"