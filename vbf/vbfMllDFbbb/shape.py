#
# VBF shape   DF    Mll ---> bin-by-bin !
#


#
# deve chiamarsi "shape.py"
#

tag='mll_vbf'
lumi=19.468
chans=['of_2j']

variable='mll'

selection='vbf-shape'
# -> cerca vbf-shape-selection
# da hwwinfo

#
range='vbfMll-range'
#


dataset='Data2012'

mcset='vbf_of'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='bybin'

xlabel='m(ll) [GeV]'


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




