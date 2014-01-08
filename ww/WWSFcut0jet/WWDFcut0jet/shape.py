#
# WW 0 jet cut OF 2012
#


tag='cut_WW2jewk'
lumi=19.365
chans=['of_2j']

variable='1'

selection='wwewkCut21'

#
range = (1,0,2)
#



dataset='Data2012'

mcset='wwewk_of'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='events'


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
path_dd     = '/home/amassiro/Latinos/Shape/dd/Cut_WW2jewk_2012_20fb_tche21/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'



# remove some nuisances defined in mkShapes.py
skipSyst = ['metScale_down','metScale_up','muonEfficiency_down','muonEfficiency_up','electronEfficiency_down','electronEfficiency_up']

# activate/de-activate some nuisances
shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





