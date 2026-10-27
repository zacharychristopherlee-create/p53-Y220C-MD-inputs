# p53-Y220C-MD-inputs
 
Input parameter files and scripts for the molecular dynamics (MD) simulations in:
 
**P53 Mutant Structures Predicted by AlphaFold and Molecular Dynamics Simulations of Candidate Stabilizing Compounds**
 
This repository contains inputs only. Trajectories, structures and output files are not included because of their size.
 
## Files
 
| File | Purpose |
|---|---|
| `minim.mdp` | Energy minimization (steepest descent, `emtol` = 1000 kJ mol⁻¹ nm⁻¹, 50,000 steps) |
| `ions.mdp` | Parameter file used with `grompp` before `genion` to neutralize the system with Na⁺ and Cl⁻ |
| `nvt.mdp` | NVT equilibration: 500 ps (250,000 steps × 2 fs), V-rescale thermostat at 300 K, position restraints, velocities generated at 300 K |
| `npt.mdp` | NPT equilibration: 500 ps (250,000 steps × 2 fs), V-rescale thermostat at 300 K, Berendsen barostat at 1 bar, position restraints |
| `md-277K.mdp` | Production MD at 277 K: 10,000,000 steps × 2 fs = 20 ns, V-rescale thermostat, Parrinello–Rahman barostat at 1 bar, coordinates saved every 10 ps |
| `md-310K.mdp` | Production MD at 310 K: identical to `md-277K.mdp` except for `ref_t` |
| `tleap.in` | AmberTools `tleap` input used when preparing the CDB3 peptide for GROMACS (ff19SB and GAFF2 parameters) |
| `merge.py` | ParmEd script used to merge the protein and ligand topologies and coordinates |
 
## Simulated systems
 
Six systems were each simulated at 277 K and 310 K (12 simulations, one trajectory per system, 20 ns each):
 
1. Wild-type p53 DNA-binding domain
2. Y220C p53 DNA-binding domain
3. Wild-type p53–DNA complex
4. Y220C p53–DNA complex
5. Y220C–DNA complex with rezatapopt
6. Y220C–DNA complex with CDB3
## Workflow
 
1. Structure prediction with AlphaFold 3 (UniProt P04637, residues 89–293; Y220C substitution introduced in the input sequence). The first model was converted from mmCIF to PDB with GEMMI.
2. GROMACS `pdb2gmx` with the AMBERGS force field and the SPC/E water model (hydrogens ignored).
3. `editconf` to create a cubic box with at least 1.2 nm between the molecule and the box edge, then `solvate` with `spc216`.
4. `grompp` with `ions.mdp`, then `genion` to neutralize with NA and CL.
5. Energy minimization (`minim.mdp`).
6. NVT equilibration (`nvt.mdp`), then NPT equilibration (`npt.mdp`).
7. Production MD (`md-277K.mdp` or `md-310K.mdp`).
8. Analysis of the trajectories: backbone RMSD, radius of gyration, RMSF (residues 200–220), protein–DNA hydrogen bonds, protein–DNA contacts, and the distance between residue 248 and the DNA phosphates.
For the CDB3 and rezatapopt systems, the ligand was prepared as described in the Methods of the paper (AlphaFold structure of CDB3, docking in PyRx with AutoDock Vina, parameters from `tleap.in`, merged with `merge.py`).
 
## Notes
 
- All systems were equilibrated at 300 K. The production temperature (277 K or 310 K) is set only by `ref_t` in the production file.
- Each system was simulated once.
- Software: GROMACS 2026.3, AlphaFold 3 v3.0.4, AmberTools (`tleap`, `antechamber`, `parmchk2`), ACPYPE, ParmEd, GEMMI, PyMOL, PyRx.
## Citation
 
Please cite the paper above. Citation details will be added here after publication.
 
