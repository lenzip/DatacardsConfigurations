#! /bin/sh


rm -r merged
rm -r datacards


cd /data2/amassiro/VBF/Summer12/28Jan2013/CMSSW_6_1_0/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -





rm ScaleFactors.py

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
mkMerged.py -m 350
mkMerged.py -m 400
mkMerged.py -m 450
mkMerged.py -m 500
mkMerged.py -m 550
mkMerged.py -m 600




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
mkDatacards.py -m 160   --Xsh=CMS_8TeV_ch_res --Xsh=CMS_8TeV_hww_WJet_FakeRate_e_shape_2j --Xsh=CMS_8TeV_hww_WJet_FakeRate_m_shape_2j
mkDatacards.py -m 170   --Xsh=CMS_8TeV_ch_res --Xsh=CMS_8TeV_hww_WJet_FakeRate_e_shape_2j --Xsh=CMS_8TeV_hww_WJet_FakeRate_m_shape_2j
mkDatacards.py -m 180   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 190   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 200   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 250   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 300   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 350   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 400   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 450   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 500   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 550   --Xsh=CMS_8TeV_ch_res
mkDatacards.py -m 600   --Xsh=CMS_8TeV_ch_res


