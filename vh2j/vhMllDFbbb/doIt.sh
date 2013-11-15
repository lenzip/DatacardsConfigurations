#! /bin/sh


rm -r raw
rm -r merged
rm -r datacards



cd /data2/amassiro/VBF/Summer12/28Jan2013/CMSSW_6_1_0/src/HWWAnalysis/ShapeAnalysis/
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




mkDatacards.py -m 110   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 115   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 120   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 125   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 130   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 135   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 140   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 145   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 150   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 155   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 160   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 170   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 180   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 190   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 200   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 250   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 300   --Xsh=CMS_8TeV_ch_res

# 
# 
# mkdir postFit
# 
# mkAutopsy.py datacards/hww-12.10fb.mH110.of_2j_shape.txt  -m 110  --dump postFit/mH110.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH115.of_2j_shape.txt  -m 115  --dump postFit/mH115.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH120.of_2j_shape.txt  -m 120  --dump postFit/mH120.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH125.of_2j_shape.txt  -m 125  --dump postFit/mH125.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH130.of_2j_shape.txt  -m 130  --dump postFit/mH130.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH135.of_2j_shape.txt  -m 135  --dump postFit/mH135.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH140.of_2j_shape.txt  -m 140  --dump postFit/mH140.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH145.of_2j_shape.txt  -m 145  --dump postFit/mH145.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH150.of_2j_shape.txt  -m 150  --dump postFit/mH150.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH155.of_2j_shape.txt  -m 155  --dump postFit/mH155.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH160.of_2j_shape.txt  -m 160  --dump postFit/mH160.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH170.of_2j_shape.txt  -m 170  --dump postFit/mH170.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH180.of_2j_shape.txt  -m 180  --dump postFit/mH180.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH190.of_2j_shape.txt  -m 190  --dump postFit/mH190.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH200.of_2j_shape.txt  -m 200  --dump postFit/mH200.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH250.of_2j_shape.txt  -m 250  --dump postFit/mH250.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH300.of_2j_shape.txt  -m 300  --dump postFit/mH300.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH350.of_2j_shape.txt  -m 350  --dump postFit/mH350.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH400.of_2j_shape.txt  -m 400  --dump postFit/mH400.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH450.of_2j_shape.txt  -m 450  --dump postFit/mH450.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH500.of_2j_shape.txt  -m 500  --dump postFit/mH500.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH550.of_2j_shape.txt  -m 550  --dump postFit/mH550.root -o plot
# mkAutopsy.py datacards/hww-12.10fb.mH600.of_2j_shape.txt  -m 600  --dump postFit/mH600.root -o plot
