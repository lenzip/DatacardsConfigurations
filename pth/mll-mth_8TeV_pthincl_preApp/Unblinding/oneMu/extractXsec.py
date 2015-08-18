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
    if 'r :' in line:
      ls = line.split()
      r.append(float(ls[2]))
      errs = ls[3]
      errssplit = errs.split('/')
      errDown.append(float(errssplit[0]))
      errUp.append(float(errssplit[1])) 

  return(r, errUp, errDown)

def makeXsec(N, r, errTotUp, errTotDown, errStat, fid=1):
  lumi=19.467
  r = float(r[0])
  errTotUp = float(errTotUp[0]) 
  errTotDown = float(errTotDown[0])
  errStat = float(errStat[0])
  totfake=0
  if fid:
    eff=0.361935
    fakesFile = TFile("fakes_reco.root")
    hfake = fakesFile.Get("hfake")
    for i in range(1, 7):
      totfake+=hfake.GetBinContent(i)
  else: 
    totfake=0
    eff=0.03960

  N_acc = r*(N - totfake)
  DN_accUp = errTotUp*N_acc
  DN_accDown = errTotDown*N_acc
  DN_accStat = errStat*N_acc
  xsec = N_acc/lumi/eff
  DxsecUp = (DN_accUp/N_acc)*xsec
  DxsecDown = (DN_accDown/N_acc)*xsec
  DxsecStat = (DN_accStat/N_acc)*xsec
  DxsecSystUp = sqrt( DxsecUp**2 - DxsecStat**2 )
  DxsecSystDown = sqrt( DxsecDown**2 - DxsecStat**2 )

  return (xsec, DxsecStat, DxsecSystUp, DxsecSystDown)


shapes=TFile("hww-19.47fb.mH125.of_pthincl_shape.root")

fitFull = open('logFull.txt')
fitStat = open('logStatOnly.txt')

(r, errTotUp, errTotDown) = extract(fitFull)
(rDummy, errStatUp, errStatDown) = extract(fitStat)

errStat = []
for i in range(len(errStatUp)):
  errStat.append(max(abs(errStatUp[i]), abs(errStatDown[i])))

H = [0., 0., 0., 0., 0., 0.]
Htot = 0
samples = ['ggH', 'qqH', 'WH', 'ZH']

for i in range(0, 6):
  for o in samples:
    name = "histo_"+o+"Bin"+str(i)
    h = shapes.Get(name)
    H[i]+=h.Integral()
  Htot+=H[i]    

print "Htot:  ", Htot

print "r:        ", r
print "errTotUp:      ", errTotUp
print "errTotDown:      ", errTotDown
print "errStat:      ", errStat

(xsec, xsec_errStat, xsec_errSystUp, xsec_errSystDown) = makeXsec(Htot, r, errTotUp, errTotDown, errStat)
print "### FIDUCIAL: ", (xsec, xsec_errStat, xsec_errSystUp, xsec_errSystDown)
(xsec, xsec_errStat, xsec_errSystUp, xsec_errSystDown) = makeXsec(Htot, r, errTotUp, errTotDown, errStat, 0)
print "### 4PI: ", (xsec, xsec_errStat, xsec_errSystUp, xsec_errSystDown)

