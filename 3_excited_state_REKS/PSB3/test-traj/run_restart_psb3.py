import pickle

with open("RESTART.bin", "rb") as fr:
    data = pickle.load(fr)
    qm = data['qm']
    md = data['md']

qm.nthreads=16

md.run(qm=qm, output_dir="./", l_save_scr=True, l_save_qm_log=True, l_save_mm_log=False, restart="append")

