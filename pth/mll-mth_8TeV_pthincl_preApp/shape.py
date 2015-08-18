# signal set used for pTH analysis
sigset='PTH'

# tag, used to name-pth the intermediate shape files
tag='mll-mth'

# luminosity to normalize to
lumi=19.47
#chans=['of_pth1']
chans=['of_pthincl']

# dataset to use: Data2012, Data2012A, Data2012B, SI125
dataset='Data2012'

# set of mc samples: 0j1j, vbf
mcset='0j1j-differential3'

# variable, or formula to use: mll, mjj, 2*unboostedMr
# for 2D, use TTree::Draw sytax i.e. x:y
#variable='mll:mth' # remember, y:x
variable='Pth' # remember, y:x

# selection to apply when 
selection='shape-pth'

# shape range. can be an
# - hard-coded label
# - a tuple (nx,xmin,xmax)
# - 2d tuple (nx,xmin,xmax,ny,ymin,ymax)
# - 1d array ([x0,..,xn],)
# - 2d array ([x0,..,xn],[y0,...,ym])
#range = 'mth-mll-hilospin'
range = 'Pth-range'
#range = '(30,80,280,8,0,200)'

# splitmode, define the selection to split the shape 2 regions according to the splitmode selection
# splitmode='mll'

# statmode: defined the style of the statistical systematics:
#  - unified: 1 up and 1 down histogram, all bins fluctuating up/down respectively
#  - bybin: 2 histograms per bin, where the corresponding bin is fluctuated up/down
statmode = 'unified'

# label used for the plot's x-axis 
xlabel='m_{ll} - m_{tH}'

# rebin=10
rebin=1

floatN = ['WWBin0', 'WWBin1', 'WWBin2', 'WWBin3', 'WWBin4', 'WWBin5',]

# directories
#    path_latino: latino's files
#    path_dd: data driven estimates
#    path_bdt: location of bdt-trees
#path_latino = '/shome/mtakahashi/HWW/Tree/ShapeAna/53x_195fb/tree_skim_wwmin/'
#path_dd = '/shome/mtakahashi/HWW/Data/dd/shape_2012_195fb/'
path_latino = '/data/lenzip/differential/tree_skim_wwmin_pth/'
#path_latino = '/afs/cern.ch/work/m/maiko/private/Tree/tree/'

path_dd = 'dd/'

# name nuisance nominal simil-template
#MCextrap = [('CMS_8TeV_hww_Top0jet_stat', 'Top0jet', 'CHITOP-Top0jet')]
#MCextrap = [('CMS_8TeV_hww_Top0jet_of_pth1_stat_bin1', 'Top0jet', 'CHITOP-Top0jet')]


# other directories
path_shape_raw='raw'
path_shape_merged='merged'
skipSyst = ['JER_down', 'JER_up']
#            'electronResolution'      ,
#                  'electronScale_down'      ,
#                  'electronScale_up'        ,
#                  'jetEnergyScale_down'     ,
#                  'jetEnergyScale_up'       ,
#                  'leptonEfficiency_down'   ,
#                  'leptonEfficiency_up'     ,
#                  'muonEfficiency_down'     ,
#                  'muonEfficiency_up'       ,
#                  'electronEfficiency_down' ,
#                  'electronEfficiency_up'   ,
#                  'puW_up'                  ,
#                  'puW_down'                ,
#                  'metResolution'           ,
#                  'metScale_down'           ,
#                  'metScale_up'             ,
#                  'muonScale_down'          ,
#                  'muonScale_up'            ,
#                  'chargeResolution'        ,
#                  'JER_down'                ,
#                  'JER_up'                  ,
#                  'JER_down'                ,
#                  'btagsf_up'               ,
#                  'btagsf_down'             ,] 
