
1. Run optimizations in the ground and excited states

    cd s0min-cis
    sbatch submit.slm


    cd ../s0min-trans
    sbatch submit.slm

 
    cd ../s1min
    sbatch submit.slm


2. Normal mode calculations

    cd ../normal_modes

  Update the input files with the optimized geometry and start the Hessian calculations

    sbatch submit.slm

  there will be the .out file with the vibrational frequencies


3. Sample initial conditions
   
   We need to prepare these two files:

   - geom  (geometry)

   - gamess.out (output of the vibrational calculations)
  
   Prepare geom.xyz file using the last geometry of the trans conformer optimization

    $NX/xyz2nx < geom.xyz


4. Generate the input file in the Newton-X format

   https://vdv.dcf.mybluehost.me/nx/wp-content/uploads/2020/02/tutorial-2_2.pdf
 

   using answers: 1 - 3 - Enter - 10 - Enter - 1 - Enter - Enter - 300.0 - n - Enter - Enter - Enter - 7

   This generates the file `initqp_init`
  
   Now generate the initial conditions:

    $NX/initcond.pl > initcond.log

  Look for the `final_output` file

  Pick any initial condition from it


5. Create an iniput for the dynamics
   E.g.
   https://jkha-rtd-test.readthedocs.io/en/latest/objects/mqc/shxf.html

     cd ../test-traj
     sbatch submit.slm

   
