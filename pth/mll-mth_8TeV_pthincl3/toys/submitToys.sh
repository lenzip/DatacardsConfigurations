#!/bin/bash

seed=$1

base=/afs/cern.ch/user/l/lenzip/work/ww/differential/CMSSW_6_1_1/src/DatacardsConfigurations/pth/mll-mth_8TeV_pthincl3/toys/

cd $base
eval `scram runtime -sh`
cd -
cp $base/hww-19.47fb.mH125.of_pthincl_shape_workspace.root .
combine --expectSignal=1 -t 10 -M GenerateOnly hww-19.47fb.mH125.of_pthincl_shape_workspace.root -s $seed --saveToys --toysNoSystematics 
combine --expectSignal=1 -t 10 -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --toysFile  higgsCombineTest.GenerateOnly.mH120.$seed.root -s $seed --algo=singles

cp higgsCombineTest.MultiDimFit.mH120.$seed.root $base/toysNoSystematics/


