#/usr/bin/env python

import sys
import math
import copy
import numpy

import operator

from ROOT import *

def extractUpDownIntegral(graph):
  integralUp=0
  integralDown=0
  xx=Double(0.)
  yy=Double(0.)
  for bin in range(graph.GetN()+1):
    graph.GetPoint(bin, xx, yy)
    errUp = graph.GetErrorYhigh(bin)
    errDown = graph.GetErrorYlow(bin)
    integralUp += (yy+errUp)
    integralDown += (yy-errDown)
  return (integralUp, integralDown)

shapes=TFile("postFit/hww-pthincl-of-error-data.root")

signals=[]
binnedBkgs=[]
keys=[]

shapes.cd("/sig/of_pthincl")
for key in gDirectory.GetListOfKeys():
  if ("histo" in key.GetName() and "model" not in key.GetName()):  keys.append(key.GetName())
keys.sort()  
print keys

intSig=0.
intSigErr=0.
intBkg=0.
intBkgErr=0.
for h in keys :
  gDirectory.cd("/sig/of_pthincl")
  int = gDirectory.Get(h).Integral()
  if "Data" in h:
    intErr = sqrt(int)
  else:
    err_dir = h.replace("histo_","")
    gDirectory.cd(err_dir)
    graph = gDirectory.Get(err_dir+"_errs_all")
    (intUp, intDown) = extractUpDownIntegral(graph)
    intErr = max(abs(intUp-int), abs(intDown-int))

    if ("ggH" in h or "qqH" in h or "WH" in h or "ZH" in h):
      intSig += int
      intSigErr += intErr**2
    else:
      intBkg += int
      intBkgErr += intErr**2

  print "Histogram ", h, " integral = ", int, " error = ", intErr

print "Signal tot = ", intSig, " +/- ", sqrt(intSigErr)
print "Background tot = ", intBkg, " +/- ", sqrt(intBkgErr)

