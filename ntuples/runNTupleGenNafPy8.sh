#!/bin/bash

if [ $2 ]
then
    topmass=$2
    echo "Generating ntuple for mass mt = $topmass, using script $inscript"
else
    echo "Usage: runNTupleGen.sh RUNNAME TOPMASS"
    exit
fi

run=$1

for i in {1..501} #NJOBS
do
  paddedjob=`echo ${i} | awk '{printf("%04s\n", $1)}'`
  sed -e "s/##JOBNUMBER##/${paddedjob}/g" -e "s/##TOPMASS##/${topmass}/g" -e "s/##RUNNAME##/${run}/g" < ../config/cmsntupleNodePy8.sh > cmsntupleNode${i}.sh
  qsub -js 2 -N "ntp-m${topmass}" cmsntupleNode${i}.sh

done

