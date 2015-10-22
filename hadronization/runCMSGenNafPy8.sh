#!/bin/bash

if [ $2 ]
then
    topmass=$2
    mass="${topmass/p/.}"
    run=$1
    gennode="cmsgenNodePy8.sh-tmpl"
    echo "Generating samples for mass mt = $topmass, file $gennode"
else
    echo "runCMSGenNaf.sh RUNNAME TOPMASS"
    exit
fi


for i in {1..250} #NJOBS
do
  paddedjob=`echo ${i} | awk '{printf("%04s\n", $1)}'`
  sed -e "s/##JOBNUMBER##/${paddedjob}/g" -e "s/##MASS##/${mass}/g" -e "s/##TOPMASS##/${topmass}/g" -e "s/##RUNNAME##/${run}/g" < ../config/Hadronizer_Tune4C_emissionVeto1_LHE_pythia8.py-tmpl > Hadronizer_Tune4C_emissionVeto1_LHE_pythia8-${paddedjob}.py
  sed -e "s/##JOBNUMBER##/${paddedjob}/g" -e "s/##TOPMASS##/${topmass}/g" -e "s/##RUNNAME##/${run}/g" < ../config/${gennode} > cmsgenNode${i}.sh
  qsub cmsgenNode${i}.sh
done

