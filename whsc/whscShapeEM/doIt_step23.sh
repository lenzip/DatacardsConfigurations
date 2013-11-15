#! /bin/sh


rm -r merged
rm -r datacards


cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -



mkMerged.py -m 110
mkMerged.py -m 115
mkMerged.py -m 120
mkMerged.py -m 125
mkMerged.py -m 130
mkMerged.py -m 135
mkMerged.py -m 140
mkMerged.py -m 145
mkMerged.py -m 150
mkMerged.py -m 155
mkMerged.py -m 160
mkMerged.py -m 170
mkMerged.py -m 180
mkMerged.py -m 190
mkMerged.py -m 200
mkMerged.py -m 250
mkMerged.py -m 300


mkDatacards.py -m 110
mkDatacards.py -m 115
mkDatacards.py -m 120
mkDatacards.py -m 125
mkDatacards.py -m 130
mkDatacards.py -m 135
mkDatacards.py -m 140
mkDatacards.py -m 145
mkDatacards.py -m 150
mkDatacards.py -m 155
mkDatacards.py -m 160
mkDatacards.py -m 170
mkDatacards.py -m 180
mkDatacards.py -m 190
mkDatacards.py -m 200
mkDatacards.py -m 250
mkDatacards.py -m 300


