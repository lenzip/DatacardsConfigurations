#
# VH shape   DF    Mll   ---> bbb active!
#



#
# deve chiamarsi "shape.py"
#

tag='mll_vh'
#lumi=19.468
lumi=19.365
chans=['of_vh2j']

variable='mll'

selection='vh-shape'
#  -> cerca vh-shape-selection
# da hwwinfo


range='vhMll-range'
#range='vhMll-coarse-range'



# dataset to use: Data2012, Data2012A, Data2012B, SI125
dataset='Data2012'
#dataset='SI125'
#simask='SM'  --> serve ad iniettare un subset dei segnali

mcset='vh_of'

energy = '8TeV'

# signals samples to use
sigset='SM'
# mass=125


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

# statmode='unified'
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



#shapeFlags = [('CMS_8TeV_ch_res',False), ('CMS_8TeV_*_stat_shape_bin4',False), ('CMS_8TeV_*_stat_shape_bin5',False), ('CMS_8TeV_*_stat_shape_bin6',False), ('CMS_8TeV_*_stat_shape_bin7',False), ('CMS_8TeV_*_stat_shape_bin8',False), ('CMS_8TeV_*_stat_shape_bin9',False), ('CMS_8TeV_hww_VVV_of_vh2j_stat_shape_bin*',False), ('CMS_8TeV_hww_VV_of_vh2j_stat_shape_bin*',False)]


#shapeFlags = [('CMS_8TeV_ch_res',False), ('CMS_8TeV_*_stat_shape_bin4',False), ('CMS_8TeV_*_stat_shape_bin5',False), ('CMS_8TeV_*_stat_shape_bin6',False), ('CMS_8TeV_*_stat_shape_bin7',False), ('CMS_8TeV_*_stat_shape_bin8',False), ('CMS_8TeV_*_stat_shape_bin9',False)]

shapeFlags = [('CMS_8TeV_ch_res',False)]

nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]









