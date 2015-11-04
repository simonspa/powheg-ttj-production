#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#$ -l site=hh
#
# Require SL6 operating systems:
#$ -l os=sld6
#
#(the cpu time for this job)
#$ -l h_rt=30:00:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=4096M
#
#(stderr and stdout are merged together to stdout)
#$ -j y
#$ -m a 
#$ -V
#$ -cwd
#$ -l h_stack=1536M
#$ -R y

cmsRun ../config/ntuple_8tev_latestReleases_naf.py outputFile=ttbarsignalplustau_powhegbox_m##TOPMASS##-##JOBNUMBER##.root,inputFile="file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-##JOBNUMBER##.root",samplename=ttbarsignalplustau,systematicsName=POWHEG > run-##JOBNUMBER##.log 2>&1
