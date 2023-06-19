
## 1. Run optimizations in the ground and excited states

    cd s0min-cis
    sbatch submit.slm


    cd ../s0min-trans
    sbatch submit.slm

 
    cd ../s1min
    sbatch submit.slm


## 2. Normal mode calculations

    cd ../normal_modes

  Update the input files with the optimized geometry and start the Hessian calculations

    sbatch submit.slm

  there will be the .out file with the vibrational frequencies


## 3. Sample initial conditions [E.g. using this tutorials](https://vdv.dcf.mybluehost.me/nx/wp-content/uploads/2020/02/tutorial-2_2.pdf) 
   
### 3.1. We need to prepare these two files:

   - geom  (geometry)

   - gamess.out (output of the vibrational calculations)
  

   Rename your GAMESS Hessian job output file (`psb3-s0min-ssr-bhhlyp-6-31gs.out`) to `gamess.out`

   Prepare geom.xyz file using the last geometry of the trans conformer optimization. 

   Convert it to the Newton-X format:

    $NX/xyz2nx < geom.xyz
   

### 3.2.  Generate the input file for initial conditions sampling by running:

    $NX/nxinp

   using answers: 1 - 3 - Enter - 10 - Enter - 1 - Enter - Enter - 300.0 - n - Enter - Enter - Enter - 7

   This generates the file `initqp_input
  

### 3.3. Now generate the initial conditions:

    $NX/initcond.pl > initcond.log

   Look for the `final_output` file


### 3.4. Pick any initial condition from it and use to create the `init.xyz` file in the dynamics folder

   Note: NX generates the coordinates in atomic units, so you'll need to update the input file of PyUNIxMD


## 5. Run NA-MD [e.g. using this Tutorial](https://jkha-rtd-test.readthedocs.io/en/latest/objects/mqc/shxf.html)
   
     cd ../test-traj
     sbatch submit.slm

   
