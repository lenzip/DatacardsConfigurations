#/usr/bin/env python
import os
from ROOT import *
import sys

allsyst = ["CMS_8TeV_hww_FakeRate","CMS_8TeV_norm_DYTT","CMS_8TeV_norm_Vg","CMS_norm_pthincl_WWBin0","CMS_norm_pthincl_WWBin1","CMS_norm_pthincl_WWBin2","CMS_norm_pthincl_WWBin3","CMS_norm_pthincl_WWBin4","CMS_norm_pthincl_WWBin5","QCDscale_VV","QCDscale_VVV","QCDscale_VgS","QCDscale_WW","QCDscale_WW1in","QCDscale_ggH","QCDscale_ggH1in","QCDscale_ggH2in","QCDscale_ggWW","lumi_8TeV","pdf_gg_ACCEPT","pdf_qqbar_ACCEPT","CMS_8TeV_hww_ggHBin0_of_pthincl_stat_bin1","CMS_8TeV_hww_ggHBin1_of_pthincl_stat_bin1","CMS_8TeV_hww_ggHBin2_of_pthincl_stat_bin1","CMS_8TeV_hww_ggHBin3_of_pthincl_stat_bin1","CMS_8TeV_hww_ggHBin4_of_pthincl_stat_bin1","CMS_8TeV_hww_ggHBin5_of_pthincl_stat_bin1","CMS_8TeV_hww_qqHBin0_of_pthincl_stat_bin1","CMS_8TeV_hww_qqHBin1_of_pthincl_stat_bin1","CMS_8TeV_hww_qqHBin2_of_pthincl_stat_bin1","CMS_8TeV_hww_qqHBin3_of_pthincl_stat_bin1","CMS_8TeV_hww_qqHBin4_of_pthincl_stat_bin1","CMS_8TeV_hww_qqHBin5_of_pthincl_stat_bin1","CMS_8TeV_hww_WHBin0_of_pthincl_stat_bin1","CMS_8TeV_hww_WHBin1_of_pthincl_stat_bin1","CMS_8TeV_hww_WHBin2_of_pthincl_stat_bin1","CMS_8TeV_hww_WHBin3_of_pthincl_stat_bin1","CMS_8TeV_hww_WHBin4_of_pthincl_stat_bin1","CMS_8TeV_hww_WHBin5_of_pthincl_stat_bin1","CMS_8TeV_hww_ZHBin0_of_pthincl_stat_bin1","CMS_8TeV_hww_ZHBin1_of_pthincl_stat_bin1","CMS_8TeV_hww_ZHBin2_of_pthincl_stat_bin1","CMS_8TeV_hww_ZHBin3_of_pthincl_stat_bin1","CMS_8TeV_hww_ZHBin4_of_pthincl_stat_bin1","CMS_8TeV_hww_ZHBin5_of_pthincl_stat_bin1","CMS_8TeV_hww_ggWW_of_pthincl_stat_bin1","CMS_8TeV_hww_VgS_of_pthincl_stat_bin1","CMS_8TeV_hww_Vg_of_pthincl_stat_bin1","CMS_8TeV_hww_WJet_of_pthincl_stat_bin1","CMS_8TeV_hww_VV_of_pthincl_stat_bin1","CMS_8TeV_hww_DYTT_of_pthincl_stat_bin1","CMS_8TeV_hww_VVV_of_pthincl_stat_bin1","CMS_8TeV_hww_WWBin0_of_pthincl_stat_bin1","CMS_8TeV_hww_WWBin1_of_pthincl_stat_bin1","CMS_8TeV_hww_WWBin2_of_pthincl_stat_bin1","CMS_8TeV_hww_WWBin3_of_pthincl_stat_bin1","CMS_8TeV_hww_WWBin4_of_pthincl_stat_bin1","CMS_8TeV_hww_WWBin5_of_pthincl_stat_bin1","CMS_8TeV_hww_Topge1jetBin3_pthincl_of_pthincl_extr","CMS_8TeV_hww_Topge1jetBin3_pthincl_of_pthincl_stat","CMS_8TeV_hww_Topge1jetBin2_pthincl_of_pthincl_extr","CMS_8TeV_hww_Topge1jetBin2_pthincl_of_pthincl_stat","CMS_8TeV_hww_Topge1jetBin1_pthincl_of_pthincl_extr","CMS_8TeV_hww_Topge1jetBin1_pthincl_of_pthincl_stat","CMS_8TeV_hww_Topge1jetBin0_pthincl_of_pthincl_extr","CMS_8TeV_hww_Topge1jetBin0_pthincl_of_pthincl_stat","CMS_8TeV_hww_Topge1jetBin5_pthincl_of_pthincl_extr","CMS_8TeV_hww_Topge1jetBin5_pthincl_of_pthincl_stat","CMS_8TeV_hww_Topge1jetBin4_pthincl_of_pthincl_extr","CMS_8TeV_hww_Topge1jetBin4_pthincl_of_pthincl_stat","CMS_8TeV_hww_Top0jet_pthincl_of_pthincl_extr","CMS_8TeV_hww_Top0jet_pthincl_of_pthincl_stat","CMS_8TeV_btagsf","CMS_8TeV_eff_l","CMS_8TeV_hww_DYTT_of_pthincl_stat_shape","CMS_8TeV_hww_Top0jet_fTW","CMS_8TeV_hww_Top0jet_of_pthincl_stat_shape","CMS_8TeV_hww_Topge1jetBin0_fTW","CMS_8TeV_hww_Topge1jetBin0_of_pthincl_stat_shape","CMS_8TeV_hww_Topge1jetBin1_fTW","CMS_8TeV_hww_Topge1jetBin1_of_pthincl_stat_shape","CMS_8TeV_hww_Topge1jetBin2_fTW","CMS_8TeV_hww_Topge1jetBin2_of_pthincl_stat_shape","CMS_8TeV_hww_Topge1jetBin3_fTW","CMS_8TeV_hww_Topge1jetBin3_of_pthincl_stat_shape","CMS_8TeV_hww_Topge1jetBin4_fTW","CMS_8TeV_hww_Topge1jetBin4_of_pthincl_stat_shape","CMS_8TeV_hww_Topge1jetBin5_fTW","CMS_8TeV_hww_Topge1jetBin5_of_pthincl_stat_shape","CMS_8TeV_hww_VVV_of_pthincl_stat_shape","CMS_8TeV_hww_VV_of_pthincl_stat_shape","CMS_8TeV_hww_VgS_of_pthincl_stat_shape","CMS_8TeV_hww_Vg_of_pthincl_stat_shape","CMS_8TeV_hww_WHBin0_of_pthincl_stat_shape","CMS_8TeV_hww_WHBin1_of_pthincl_stat_shape","CMS_8TeV_hww_WHBin2_of_pthincl_stat_shape","CMS_8TeV_hww_WHBin3_of_pthincl_stat_shape","CMS_8TeV_hww_WHBin4_of_pthincl_stat_shape","CMS_8TeV_hww_WHBin5_of_pthincl_stat_shape","CMS_8TeV_hww_WJet_FakeRate_e_shape","CMS_8TeV_hww_WJet_FakeRate_m_shape","CMS_8TeV_hww_WJet_of_pthincl_stat_shape","CMS_8TeV_hww_WWBin0_of_pthincl_stat_shape","CMS_8TeV_hww_WWBin1_of_pthincl_stat_shape","CMS_8TeV_hww_WWBin2_of_pthincl_stat_shape","CMS_8TeV_hww_WWBin3_of_pthincl_stat_shape","CMS_8TeV_hww_WWBin4_of_pthincl_stat_shape","CMS_8TeV_hww_WWBin5_of_pthincl_stat_shape","CMS_8TeV_hww_ZHBin0_of_pthincl_stat_shape","CMS_8TeV_hww_ZHBin1_of_pthincl_stat_shape","CMS_8TeV_hww_ZHBin2_of_pthincl_stat_shape","CMS_8TeV_hww_ZHBin3_of_pthincl_stat_shape","CMS_8TeV_hww_ZHBin4_of_pthincl_stat_shape","CMS_8TeV_hww_ZHBin5_of_pthincl_stat_shape","CMS_8TeV_hww_ggHBin0_of_pthincl_stat_shape","CMS_8TeV_hww_ggHBin1_of_pthincl_stat_shape","CMS_8TeV_hww_ggHBin2_of_pthincl_stat_shape","CMS_8TeV_hww_ggHBin3_of_pthincl_stat_shape","CMS_8TeV_hww_ggHBin4_of_pthincl_stat_shape","CMS_8TeV_hww_ggHBin5_of_pthincl_stat_shape","CMS_8TeV_hww_ggWW_of_pthincl_stat_shape","CMS_8TeV_hww_qqHBin0_of_pthincl_stat_shape","CMS_8TeV_hww_qqHBin1_of_pthincl_stat_shape","CMS_8TeV_hww_qqHBin2_of_pthincl_stat_shape","CMS_8TeV_hww_qqHBin3_of_pthincl_stat_shape","CMS_8TeV_hww_qqHBin4_of_pthincl_stat_shape","CMS_8TeV_hww_qqHBin5_of_pthincl_stat_shape","CMS_8TeV_met","CMS_8TeV_p_res_e","CMS_8TeV_p_scale_e","CMS_8TeV_p_scale_j","CMS_8TeV_p_scale_m","CMS_8TeV_p_scale_met","Gen_scale_of_pthincl_8TeV_WWBin0","Gen_scale_of_pthincl_8TeV_WWBin1","Gen_scale_of_pthincl_8TeV_WWBin2","Gen_scale_of_pthincl_8TeV_WWBin3","Gen_scale_of_pthincl_8TeV_WWBin4","Gen_scale_of_pthincl_8TeV_WWBin5","Gen_nlo_of_pthincl_8TeV_WWBin0","Gen_nlo_of_pthincl_8TeV_WWBin1","Gen_nlo_of_pthincl_8TeV_WWBin2","Gen_nlo_of_pthincl_8TeV_WWBin3","Gen_nlo_of_pthincl_8TeV_WWBin4","Gen_nlo_of_pthincl_8TeV_WWBin5"]


