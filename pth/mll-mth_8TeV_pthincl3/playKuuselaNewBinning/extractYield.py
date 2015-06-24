#/usr/bin/env python

import sys
import math
import copy
import numpy

import operator

from ROOT import *

def extract(file):
  r = []
  errUp = []
  errDown = []
  for line in file:
    if 'rBin' in line:
      ls = line.split()
      r.append(float(ls[2]))
      errs = ls[3]
      errssplit = errs.split('/')
      errDown.append(float(errssplit[0]))
      errUp.append(float(errssplit[1])) 

  return(r, errUp, errDown)

def makePlot(central, r, stat, name, syst=[]):
  rcopy = copy.deepcopy(r)
  if syst != []:
    for i in range(len(r)):
      rcopy[i] += syst[i]

  edges = numpy.array([0., 15., 45., 87., 125., 162., 200.])
  h = TH1F(name, name, 6, edges)
  for i in range(1, 7):
    h.SetBinContent(i, rcopy[i-1]*central[i-1])
    h.SetBinError(i, stat[i-1]*central[i-1])

  return h



shapes=TFile("hww-19.47fb.mH125.of_pthincl_shape.root")
fitResultNotChangingRM = TFile("mlfit_notchangingRM.root")

fitFull = open('logFull.txt')
fitNotChangingRM = open('logNotchangingRM.txt')
fitStat = open('logStatOnly.txt')

correlated = ["CMS_8TeV_btagsf","CMS_8TeV_eff_l","CMS_8TeV_met","CMS_8TeV_p_res_e","CMS_8TeV_p_scale_e","CMS_8TeV_p_scale_m","CMS_8TeV_p_scale_met","CMS_8TeV_p_scale_j"]

(r, errTotUp, errTotDown) = extract(fitFull)
(rDummy, errNotChangingRMUp, errNotChangingRMDown) = extract(fitNotChangingRM)
(rDummy2, errStatUp, errStatDown) = extract(fitStat)

errStat = []
for i in range(len(errStatUp)):
  errStat.append(max(abs(errStatUp[i]), abs(errStatDown[i])))

errNotChangingRM=[]
for i in range(len(errNotChangingRMUp)):
  errNotChangingRM.append(max(abs(errNotChangingRMUp[i]), abs(errNotChangingRMDown[i])))

H = [0., 0., 0., 0., 0., 0.]
samples = ['ggH', 'qqH', 'WH', 'ZH']
#samples = ['ggH', 'qqH']

for i in range(0, 6):
  for o in samples:
    name = "histo_"+o+"Bin"+str(i)
    h = shapes.Get(name)
    H[i]+=h.Integral()

print "H:  ",H

print "r:          ", r
print "errStatUp:    ", errStatUp
print "errStatDown:    ", errStatDown

rBin0 = RooRealVar("rBin0", "rBin0", -10, 10)
rBin1 = RooRealVar("rBin1", "rBin1", -10, 10)
rBin2 = RooRealVar("rBin2", "rBin2", -10, 10)
rBin3 = RooRealVar("rBin3", "rBin3", -10, 10)
rBin4 = RooRealVar("rBin4", "rBin4", -10, 10)
rBin5 = RooRealVar("rBin5", "rBin5", -10, 10)

rBins = RooArgList(rBin0, rBin1, rBin2, rBin3, rBin4, rBin5)

A = TMatrixD(6,6)
for i in range(6):
  A[i][i] = H[i]

fr = fitResultNotChangingRM.Get("fit_s")
matrix_mu = fr.reducedCovarianceMatrix(rBins)
matrix_mu.Print()
At = A.Transpose(A)

matix_h = (A.Transpose(A)*matrix_mu)
matix_h*=A
matix_h.Print()
#matix_h.SetNameTitle("Hcentral_covariance", "Hcentral_covariance")

outfile = TFile("plotsFromFit.root", "RECREATE")
outfile.cd()
Hcentral   = makePlot(H, r, errNotChangingRM, "HcentralNotChangingRM")
Hcentral.Write()
HcentralStat   = makePlot(H, r, errStat, "HcentralStat")
HcentralStat.Write()
matix_h.Write("Hcentral_covariance")
infile=''
infile+="nuisance & bin1 & bin2 & bin3 & bin4 & bin5 & bin6\n"
#print "nuisance & bin1 & bin2 & bin3 & bin4 & bin5 & bin6"
systs={}
for syst in correlated:
  errSystUp=[]
  errSystDown=[] 
  fitfileUp   = open("log"+syst+"_Up.txt")
  fitfileDown = open("log"+syst+"_Down.txt")
  (rSystUp,   errUpUp, errUpDown) = extract(fitfileUp) 
  (rSystDown, errDownUp, errDownDown) = extract(fitfileDown) 
  row = syst+" & "
  systs[syst] = {} 
  for i in range(len(errTotUp)):
    systs[syst][i]={}
    errSystUp.append(rSystUp[i]-r[i])
    errSystDown.append(rSystDown[i]-r[i])
    systs[syst][i]["Up"] = errSystUp[-1]*100
    systs[syst][i]["Down"] = errSystDown[-1]*100
    row+=""+str("{0:.1f}".format(errSystUp[-1]*100))+"/"+str("{0:.1f}".format(errSystDown[-1]*100))+" (\%) & " 
  infile += row+'\n'  
  print row
  #print "errSystUp:  ", errSystUp
  #print "errSystDown:", errSystDown

  HsystUp    = makePlot(H, r, errStat, "H"+syst+"Up", errSystUp)
  HsystDown  = makePlot(H, r, errStat, "H"+syst+"Down", errSystDown)

  HsystUp.Write()
  HsystDown.Write()

#print operator.itemgetter.__doc__
#sorted_systs = sorted(systs.items(), key=operator.itemgetter(1))
#print "nuisance & bin1 & bin2 & bin3 & bin4 & bin5 & bin6"
#for item in sorted_systs:
#  row = item[0] + " & "
#  for key in item[1].keys():
#    row += str("{0:.1f}".format(item[1][key]["Up"]))+"/"+str("{0:.1f}".format(item[1][key]["Down"])) + " (\%) & "
#  print row  
