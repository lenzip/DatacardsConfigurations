#!/usr/bin/env python

import sys

file = open(sys.argv[1])

for line in file:
  ls = line.split()
  x  = float(ls[0])
  y  = float(ls[1])
  ex = float(ls[2])
  ey = float(ls[3])

  y/=(2*ex)
  ey/=(2*ex)

  print x,y,ex,ey