#correlated = ["CMS_8TeV_hww_FakeRate","CMS_8TeV_norm_DYTT","CMS_8TeV_norm_Vg","QCDscale_VV","QCDscale_VVV","QCDscale_VgS","QCDscale_WW","QCDscale_WW1in","QCDscale_ggWW","lumi_8TeV","pdf_gg","pdf_qqbar","CMS_8TeV_btagsf","CMS_8TeV_eff_l","CMS_8TeV_met","CMS_8TeV_p_res_e","CMS_8TeV_p_scale_e","CMS_8TeV_p_scale_j","CMS_8TeV_p_scale_m","CMS_8TeV_p_scale_met"]
changing_RM = ["CMS_8TeV_btagsf","CMS_8TeV_eff_l","CMS_8TeV_met","CMS_8TeV_p_res_e","CMS_8TeV_p_scale_e","CMS_8TeV_p_scale_m","CMS_8TeV_p_scale_met", "CMS_8TeV_p_scale_j"]

command = "combine --saveWorkspace -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --saveToys &> logFull.txt"
os.popen(command)
os.popen("mv higgsCombineTest.MultiDimFit.mH120.123456.root full.root")
os.popen("mv mlfit.root mlfit_full.root")
#sys.exit(0)
command = "combine --saveWorkspace -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances="+",".join(changing_RM)+" &> logNotchangingRM.txt"
os.popen(command)
os.popen("mv higgsCombineTest.MultiDimFit.mH120.root stat.root")
os.popen("mv mlfit.root mlfit_notchangingRM.root")

