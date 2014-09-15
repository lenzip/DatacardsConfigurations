cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -



cd 0jetDF8TeV
bash doIt.sh
cd ..
rm 0jetDF8TeV.tgz
pack.py -p 0jetDF8TeV


cd 1jetDF8TeV
bash doIt.sh
cd ..
rm 1jetDF8TeV.tgz
pack.py -p 1jetDF8TeV


cd 2jetDF8TeV
bash doIt.sh
cd ..
rm 2jetDF8TeV.tgz
pack.py -p 2jetDF8TeV





