DatacardsConfigurations
=======================

Collection of "shape.py" used in datacards creation

Channels considered:

    vbf
       shape
       cut
    vh2j
       shape
       cut
    whsc
       shape
       cut
    ggH2j
       shape




To prepare:

    ls -d ../*/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d */   | awk '{print "cp ../../"$1"/shape.py ./"$1"/; cp ../../"$1"/do*.sh ./"$1"/"}'

