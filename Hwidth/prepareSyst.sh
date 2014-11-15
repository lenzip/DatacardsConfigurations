scaleAndSmearTree.py -i nominals/$1 -o jetEnergyScale_up/$1 -a jetEnergyScale -v up
scaleAndSmearTree.py -i nominals/$1 -o jetEnergyScale_down/$1 -a jetEnergyScale -v down

scaleAndSmearTree.py -i nominals/$1 -o electronScale_up/$1 -a electronScale -v up
scaleAndSmearTree.py -i nominals/$1 -o electronScale_down/$1 -a electronScale -v down

scaleAndSmearTree.py -i nominals/$1 -o muonScale_up/$1 -a muonScale -v up
scaleAndSmearTree.py -i nominals/$1 -o muonScale_down/$1 -a muonScale -v down

scaleAndSmearTree.py -i nominals/$1 -o metResolution/$1 -a metResolution
scaleAndSmearTree.py -i nominals/$1 -o electronResolution/$1 -a electronResolution

# scaleAndSmearTree.py -i nominals/$1 -o JER_up/$1 -a jetEnergyResolution -v up
# scaleAndSmearTree.py -i nominals/$1 -o JER_down/$1 -a jetEnergyResolution -v down

#
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh      latino000_nll_ewk.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh      latino002_nll_ewk.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh      latino006_nll_ewk.root
#
#  ls nominals/latino*_baseW.root | tr "/" " " | awk '{print "bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh "$2}'
#

# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_160_qqww1smEM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_161_qqww9smEM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_162_qqww25smEM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_169_qqww1smTM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_170_qqww9smTT_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_171_qqww25smTM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_172_qqww1smTE_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_173_qqww9smTE_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_174_qqww25smTE_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_175_qqww9smTM_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_176_qqww1smTT_baseW.root
# bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_177_qqww25smTT_baseW.root
