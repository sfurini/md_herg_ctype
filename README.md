# Molecular Dynamics simulations of wild-type hERG, hERG-N629D, hERG-N627Y

## Equilibrium MD simulations

The folder contain input and restart files for the MD simulations described in: https://pubmed.ncbi.nlm.nih.gov/36512342/.

* md.conf: Template configuration file for MD simulation with NAMD.

* [wt, n629d, f627y].prmtop: Topology files for the 3 model systems.

* [wt, n629d, f627y].inpcrd: Initial atom coordinates  for the 3 model systems.

* [wt, n629d, f627y].restart.[coor, xsc, vel]: Restart file for the 3 model systems. These files provide the state of the 3 systems after equilibration.

* [wt, n629d, f627y].replica[1-8].pdb: Atomic coordinates of the 3 model systems after 1 microsecond of MD simulation. Coordinates of 8 independent simulations, replica[1-8], are included for each model system.

## MD simulations with electric field

The folder contain simulations of the hERG for:
* wild-type and N629D mutant
* membrane potentials equal to ±200 mV and ±400 mV
* force field amber14sb, and amber14sb with charge scaling ion parameters

For each setup, it is included:
* initial system configuration
* input files
* topology
* coordinates and velocities at the end of the MD trajectory

Results of the simulations are presented in: https://www.biorxiv.org/content/10.64898/2026.09.02.748792v1
