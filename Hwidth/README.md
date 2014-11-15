Higgs width
====

emu

    0 jet: 0jetDF8TeV
    1 jet: 1jetDF8TeV
    2 jet: 2jetDF8TeV


To run the limit:

    https://github.com/amassiro/LimitCombine/tree/master/HiggsWidth/test




To prepare:

    ls -d  ../../Hwidth/*/ | tr "/" " " | awk '{print "cp ../../Hwidth/"$4"/* "$4"/"}'




To smear ntuples:

    cd /home/amassiro/Latinos/Shape/tree_skim_all_hwidth

    cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
    eval `scramv1 runtime -sh`
    source test/env.sh
    cd -

    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_160_qqww1smEM_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_161_qqww9smEM_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_162_qqww25smEM_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_169_qqww1smTM_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_170_qqww9smTT_baseW.root

    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_171_qqww25smTM_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_172_qqww1smTE_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_173_qqww9smTE_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_174_qqww25smTE_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_175_qqww9smTM_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_176_qqww1smTT_baseW.root
    bash /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/Hwidth/prepareSyst.sh latino_177_qqww25smTT_baseW.root

