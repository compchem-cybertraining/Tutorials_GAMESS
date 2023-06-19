from molecule import Molecule
import qm, mqc
from thermostat import *
from misc import data

with open ("./init.xyz", "r") as f:
    geom = f.read()

mol = Molecule(geometry=geom, nstates=2, charge=1., unit_pos="angs")

qm = qm.gamess.SSR(molecule=mol, \
    Baeck_An = "yes", \
    gam_scr = "$GMSSCR", \
    template_file = "GMS_input_psb3.inp", \
    tmp_file_name = "GMS_run_psb3_010.tmp", \
    qm_path="/projects/academic/cyberwksp21/Software/pyUNI-xMD/uxmd2gms/", \
    nthreads=12, \
    version="01")

md = mqc.SHXF(molecule=mol, nsteps=1000, dt=0.25, istate=1, elec_object="density", rho_threshold=0.02, \
    sigma=0.2, hop_rescale="momentum", hop_reject="keep", l_xf1d=False, l_econs_state=True, \
    unit_dt="fs", verbosity=2)

md.run(qm=qm, output_dir="./", l_save_scr=True, l_save_qm_log=True, l_save_mm_log=False)

