
mkdir nominals
eos cp /eos/cms/store/user/maiko/ww/ntuples/systematics2013/nominals/*.root nominals/

mkdir data
eos cp /eos/cms/store/user/maiko/ww/ntuples/systematics2013/data/*.root data/

mkdir wjets
eos cp /eos/cms/store/user/maiko/ww/ntuples/systematics2013/wjets/*.root wjets


mkdir templates

mkdir vgTemplate
eos cp /eos/cms/store/user/maiko/ww/ntuples/systematics2013/vgTemplate/*.root vgTemplate

cd templates
ln -s ../vgTemplate/*root .
ln -s ../nominals/*root .



mkdir jetEnergyScale_down
mkdir jetEnergyScale_up

mkdir electronScale_down
mkdir electronScale_up

mkdir muonScale_down
mkdir muonScale_up

mkdir metResolution
mkdir electronResolution



cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -



ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o jetEnergyScale_up/"$1"    -a jetEnergyScale -v up"}'  | /bin/sh
ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o jetEnergyScale_down/"$1"  -a jetEnergyScale -v down"}'| /bin/sh

ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o electronScale_up/"$1"    -a electronScale -v up"}'| /bin/sh
ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o electronScale_down/"$1"  -a electronScale -v down"}'| /bin/sh

ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o muonScale_up/"$1"    -a muonScale -v up"}'| /bin/sh
ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o muonScale_down/"$1"  -a muonScale -v down"}'| /bin/sh

ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o metResolution/"$1"         -a metResolution"}'| /bin/sh
ls --color=none nominals/ | grep .root | awk '{print "scaleAndSmearTree.py -i nominals/"$1" -o electronResolution/"$1"    -a electronResolution"}'| /bin/sh



