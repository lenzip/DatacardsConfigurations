ggH 0 and 1 jet bin
=======================

default:

    cut_hww_7TeV
    cut_hww_8TeV
    mll-mth_7TeV
    mll-mth_8TeV

to prepare:

    leave only shape.py
    find * -maxdepth 3  -name 'shape.py' -prune -o -exec rm -f '{}' ';'
    rm -r */*/*/


for datadriven:

    cd ggH01j
    ls | awk '{print "mkdir "$1"/dd/"}'

    ls /afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Data/dd/
    hww_2011_494fb  hww_2012_195fb  mll_2012_195fb  shape_2011_494fb  shape_2012_195fb  shapehcp_2012_195fb

    cp -r /afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Data/dd/hww_2011_494fb     cut_hww_7TeV/dd/
    cp -r /afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Data/dd/hww_2012_195fb     cut_hww_8TeV/dd/
    cp -r /afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Data/dd/shape_2012_195fb   mll-mth_8TeV/dd/
    cp -r /afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Data/dd/shape_2011_494fb   mll-mth_7TeV/dd/

    cut_hww_7and8TeV  cut_hww_7TeV  cut_hww_8TeV  mll-mth_7and8TeV  mll-mth_7TeV  mll-mth_8TeV 