#
# WW2jewk: shape OF 2012
#


tag='shape_WW2jewk'
lumi=19.365
chans=['of_2j']

variable='WWewkMVABDTG'

selection='wwewkShape'

#
range = (20,-1.0,1.0)
#range = 'wwewk-range'
#


dataset='Data2012'

mcset='wwewk_of'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='mva'

# signal definition: needed because Higgs is not the signal here
listSignals = ['WWewk']


# usato da mkmerged  -> li ricompatto dopo
# rebin=10
rebin=1

# directories
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j/'
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j_wwewk/'

# not to performe datadriven estimation: just comment!
path_dd     = '/home/amassiro/Latinos/Shape/dd/Shape_WW2jewk_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





