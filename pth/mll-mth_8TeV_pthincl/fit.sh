text2workspace.py -m 125.6 hww-19.47fb.mH125.of_pthincl_shape.txt -P DatacardsConfigurations.pth.HiggsDifferentialWW:differentialFiducialWW -o model.root
combine -M MultiDimFit -m 125.6 -t -1 --expectSignal=1 model.root --algo=singles
