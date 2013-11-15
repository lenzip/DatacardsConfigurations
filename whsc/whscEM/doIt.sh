#! /bin/sh


rm -r raw
rm -r merged
rm -r datacards


cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -


mkShapes.py -m 110
mkShapes.py -m 115
mkShapes.py -m 120
mkShapes.py -m 125
mkShapes.py -m 130
mkShapes.py -m 135
mkShapes.py -m 140
mkShapes.py -m 145
mkShapes.py -m 150
mkShapes.py -m 155
mkShapes.py -m 160
mkShapes.py -m 170
mkShapes.py -m 180
mkShapes.py -m 190
mkShapes.py -m 200
mkShapes.py -m 250
mkShapes.py -m 300




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
