#! /bin/sh
cd /afs/cern.ch/work/l/lviliani/DatacardFramework/CMSSW_6_1_1/src/HWWAnalysis/ShapeAnalysis 
eval `scramv1 runtime -sh`
source test/env.sh
cd -

mkAutopsy.py datacards/hww-19.47fb.mH125.of_pthincl_shape.txt   --dump=postFit/Hwidth-pthincl-of-error-signalInjection.root --injectionSignal --model  DatacardsConfigurations.pth.HiggsDifferentialWWSingleMu:differentialFiducialWWSingleMu --fitmode='MultiDimFit'
