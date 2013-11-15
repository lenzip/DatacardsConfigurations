#
# whsc: cut 2012  - mm -
#


tag='cut_whsc'
lumi=19.365
chans=['ll_whsc']

variable='1'

selection='whsc-mm'

#
range = (1,0,2)
#


dataset='Data2012'

mcset='whsc'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='events'


# usato da mkmerged  -> li ricompatto dopo
# rebin=10
rebin=1

# directories
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_whsc/'

# not to performe datadriven estimation: just comment!
#path_dd     = '/home/amassiro/Latinos/Shape/dd/Cut_whsc_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


#shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





