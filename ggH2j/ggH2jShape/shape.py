#
# ggH2j: shape 2012
#


tag='cut_ggH2j'
lumi=19.365
chans=['of_2j']

variable='mll'

selection='ggH2jShape'

#
range = (8,12,150)
#


dataset='Data2012'

mcset='ggH2j_of'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='mll'


# usato da mkmerged  -> li ricompatto dopo
# rebin=10
rebin=1

# directories
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin/'

# not to performe datadriven estimation: just comment!
path_dd     = '/home/amassiro/Latinos/Shape/dd/Shape_ggH2j_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





