lumi=19.47
chans=['of_0j','of_1j', 'sf_0j', 'sf_1j']

# set of mc samples: 0j1j, vbf
mcset='0j1j'
dataset='Data2012'

variable='mll' # remember, y:x
selection='hww'
# TTree::Draw style as in h(nx,xmin,xmax, ny,ymin,ymax)

# shape range. can be an
# - hard-coded label
# - a tuple (nx,xmin,xmax)
# - 2d tuple (nx,xmin,xmax,ny,ymin,ymax)
# - 1d array ([x0,..,xn],)
# - 2d array ([x0,..,xn],[y0,...,ym])
#range=(4,80,280,16,0,200)
#range = ([80., 130., 180., 230., 280.],[0., 12.5, 25., 37.5, 50., 62.5, 75., 87.5, 100., 112.5, 125, 137.5, 150., 162.5, 175., 187.5, 200.])
# range = ([80., 130., 180., 280.],[0., 25., 37.5, 50., 62.5, 75., 87.5, 100., 112.5, 125, 140., 160., 190., 230., 310., 600.])
range = (1,0,200)

tag='mll_hww'
xlabel='m_{ll}'

# rebin=10
rebin=1

# directories
#path_latino = '/shome/mtakahashi/HWW/Tree/ShapeAna/53x_195fb/tree_skim_wwmin/'
#path_dd = '/shome/mtakahashi/HWW/Data/dd/hww_2012_195fb/'
path_latino = '/afs/cern.ch/work/x/xjanssen/public/LatinoTrees/ShapeAnalysis/Tree/tree_skim_wwmin/'
path_dd = '/afs/cern.ch/user/m/maiko/work/private/Data/dd/hww_2012_195fb/'

# other directories
path_shape_raw='raw'
path_shape_merged='merged'
