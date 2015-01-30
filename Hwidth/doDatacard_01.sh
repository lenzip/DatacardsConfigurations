cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -



cd 01jetDF8TeV
bash doIt.sh
cd ..
rm 01jetDF8TeV.tgz
pack.py -p 01jetDF8TeV



