import FWCore.ParameterSet.Config as cms

process = cms.Process("PROTPGD")
# ecal mapping
process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

# magnetic field
process.load("Configuration.StandardSequences.MagneticField_cff")

# Calo geometry service model
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")

# Calo geometry service model
process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")

# IdealGeometryRecord
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("CalibCalorimetry.Configuration.Ecal_FakeConditions_cff")

#include  "SimCalorimetry/EcalTrigPrimProducers/data/ecalTriggerPrimitiveDigis.cff"
process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_with_suppressed_cff")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/cms/store/mc/2007/11/15/RelVal-RelValSingleMuMinusPt1-1195137779/0000/22F6D4B1-DF93-DC11-A2EF-000423D94494.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *_*_*_*', 
        'keep *_ecalTriggerPrimitiveDigis_*_*', 
        'keep *_ecalDigis_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalWeightUncalibRecHit_*_*', 
        'keep PCaloHits_*_EcalHitsEB_*', 
        'keep PCaloHits_*_EcalHitsEE_*', 
        'keep edmHepMCProduct_*_*_*'),
    fileName = cms.untracked.string('TrigPrim2.root')
)

process.MessageLogger = cms.Service("MessageLogger")

process.p = cms.Path(process.simEcalTriggerPrimitiveDigis)
process.outpath = cms.EndPath(process.out)
process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_cosmics.txt'


