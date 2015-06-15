#!/usr/bin/env python

from ROOT import *
import sys
from array import *
import copy 
import numpy 

edges = numpy.array([0., 15., 45., 87., 125., 162., 200.])

def makePlot(central, r, name, syst=[]):
  rcopy = copy.deepcopy(r)
  if syst != []:
    for i in range(len(r)):
      rcopy[i] += syst[i]

  h = TH1F(name, name, 6, edges)
  for i in range(1, 7):
    h.SetBinContent(i, rcopy[i-1]*central[i-1])
    #h.SetBinError(i, stat[i-1]*central[i-1])

  return h


gROOT.ProcessLine(".L ~/tdrStyle.C")
setTDRStyle()
gStyle.SetPalette(1)


file=TFile(sys.argv[1])
shapes=TFile(sys.argv[2])
out=TFile("plotsFromFitToys.root", "RECREATE")

tree=file.Get("limit")
rBin0  = array('f', [0])
rBin1  = array('f', [0])
rBin2  = array('f', [0])
rBin3  = array('f', [0])
rBin4  = array('f', [0])
rBin5  = array('f', [0])

tree.SetBranchAddress("rBin0", rBin0)
tree.SetBranchAddress("rBin1", rBin1)
tree.SetBranchAddress("rBin2", rBin2)
tree.SetBranchAddress("rBin3", rBin3)
tree.SetBranchAddress("rBin4", rBin4)
tree.SetBranchAddress("rBin5", rBin5)

profile = TProfile("profileFit", "profileFit", 6, edges)

Hfit = [0., 0., 0., 0., 0., 0.]
samplesFit = ['ggH', "WH", "ZH", 'qqH']
Htrue = [0., 0., 0., 0., 0., 0.]
samplesTrue = ['ggH', "WH", "ZH",'qqH']

for i in range(0, 6):
  for o in samplesFit:
    name = "histo_"+o+"Bin"+str(i)
    h = shapes.Get(name)
    Hfit[i]+=h.Integral()
  for j in samplesTrue:
    name = "histo_"+j+"Bin"+str(i)
    h = shapes.Get(name)
    Htrue[i]+=h.Integral()

rTrue = [1.,1.,1.,1.,1.,1.]    
HTrue = makePlot(Htrue, rTrue, "Htrue")
HTrue.Write()

for itoy in range(2000):
  print "############## TOY", itoy 
  r=[0., 0., 0., 0., 0., 0.]
  tree.GetEntry(itoy)
  for ibin in range(6):
    central = eval("rBin"+str(ibin)+"[0]")
    r[ibin] =  central
  #check for parameters at limit  
  for ir in r:
    print ir
    if abs(ir) == 10.:
      print "skipping this toy because of parameter at limit"
      continue
  HfitThisToy = makePlot(Hfit, r, "HcentralToy"+str(itoy))
  for ibin in range(6):
    profile.Fill(HfitThisToy.GetBinCenter(ibin+1), HfitThisToy.GetBinContent(ibin+1))
  out.cd()
  HfitThisToy.Write()

profile.Write()

a=raw_input("Done")


