DatacardsConfigurations
=======================

Collection of "shape.py" used in datacards creation

Channels considered:

    vbf
    vh2j
    whsc
    ggH2j
    ww   (0/1 jet SF/DF)
    ww2j (ewk and qcd)


Ntuples folder:

    eos something ...

    7 TeV
    /afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Tree/tree_42x_skim_wwmin/

    8 TeV
    /afs/cern.ch/user/m/maiko/work/public/Tree/tree_skim_wwmin/


Datadriven folder:

    for each channel in the correct folder


To prepare:

    ls -d ../*/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d */   | awk '{print "cp ../../"$1"/shape.py ./"$1"/; cp ../../"$1"/do*.sh ./"$1"/"}'


