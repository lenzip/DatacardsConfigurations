from __future__ import division
from ROOT import *
from math import *


file_sig = TFile("/afs/cern.ch/user/l/lenzip/work/ww/differential/CMSSW_6_1_1/src/DatacardsConfigurations/pth/mll-mth_8TeV_pthincl3Btag/merged/hww-19.47fb.mH125.of_pthincl_shape.root")
file_ctrl = TFile("/afs/cern.ch/user/l/lenzip/work/ww/differential/CMSSW_6_1_1/src/DatacardsConfigurations/pth/mll-mth_8TeV_pthincl3Ctrl/merged/hww-19.47fb.mH125.of_pthincl_shape.root")

snames = [hs.GetName() for hs in file_sig.GetListOfKeys()]
cnames = [hc.GetName() for hc in file_ctrl.GetListOfKeys()]

hsig = {}
for n in snames :
  if not "histo" in n : continue
  hsig[n] = file_sig.Get(n).Integral() 

hctrl = {}
for n in cnames :
  if not "histo" in n : continue
  hctrl[n] = file_ctrl.Get(n).Integral()


fBin0 = open("Topge1jetBin0Card_of_pthincl.txt","w")
fBin1 = open("Topge1jetBin1Card_of_pthincl.txt","w")
fBin2 = open("Topge1jetBin2Card_of_pthincl.txt","w")
fBin3 = open("Topge1jetBin3Card_of_pthincl.txt","w")
fBin4 = open("Topge1jetBin4Card_of_pthincl.txt","w")
fBin5 = open("Topge1jetBin5Card_of_pthincl.txt","w")

fList = [fBin0,fBin1,fBin2,fBin3,fBin4,fBin5]

mass = 125

for pthbin in range(0,6) :
  nsig = hsig["histo_Topge1jetBin"+str(pthbin)]
  nctrl = hctrl["histo_Topge1jetCtrlBin"+str(pthbin)]

  nsigup = hsig["histo_Topge1jetBin"+str(pthbin)+"_CMS_8TeV_btagsfUp"]
  nsigdown = hsig["histo_Topge1jetBin"+str(pthbin)+"_CMS_8TeV_btagsfDown"]
  nctrlup = hctrl["histo_Topge1jetCtrlBin"+str(pthbin)+"_CMS_8TeV_btagsfUp"]
  nctrldown = hctrl["histo_Topge1jetCtrlBin"+str(pthbin)+"_CMS_8TeV_btagsfDown"]

#  errsig = max(abs(nsigup - nsig), abs(nsig - nsigdown))
#  errctrl = max(abs(nctrlup - nctrl), abs(nctrl - nctrldown))

  alpha = nsig/nctrl
  alphaup = nsigup/nctrlup
  alphadown = nsigdown/nctrldown

  alpha_err = max(abs(alpha-alphaup),abs(alpha-alphadown))

#  alpha.append(nsig/nctrl)
#  alphaup.append(nsigup/nctrlup)
#  alpha_err.append( sqrt( (errsig/nsig)**2 + (errctrl/nctrl)**2 )*nsig/nctrl )
#  alpha_err.append( ( (errsig/nsig) + (errctrl/nctrl) )*nsig/nctrl )


  firstbin = 9*14*pthbin
  lastbin = 9*14*(pthbin+1)

  ndata = file_ctrl.Get("histo_Data").Integral(firstbin,lastbin)

#  ndata.append(file_ctrl.Get("histo_Data").Integral(firstbin,lastbin))

  fList[pthbin].write("%d\t%d\t%f\t%f" % (mass,int(ndata),alpha,alpha_err))

