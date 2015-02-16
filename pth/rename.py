#!/usr/bin/env python

import sys,os
from ROOT import *

def printHelp():
  print "usage: rename.py <directory>"

def renameShapes(filename, bin):
  rootfile=TFile(filename, "UPDATE");
  rootfile.cd()
  iter=TIter(rootfile.GetListOfKeys())
  while (iter()):
    if iter.ReadObj().InheritsFrom("TH1"):
      name = iter.ReadObj().GetName();
      if "histo_ggH" in name or "histo_qqH" in name or "histo_WH" in name or "histo_ZH" in name:
        #print "changing name for", name
        newname = name.replace("histo_ggH", "histo_ggHBin"+str(bin))
        newname = newname.replace("histo_qqH", "histo_qqHBin"+str(bin))
        newname = newname.replace("histo_WH", "histo_WHBin"+str(bin))
        newname = newname.replace("histo_ZH", "histo_ZHBin"+str(bin))
        iter.ReadObj().SetNameTitle(newname, newname)
        iter.ReadObj().Write(newname,TObject.kWriteDelete);
        rootfile.Delete(name+";1")
  
  rootfile.Close()



if len(sys.argv) != 2:
  printHelp()
  sys.exit(1)
  
dir=sys.argv[1]
bin=int(dir[-1:])


if not os.path.exists(dir):
  print dir, "does not exist"
  sys.exit(1)

datacard=open(dir+"/datacards/hww-19.47fb.mH125.of_pth"+str(bin)+"_shape.txt")
newcard=""
for line in datacard:
  
  if ("ggH" in line and "qqH" in line and "WH" in line and "ZH" in line):
    line = line.replace("ggH", "ggHBin"+str(bin - 1))
    line = line.replace("qqH", "qqHBin"+str(bin - 1))
    line = line.replace("WH", "WHBin"+str(bin - 1))
    line = line.replace("ZH", "ZHBin"+str(bin - 1))
  newcard+=line  

os.mkdir(dir+"/datacardsRenamed")   
newDatacard = open(dir+"/datacardsRenamed/hww-19.47fb.mH125.of_pth"+str(bin)+"_shape.txt", "w")
newDatacard.write(newcard)
os.popen("cp -Lr "+dir+"/datacards/shapes "+dir+"/datacardsRenamed/")

renameShapes(dir+"/datacardsRenamed/shapes/hww-19.47fb.mH125.of_pth"+str(bin)+"_shape.root", bin - 1)
