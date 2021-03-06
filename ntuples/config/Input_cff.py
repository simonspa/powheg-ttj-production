import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0001.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0002.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0003.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0004.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0005.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0006.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0007.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0008.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0009.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0010.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0011.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0012.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0013.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0014.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0015.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0016.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0017.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0018.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0019.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0020.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0021.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0022.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0023.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0024.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0025.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0026.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0027.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0028.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0029.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0030.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0031.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0032.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0033.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0034.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0035.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0036.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0037.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0038.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0039.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0040.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0041.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0042.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0043.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0044.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0045.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0046.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0047.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0048.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0049.root',
    'file:/nfs/dust/cms/user/spanns/montecarlo-generation/hadronization/##RUNNAME##_m##TOPMASS##/dilepton_m##TOPMASS##-0050.root',
    ] );
secFiles.extend( [
               ] )

