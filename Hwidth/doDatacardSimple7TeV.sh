cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -



cd 0jetDF7TeVSimple
bash doIt.sh
cd ..
rm 0jetDF7TeVSimple.tgz
pack.py -p 0jetDF7TeVSimple


cd 1jetDF7TeVSimple
bash doIt.sh
cd ..
rm 1jetDF7TeVSimple.tgz
pack.py -p 1jetDF7TeVSimple


cd 2jetDF7TeVSimple
bash doIt.sh
cd ..
rm 2jetDF7TeVSimple.tgz
pack.py -p 2jetDF7TeVSimple


