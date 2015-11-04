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
inscript="Input_cff"

sed -e "s/##TOPMASS##/${topmass}/g" -e "s/##RUNNAME##/${run}/g" < ../config/${inscript}.py > ${inscript}_m${topmass}.py

cmsRun ../config/ntupleGen.py outputFile=ttbarsignalplustau_powhegbox_m${topmass}.root,inputScript=${inscript}_m${topmass},samplename=ttbarsignalplustau,systematicsName=POWHEG

