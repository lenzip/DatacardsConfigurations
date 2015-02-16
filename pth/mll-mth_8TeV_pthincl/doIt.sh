#! /bin/sh
rm -r raw
rm -r merged
rm -r datacards
cd /afs/cern.ch/user/l/lenzip/work/ww/differential/CMSSW_6_1_1/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -

mkShapes.py -m 125

mkMerged.py -m 125

mkDatacards.py -m 125


mkAutopsy.py datacards/hww-19.47fb.mH125.of_pthincl_shape.txt   --dump=postFit/Hwidth-pthincl-of-error-signalInjection.root --injectionSignal --model DatacardsConfigurations.pth.HiggsDifferentialWW:differentialFiducialWW --fitmode='MultiDimFit'
#mkAutopsy.py datacards/hww-19.47fb.mH125.of_pth1_shape.txt   --dump=postFit/Hwidth-pth1-of-error-data.root




