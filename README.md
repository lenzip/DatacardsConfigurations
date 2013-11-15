DatacardsConfigurations
=======================

Collection of "shape.py" used in datacards creation

Channels considered:

    vbf
    vh2j
    whsc
    ggH2j


Ntuples folder:

    eos something ...


Datadriven folder:

    eos something ...


To prepare:

    ls -d ../*/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d */   | awk '{print "cp ../../"$1"/shape.py ./"$1"/; cp ../../"$1"/do*.sh ./"$1"/"}'

