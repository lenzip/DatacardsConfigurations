
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


mkdir electronResolution
mkdir electronScale_down
mkdir electronScale_up
mkdir jetEnergyScale_down
mkdir jetEnergyScale_up
mkdir metResolution
mkdir muonScale_down
mkdir muonScale_up
