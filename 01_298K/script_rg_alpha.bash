#!/bin/bash
if [ $# -ne 1 ]
then
echo "usage: ./script_rg_alpha.bash COLVAR_file"
exit 0
fi

wait
grep -v "^#" ${1} | awk '{print $2, $5}' > gyrate_alpha.dat
wait
python3 histograms.py gyrate_alpha.dat 0.6 0 2.5 15.0 50 50
wait

