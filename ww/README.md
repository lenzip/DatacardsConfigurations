WW
=======================

To prepare:

    ls -d ../../WW?Fcut?jet/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d */   | awk '{print "cp ../../"$1"/shape.py ./"$1"/; cp ../../"$1"/do*.sh ./"$1"/"}'

and the datadriven estimation:

    cp ../../../dd/Cut_WW_2012_20fb/*.txt   dd/




To prepare datacards:


    cd /afs/cern.ch/user/a/amassiro/Limit/ModificationDatacards
    git clone git@github.com:amassiro/ModificationDatacards.git

    rm -r ww
    mkdir ww

    scp amassiro@cmsneu:/home/amassiro/Latinos/Shape/playground/WW?Fcut?jet.tgz ww/
    cd ww
    tar -xf WWDFcut0jet.tgz
    mv datacards  WWDFcut0jet
    tar -xf WWDFcut1jet.tgz
    mv datacards  WWDFcut1jet
    tar -xf WWSFcut0jet.tgz
    mv datacards  WWSFcut0jet
    tar -xf WWSFcut1jet.tgz
    mv datacards  WWSFcut1jet

    cd WWDFcut0jet
    python ../../../ModificationDatacards/TransformShapeToCutBased.py  -d   hww-19.36fb.mH125.of_0j_shape.txt
    cd ..
    cd WWDFcut1jet
    python ../../../ModificationDatacards/TransformShapeToCutBased.py  -d   hww-19.36fb.mH125.of_1j_shape.txt
    cd ..
    cd WWSFcut0jet
    python ../../../ModificationDatacards/TransformShapeToCutBased.py  -d   hww-19.36fb.mH125.sf_0j_shape.txt
    cd ..
    cd WWSFcut1jet
    python ../../../ModificationDatacards/TransformShapeToCutBased.py  -d   hww-19.36fb.mH125.sf_1j_shape.txt
    cd ..

    rm -r WW?Fcut?jet/shapes/


and copy

    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww/



Run mu scan
====

Prepare combine framework

    export SCRAM_ARCH=slc5_amd64_gcc472
    setenv SCRAM_ARCH slc5_amd64_gcc472
    cmsrel CMSSW_6_2_0_pre3
    cd CMSSW_6_2_0_pre3/src
    cmsenv
    git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
    cd HiggsAnalysis/CombinedLimit
    git pull origin master
    git checkout V03-05-00
    scramv1 b -j 4


Get datacards:

    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww/

    cd /afs/cern.ch/user/a/amassiro/scratch0/VBF/Limit/CMSSW_6_1_0/src
    export SCRAM_ARCH=slc5_amd64_gcc462
    cmsenv

    rm -r  dc-WWDFcut0jet
    tar -xvf WWDFcut0jet.tgz
    mv datacards/ dc-WWDFcut0jet

    rm -r  dc-WWSFcut0jet
    tar -xvf WWSFcut0jet.tgz
    mv datacards/ dc-WWSFcut0jet

    rm -r  dc-WWDFcut1jet
    tar -xvf WWDFcut1jet.tgz
    mv datacards/ dc-WWDFcut1jet

    rm -r  dc-WWSFcut1jet
    tar -xvf WWSFcut1jet.tgz
    mv datacards/ dc-WWSFcut1jet

    rm *.root


Get the ad hoc combine code:

    https://github.com/amassiro/LimitScripts


Run:

    rm asymptotic*WW?Fcut?jet.out
    perl submitLocal_CutBased_PostFit.pl WWDFcut0jet
    perl submitLocal_CutBased_PostFit.pl WWSFcut0jet
    perl submitLocal_CutBased_PostFit.pl WWDFcut1jet
    perl submitLocal_CutBased_PostFit.pl WWSFcut1jet

    rm -r WW0jet
    mkdir WW0jet
    ls WWDFcut0jet/hww-*.txt | tr "/" " " | tr "." " " |  awk '{print "combineCards.py WWDF0j=WWDFcut0jet/"$2"."$3"."$4".of_0j_shape.txt  WWSF0j=WWSFcut0jet/"$2"."$3"."$4".sf_0j_shape.txt   > WW0jet/"$2"."$3"."$4".txt "}' | /bin/sh

    rm -r WW1jet
    mkdir WW1jet
    ls WWDFcut1jet/hww-*.txt | tr "/" " " | tr "." " " |  awk '{print "combineCards.py WWDF1j=WWDFcut1jet/"$2"."$3"."$4".of_1j_shape.txt  WWSF1j=WWSFcut1jet/"$2"."$3"."$4".sf_1j_shape.txt   > WW1jet/"$2"."$3"."$4".txt "}' | /bin/sh


    rm asymptotic*WW?jet.out

    perl submitLocal_CutBased_PostFit.pl WW0jet
    perl submitLocal_CutBased_PostFit.pl WW1jet







