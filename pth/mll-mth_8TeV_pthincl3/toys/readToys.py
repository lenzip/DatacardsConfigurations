#!/usr/bin/env python

from ROOT import *
import sys
from array import *
import copy 
import numpy 

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

colors=[2,4,6,8,5,1]
hcentrals = []
hpulls = []

ggH = [0., 0., 0., 0., 0., 0.]

for i in range(0, 6):
  namegg="histo_ggHBin"+str(i)
  h = shapes.Get(namegg)
  ggH[i] = h.Integral()

leg = TLegend(0.8, 0.7, 1, 1)
leg.SetFillStyle(4000)
leg.SetFillColor(0)
for i in range(6):
  hc = TH1F("rBin"+ str(i), "rBin"+ str(i), 30, -4, 5)
  hc.SetMarkerColor(colors[i])
  hc.SetLineColor(colors[i])
  hc.SetLineWidth(2)
  leg.AddEntry(hc, "#mu_"+str(i), "l")
  hp = TH1F("PullrBin"+ str(i), "Pull rBin"+ str(i), 50, -5, 5)
  hp.SetMarkerColor(colors[i])
  hp.SetLineColor(colors[i])
  hp.SetLineWidth(2)

  hcentrals.append(hc)
  hpulls.append(hp)

for itoy in range(1900):
  print "############## TOY", itoy 
  r=[0., 0., 0., 0., 0., 0.]
  errStat=[0., 0., 0., 0., 0., 0.]
  for ibin in range(6):
    icentral = itoy*14+(ibin*2)
    idown    = icentral + 1
    iup      = icentral + 2
    tree.GetEntry(icentral)
    central = eval("rBin"+str(ibin)+"[0]")
    tree.GetEntry(idown)
    down    = eval("rBin"+str(ibin)+"[0]")
    tree.GetEntry(iup)
    up      = eval("rBin"+str(ibin)+"[0]")
    errDown = down-central
    errUp   = up - central 
    print "rBin"+str(ibin),"=", central," +/- ", errUp, errDown 
    hcentrals[ibin].Fill(central)
    if abs(errUp) > 0. and abs(errDown) > 0.:
      pull = (central - 1.)/abs(errUp) if central - 1. > 0 else (central - 1.)/abs(errDown)
      hpulls[ibin].Fill(pull)  
    r[ibin] =  central
    errStat[ibin] = max(abs(errUp), abs(errDown))
  ggHthisToy = makePlot(ggH, r, errStat, "ggHcentralToy"+str(itoy))
  out.cd()
  ggHthisToy.Write()


cFit = TCanvas()
cFit.cd()

for ibin in range(6):
  if ibin == 0:
    hcentrals[ibin].Draw()
  else:
    hcentrals[ibin].Draw("sames")
leg.Draw("sames")

cFit.Write()

cPull = TCanvas()
cPull.cd()

for ibin in range(6):
  if (ibin==0):
    hpulls[ibin].Fit("gaus", "", "")
  else:  
    hpulls[ibin].Fit("gaus", "", "sames")
  hpulls[ibin].FindObject("gaus").SetLineColor(hpulls[ibin].GetLineColor() )#SetNameTitle("Fit"+str(ibin), "Fit"+str(ibin))
  hpulls[ibin].FindObject("gaus").SetLineWidth(2)
    
cPull.Write()

  #if ibin == 0:
  #  hpulls[ibin].Draw()
  #else:
  #  hpulls[ibin].Draw("sames")
leg.Draw("sames")




a=raw_input("Done")


