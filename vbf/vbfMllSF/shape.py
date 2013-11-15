#
# VBF shape   SF    --> actually it is a cut based!
#


#
# deve chiamarsi "shape.py"
#

tag='mll_vbf'
lumi=19.468
chans=['sf_2j']

variable='1'

#selection='vbf-shape'
selection='vbf'
# -> cerca vbf-selection
# da hwwinfo

#
range = (1,0,2)
#


dataset='Data2012'

mcset='vbf_sf'


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
path_latino = '/data2/amassiro/VBF/Summer12/28Jan2013/Shape/tree_skim_wwmin/'
path_dd     = '/data2/amassiro/VBF/Summer12/28Jan2013/Shape/dd/Mll_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


#             name nuisance              nominal    simil-template
MCextrap = [('CMS_8TeV_hww_Top_2j_stat',  'Top',      'CHITOP')]


shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





