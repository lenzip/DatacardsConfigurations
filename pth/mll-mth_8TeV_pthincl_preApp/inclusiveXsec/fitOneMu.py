import os
from ROOT import *

correlated = ["CMS_8TeV_hww_FakeRate","CMS_8TeV_norm_DYTT","CMS_8TeV_norm_Vg","QCDscale_VV","QCDscale_VVV","QCDscale_VgS","QCDscale_WW","QCDscale_WW1in","QCDscale_ggH","QCDscale_ggH1in","QCDscale_ggWW","lumi_8TeV","pdf_gg_ACCEPT","pdf_qqbar_ACCEPT","CMS_8TeV_btagsf","CMS_8TeV_eff_l","CMS_8TeV_hww_Top0jet_fTW","CMS_8TeV_hww_WJet_FakeRate_e_shape","CMS_8TeV_hww_WJet_FakeRate_m_shape","CMS_8TeV_met","CMS_8TeV_p_res_e","CMS_8TeV_p_scale_e","CMS_8TeV_p_scale_j","CMS_8TeV_p_scale_m","CMS_8TeV_p_scale_met"]

#command = "combine --saveWorkspace --expectSignal=1 -t -1 -M MultiDimFit datacardsOneMu/hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --saveToys&> logFull.txt"
command = "combine --saveWorkspace --expectSignal=1 -t -1 --toysFrequentist -M MultiDimFit datacardsOneMu/hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --saveToys&> logFull_postFitAsimov.txt"
os.popen(command)

#command = "combine --saveWorkspace --expectSignal=1 -t -1 -M MultiDimFit datacardsOneMu/hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances="+",".join(correlated)+"&>logStatOnly.txt"
command = "combine --saveWorkspace --expectSignal=1 -t -1 --toysFrequentist -M MultiDimFit datacardsOneMu/hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances="+",".join(correlated)+"&>logStatOnly_postFitAsimov.txt"
os.popen(command)

