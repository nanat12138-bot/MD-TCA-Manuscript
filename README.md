1. Study Information
Title
Molecular dynamics insights into orientation-dependent tension-compression yield stress asymmetry of Ni/Ni₃Al single-crystal superalloys
2. Software Requirements
The simulations and data analysis were performed using:
LAMMPS (simulation)
Atomsk (for model construction)
OVITO Basic/Pro 3.x (include link to  Python) (Visualization)
Python 3.10 (for model construction and analysis)
3. Directory Structure
Figure_data/
  Figure_data_all (includes all the chart data from the papers)
  misfit_V-strain-stress-remain data (remaining auxiliary data)
  ovito_burgers_num.py (count the dislocation)
  ovito_dislocation length.py (count the dislocation to calculating dislocation density)
  polar_coordinate.py (calculate polar coordinates)
  schmid factor.py (Calculate schmid factor)
model and loading/
  in.com (simulate the compression process)
  in.ten (simulate the tension process)
  in.relax (relaxing)
  model_standard.py (build the standard cube model)
  model_change the orientation.py (building the non-standard model)
  CSL_lattice constant.py (After adjusting the lattice constants, calculate the minimum lattice matching number.)
  orientation_Matrix.py (calculate target crystal orientation matrix)
  Ni.eam.alloy (the simulations employed the embedded atom method (EAM) potential included in this file and no modification was made to the potential file.)
4. Simulation Procedure
The simulations can be reproduced using the following steps.
-Step 1
Prepare the initial model.
  model_standard.py
  model_change the orientation.py
  CSL_lattice constant.py
  orientation_Matrix.py
-Step 2
Relax the structure.
  in.relax
-Step 3
Perform simulation.
  in.com
  in.ten
-Step 4
Analyze data
  ovito_burgers_num.py
  ovito_dislocation length.py
  visualizing with Ovito
