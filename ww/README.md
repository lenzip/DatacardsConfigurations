WW
=======================

Repository
====

Where:
  
    /home/amassiro/Latinos/Shape/playground/DatacardsConfigurations/ww

To prepare:

    ls -d ../../WW?Fcut?jet/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d */   | awk '{print "cp ../../"$1"/shape.py ./"$1"/; cp ../../"$1"/do*.sh ./"$1"/"}'

and the datadriven estimation:

    cp ../../../dd/Cut_WW_2012_20fb/*.txt   dd/



Datacards
====

Cuts definition:

    https://github.com/latinos/HWWAnalysis/blob/master/ShapeAnalysis/python/hwwinfo.py#L914
    https://github.com/latinos/HWWAnalysis/blob/master/ShapeAnalysis/python/hwwinfo.py#L427

    CutWW-selection


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

    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014/

    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014_POW/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014_POW/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014_POW/

    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014_MCatNLO/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014_MCatNLO/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_26Sep2014_MCatNLO/

    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_08Oct2014_POW/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_08Oct2014_POW/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_08Oct2014_POW/

    mkdir /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_22Oct2014_POW/
    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_22Oct2014_POW/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_22Oct2014_POW/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_22Oct2014_POW/

    mkdir /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_27Oct2014_POW/
    rm -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_27Oct2014_POW/*.tgz /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_27Oct2014_POW/WW?Fcut?jet/
    cp -r * /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_27Oct2014_POW/

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

    rm -r WW?Fcut?jet/
    cp -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww/*/ ./
    cp -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_08Oct2014_POW/*/   ./
    cp -r /afs/cern.ch/user/a/amassiro/public/xLatinos/ww_27Oct2014_POW/*/   ./

Fix datacards removing unwanted nuisances:

    ls WW?Fcut?jet/*.txt |  awk '{print "cat "$1" | grep -v QCDscale_WW | grep -v QCDscale_WW1in > "$1".tmp; mv "$1".tmp "$1}' 
    ls WW?Fcut?jet/*.txt |  awk '{print "cat "$1" | grep -v QCDscale_WW | grep -v QCDscale_WW1in > "$1".tmp; mv "$1".tmp "$1}' | /bin/sh 

Prepare datacards:

    cd /afs/cern.ch/user/a/amassiro/scratch0/VBF/Limit/CMSSW_6_1_0/src
    export SCRAM_ARCH=slc5_amd64_gcc462
    cmsenv

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

    rm -r WW01jet
    mkdir WW01jet
    ls WWDFcut0jet/hww-*.txt | tr "/" " " | tr "." " " |  awk '{print "combineCards.py WWDF0j=WWDFcut0jet/"$2"."$3"."$4".of_0j_shape.txt  WWSF0j=WWSFcut0jet/"$2"."$3"."$4".sf_0j_shape.txt   > WW0jet/"$2"."$3"."$4".txt WWDF1j=WWDFcut1jet/"$2"."$3"."$4".of_1j_shape.txt  WWSF1j=WWSFcut1jet/"$2"."$3"."$4".sf_1j_shape.txt   > WW01jet/"$2"."$3"."$4".txt"}' | /bin/sh


    rm asymptotic*WW?jet.out

    perl submitLocal_CutBased_PostFit.pl WW0jet
    perl submitLocal_CutBased_PostFit.pl WW1jet
    perl submitLocal_CutBased_PostFit.pl WW01jet


Read the results:

    cat asymptotic.postFit.hww-19.125.WWDFcut0jet.out  | grep "Best fit r"
    cat asymptotic.postFit.hww-19.125.WWSFcut0jet.out  | grep "Best fit r"
    cat asymptotic.postFit.hww-19.125.WWDFcut1jet.out  | grep "Best fit r"
    cat asymptotic.postFit.hww-19.125.WWSFcut1jet.out  | grep "Best fit r"

    cat asymptotic.postFit.hww-19.125.WW0jet.out  | grep "Best fit r"
    cat asymptotic.postFit.hww-19.125.WW1jet.out  | grep "Best fit r"

    cat asymptotic.postFit.hww-19.125.WW01jet.out  | grep "Best fit r"












Fiducial cross section
====

Cuts definition:

leptons:

    abs(genVV_S1lepton1_pid) < 20
    abs(genVV_S1lepton2_pid) < 20


from W ( W = 24)

    abs(genVV_S1lepton1_oVpid)== 24 
    abs(genVV_S1lepton2_oVpid)== 24 


pt leptons > 20

    genVV_S1lepton1_pt > 20
    genVV_S1lepton2_pt > 20


different flavour

    abs(genVV_S1lepton1_pid) != abs(genVV_S1lepton2_pid)


eta cuts (mu = 13, ele = 11)

      ((abs(genVV_S1lepton1_pid)==13 && abs(genVV_S1lepton1_eta)<2.4) ||
       (abs(genVV_S1lepton1_pid)==11 && abs(genVV_S1lepton1_eta)<2.5) )

      ((abs(genVV_S1lepton2_pid)==13 && abs(genVV_S1lepton2_eta)<2.4) ||
       (abs(genVV_S1lepton2_pid)==11 && abs(genVV_S1lepton2_eta)<2.5) )

jet veto

      genVV_jet1_pt < 30




and just in one line:

    abs(genVV_S1lepton1_pid)<20   &&     abs(genVV_S1lepton2_pid)<20  &&  abs(genVV_S1lepton1_oVpid)== 24 &&    abs(genVV_S1lepton2_oVpid)!== 24  &&     genVV_S1lepton1_pt > 20   &&     genVV_S1lepton2_pt > 20  &&     abs(genVV_S1lepton1_pid) != abs(genVV_S1lepton2_pid)   &&      ((abs(genVV_S1lepton1_pid)==13 && abs(genVV_S1lepton1_eta)<2.4) ||    (abs(genVV_S1lepton1_pid)==11 && abs(genVV_S1lepton1_eta)<2.5) )  &&  ((abs(genVV_S1lepton2_pid)==13 && abs(genVV_S1lepton2_eta)<2.4) ||   (abs(genVV_S1lepton2_pid)==11 && abs(genVV_S1lepton2_eta)<2.5) )  &&        genVV_jet1_pt < 30






















