#
# whsc: cut 2011
#


#
# deve chiamarsi "shape.py"
#

tag='cut_whsc'
lumi=4.922
chans=['ll_whsc']

variable='1'

selection='whsc2011'

#
range = (1,0,2)
#


dataset='Data2011'

energy='7TeV'

mcset='whsc'




# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='counting'


# usato da mkmerged  -> li ricompatto dopo
# rebin=10
rebin=1

# directories
path_latino = '/home/amassiro/Latinos/Shape/tree_42x_skim_wwmin/'

# not to performe datadriven estimation: just comment!
#path_dd     = '/home/amassiro/Latinos/Shape/dd/Cut_whsc_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


#shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]
skipSyst = ['chargeResolution','puW_up','puW_down']







