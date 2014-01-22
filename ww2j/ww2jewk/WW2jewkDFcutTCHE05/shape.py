#
# WW2jewk: cut OF 2012 tche 0.5
#


tag='cut_WW2jewk'
lumi=19.365
chans=['of_2jtche05']

variable='1'

selection='wwewkCut05'

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
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j_wwewk/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j_wwewk_newSmearing/'

# not to performe datadriven estimation: just comment!
path_dd     = '/home/amassiro/Latinos/Shape/dd/Cut_WW2jewk_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'



# remove some nuisances defined in mkShapes.py
skipSyst = ['metScale_down','metScale_up','muonEfficiency_down','muonEfficiency_up','electronEfficiency_down','electronEfficiency_up']

# activate/de-activate some nuisances
shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_8TeV_hww_WJet_FakeRate_e_shape_2j',False),('CMS_8TeV_hww_WJet_FakeRate_m_shape_2j',False)]





