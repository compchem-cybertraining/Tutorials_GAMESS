sbatch -N1 -n12 -p valhalla -q valhalla -M faculty -o neb.out sbatchwrap.sh $DLFPATH/find.x input.dlf

sbatch -N1 -n12 -p valhalla -q valhalla -M faculty -o output-tmp-00-reks.out sbatchwrap.sh gmsrun tmp_00_reks.inp