command = "combine --saveWorkspace -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances="+",".join(allsyst)+" &> logStatOnly.txt"
os.popen(command)
os.popen("mv higgsCombineTest.MultiDimFit.mH120.root stat.root")
os.popen("mv mlfit.root mlfit_stat.root")

fullfit =  TFile("full.root")
gSystem.Load("libHiggsAnalysisCombinedLimit")
w = fullfit.Get("w")
w.loadSnapshot("MultiDimFit")
for syst in changing_RM:
  print syst
  print w.var(syst).Print()
  print w.var(syst).getError()
  #error=w.var(syst).getError()
  error=1
  #tofreeze=[a for a in correlated if a != syst]
  #print tofreeze
  #command = "combine --saveWorkspace --expectSignal=1 -t -1 -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances="+",".join(tofreeze)+" &> log"+syst+".txt"
  # combine -t -1 -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances CMS_8TeV_btagsf  --toysFile=higgsCombineTest.MultiDimFit.mH120.123456.root --setPhysicsModelParameters CMS_8TeV_btagsf=1
  command = "combine -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --toysFile full.root --setPhysicsModelParameters "+syst+"="+str(error)+" --freezeNuisances="+syst+" &> log"+syst+"_Up.txt"
  os.popen(command)
  command = "combine -t -1 -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --toysFile full.root --setPhysicsModelParameters "+syst+"="+str(-error)+" --freezeNuisances="+syst+" &> log"+syst+"_Down.txt"
  os.popen(command)
#combine --saveWorkspace --expectSignal=1 -t -1 -M MultiDimFit hww-19.47fb.mH125.of_pthincl_shape_workspace.root --algo=singles --freezeNuisances=CMS_8TeV_hww_FakeRate
