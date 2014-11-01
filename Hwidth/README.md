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
