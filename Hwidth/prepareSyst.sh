scaleAndSmearTree.py -i nominals/$1 -o jetEnergyScale_up/$1    -a jetEnergyScale -v up
scaleAndSmearTree.py -i nominals/$1 -o jetEnergyScale_down/$1  -a jetEnergyScale -v down

scaleAndSmearTree.py -i nominals/$1 -o electronScale_up/$1    -a electronScale -v up
scaleAndSmearTree.py -i nominals/$1 -o electronScale_down/$1  -a electronScale -v down

scaleAndSmearTree.py -i nominals/$1 -o muonScale_up/$1    -a muonScale -v up
scaleAndSmearTree.py -i nominals/$1 -o muonScale_down/$1  -a muonScale -v down

scaleAndSmearTree.py -i nominals/$1 -o metResolution/$1    -a metResolution
scaleAndSmearTree.py -i nominals/$1 -o electronResolution/$1  -a electronResolution

# scaleAndSmearTree.py -i nominals/$1 -o JER_up/$1    -a jetEnergyResolution -v up
# scaleAndSmearTree.py -i nominals/$1 -o JER_down/$1  -a jetEnergyResolution -v down



# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw25_SigTail_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw1_IntOnPeak_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw1_IntShoulder_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw1_IntTail_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw1_SigOnPeak_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw1_SigShoulder_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw1_SigTail_8TeV.root
#
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw25_CotHead_8TeV.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latinogg2vv_Hw25_CotTail_8TeV.root
#
#
# /afs/cern.ch/user/j/jfernan2/public/forAndrea/latino_150_qqww1sm.root
# /afs/cern.ch/user/j/jfernan2/public/forAndrea/latino_151_qqww9sm.root
# /afs/cern.ch/user/j/jfernan2/public/forAndrea/latino_152_qqww25sm.roo
#
#
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latino_150_qqww1sm.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latino_151_qqww9sm.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latino_152_qqww25sm.root
#
# cd /home/amassiro/Latinos/Shape/tree_skim_all/
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latino_160_qqww1smEM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latino_161_qqww9smEM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/Hwidth/prepareSyst.sh    latino_162_qqww25smEM_baseW.root
#
