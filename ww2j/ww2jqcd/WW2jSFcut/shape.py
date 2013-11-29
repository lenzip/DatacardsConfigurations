#
# WW2j: cut SF 2012
#


tag='cut_WW2jewk'
lumi=19.365
chans=['sf_2j']

variable='1'

selection='ww2jCut'

#
range = (1,0,2)
#


dataset='Data2012'

mcset='wwewk_sf'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='events'

# signal definition: needed because Higgs is not the signal here
listSignals = ['WW']

# usato da mkmerged  -> li ricompatto dopo
# rebin=10
rebin=1

# directories
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j/'
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j_wwewk/'

# not to performe datadriven estimation: just comment!
path_dd     = '/home/amassiro/Latinos/Shape/dd/Cut_WW2j_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





