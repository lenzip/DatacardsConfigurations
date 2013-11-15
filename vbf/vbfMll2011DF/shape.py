#
# VBF 2011 shape mll  DF
#


tag='vbf_cutBased'

lumi=4.922
chans=['of_2j']

mcset='vbf_of'
dataset='Data2011'

energy='7TeV'


variable='mll'

selection='vbf2011-shape'
# -> cerca vbf-shape-selection
# da hwwinfo

#
#range='vbfMll-range'
range='vbfMll-2011-range'
#

xlabel='m(ll) [GeV]'

statmode='unified'

# rebin=10
rebin=1


# directories
path_latino = '/data2/amassiro/VBF/Summer12/28Jan2013/Shape/tree_42x_skim_wwmin/'
path_dd     = '/data2/amassiro/VBF/Summer12/28Jan2013/Shape/dd/Cut_2011_5fb/'
# //---->>> there are no changes in the datadriven estimation between shape and cut based! -> extrapolation performed by the shapeFramework
#           then top is ok, and DYee/mm appears only in cut based SF, and it is the same!!!


# other directories
path_shape_raw='raw'
path_shape_merged='merged'



#             name nuisance              nominal    simil-template
MCextrap = [('CMS_7TeV_hww_Top_2j_stat',  'Top',      'CHITOP')]


#shapeFlags = [('CMS_7TeV_ch_res',False)]
#nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]
shapeFlags = [('CMS_7TeV_ch_res',False),('CMS_8TeV_hww_WJet_FakeRate_m_shape_2j',False),('CMS_8TeV_hww_WJet_FakeRate_e_shape_2j',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]

skipSyst = ['chargeResolution','puW_up','puW_down']



