scaleAndSmearTree.py -i nominals/$1 -o jetEnergyScale_up/$1 -a jetEnergyScale -v up
scaleAndSmearTree.py -i nominals/$1 -o jetEnergyScale_down/$1 -a jetEnergyScale -v down

scaleAndSmearTree.py -i nominals/$1 -o electronScale_up/$1 -a electronScale -v up
scaleAndSmearTree.py -i nominals/$1 -o electronScale_down/$1 -a electronScale -v down

scaleAndSmearTree.py -i nominals/$1 -o muonScale_up/$1 -a muonScale -v up
scaleAndSmearTree.py -i nominals/$1 -o muonScale_down/$1 -a muonScale -v down

scaleAndSmearTree.py -i nominals/$1 -o metResolution/$1 -a metResolution
scaleAndSmearTree.py -i nominals/$1 -o electronResolution/$1 -a electronResolution

scaleAndSmearTree.py -i nominals/$1 -o JER_up/$1 -a jetEnergyResolution -v up
scaleAndSmearTree.py -i nominals/$1 -o JER_down/$1 -a jetEnergyResolution -v down

#
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/ww/prepareSyst.sh      latino000_nll_ewk.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/ww/prepareSyst.sh      latino002_nll_ewk.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/ww/prepareSyst.sh      latino006_nll_ewk.root
#