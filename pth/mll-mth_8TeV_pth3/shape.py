# tag, used to name the intermediate shape files
tag='mll-mth'

# luminosity to normalize to
lumi=19.47
chans=['of_pth3']

# dataset to use: Data2012, Data2012A, Data2012B, SI125
dataset='Data2012'

# set of mc samples: 0j1j, vbf
mcset='0j1j'

# variable, or formula to use: mll, mjj, 2*unboostedMr
# for 2D, use TTree::Draw sytax i.e. x:y
variable='mll:mth' # remember, y:x

# selection to apply when 
selection='shape'

# shape range. can be an
# - hard-coded label
# - a tuple (nx,xmin,xmax)
# - 2d tuple (nx,xmin,xmax,ny,ymin,ymax)
# - 1d array ([x0,..,xn],)
# - 2d array ([x0,..,xn],[y0,...,ym])
range = 'mth-mll-hilospin'
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

# directories
#    path_latino: latino's files
#    path_dd: data driven estimates
#    path_bdt: location of bdt-trees
#path_latino = '/shome/mtakahashi/HWW/Tree/ShapeAna/53x_195fb/tree_skim_wwmin/'
#path_dd = '/shome/mtakahashi/HWW/Data/dd/shape_2012_195fb/'
path_latino = '/raid/lenzip/HWidth/tree_skim_wwmin_21Dec2014/'
#path_latino = '/afs/cern.ch/work/m/maiko/private/Tree/tree/'
#path_dd = '/afs/cern.ch/user/m/maiko/work/private/Data/dd/shape_2012_195fb/'

# other directories
path_shape_raw='raw'
path_shape_merged='merged'
skipSyst = ['JER_down', 'JER_up']
