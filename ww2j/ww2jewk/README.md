WW+2jets electroweak production
=======================

To prepare:

    ls -d ../../../WW2jewk?FcutTCHE??/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d ../../../WW2jewk?FshapeTCHE??/ | tr "." " " | tr "/" " " | awk '{print "mkdir "$2}'
    ls -d */   | awk '{print "cp ../../../"$1"/shape.py ./"$1"/; cp ../../../"$1"/doIt.sh ./"$1"/"}'


and the datadriven estimation:

    cp ../../../dd/Cut_WW_2012_20fb/*.txt   dd/

    /home/amassiro/Latinos/Shape/dd/Cut_WW2jewk_2012_20fb/
    /home/amassiro/Latinos/Shape/dd/Shape_WW2jewk_2012_20fb


