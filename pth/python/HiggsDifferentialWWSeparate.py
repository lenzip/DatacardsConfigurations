from HiggsAnalysis.CombinedLimit.PhysicsModel import *

class DifferentialFiducialWWSeparate( PhysicsModel ):
    ''' Model used to unfold differential distributions '''

    def __init__(self):
        PhysicsModel.__init__(self)
        #self.Range=[0.,10]
        self.Range=[-10.,10.]
        self.nBin=6
        self.debug=1

    def setPhysicsOptions(self,physOptions):
        if self.debug>0:print "Setting PhysicsModel Options"
#        for po in physOptions:
#            if po.startswith("range="):
#                self.Range=po.replace("range=","").split(",")
#                if len(self.Range)!=2:
#                    raise RunTimeError, "Range require minimal and maximal values: range=min,max"
#                if self.debug>0:print "new Range is ", self.Range
#            if po.startswith("nBin="):
#                self.nBin=int(po.replace("nBin=",""))
#                if self.debug>0:print "new n. of bins is ",self.nBin
#            if po.startswith("higgsMassRange="):
#                if self.debug>0: print "setting higgs mass range floating:",po.replace("higgsMassRange=","").split(",")
#                self.mHRange=po.replace("higgsMassRange=","").split(",")
#                #checks
#                if len(self.mHRange) != 2:
#                    raise RuntimeError, "Higgs mass range definition requires two extrema"
#                elif float(self.mHRange[0]) >= float(self.mHRange[1]):
#                    raise RuntimeError, "Extrema for Higgs mass range defined with inverterd order. Second must be larger the first"
#            if po.startswith("mass="):
#                self.mass=float( po.replace('mass=','') )
#            #verbose
#            if po.startswith("verbose"):
#                self.debug = 1

    def doParametersOfInterest(self):
        POIs=""
        if self.debug>0:print "Setting pois"
        for iBin in range(0,self.nBin):
            print "Adding variable rBin", iBin
            self.modelBuilder.doVar("rBin%d[1, %s,%s]" % (iBin, self.Range[0],self.Range[1]))
            self.modelBuilder.doVar("rVBFBin%d[1, %s,%s]" % (iBin, self.Range[0],self.Range[1]))
            self.modelBuilder.out.var("rBin%d" % (iBin)).setConstant(False)
            self.modelBuilder.out.var("rVBFBin%d" % (iBin)).setConstant(False)

            if iBin>=0:
                POIs+="rBin%d,"%iBin
                POIs+="rVBFBin%d,"%iBin
                if self.debug>0:print "Added Bin%d to the POIs"%iBin
        POIs = POIs[:-1] # remove last comma
        self.modelBuilder.doSet("POI",POIs)
    def getYieldScale(self,bin,process):
        if not self.DC.isSignal[process]: return 1
        if "ggH" in process or "WH" in process or "ZH" in process or "ttH" in process or "bbH" in process :
          return re.sub("^(ggH|WH|ZH|ttH|bbH)","r", process)
        else: 
          return re.sub("^(qqH)","rVBF", process)

differentialFiducialWWSeparate=DifferentialFiducialWWSeparate()

