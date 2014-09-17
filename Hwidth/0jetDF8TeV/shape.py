# tag, used to name the intermediate shape files
tag='mll'

# luminosity to normalize to
lumi = 19.47
chans = ['of_0j']

# dataset to use: Data2012, Data2012A, Data2012B, SI125
dataset = 'Data2012'

# set of mc samples: 0j1j, vbf
mcset = 'Hwidth_01j'
sigset = 'Hwidth'
# variable, or formula to use: mll, mjj, 2*unboostedMr
# for 2D, use TTree::Draw sytax i.e. x:y
#variable='mll:mth' # remember, y:x
#variable='mll' # remember, y:x
variable = 'Hwidth'

# selection to apply when
selection='Hwidth'

# shape range. can be an
# - hard-coded label
# - a tuple (nx,xmin,xmax)
# - 2d tuple (nx,xmin,xmax,ny,ymin,ymax)
# - 1d array ([x0,..,xn],)
# - 2d array ([x0,..,xn],[y0,...,ym])
#range = 'mth-mll-hilospin'
#range = '(30,80,280,8,0,200)'
#range = (30,0,300)
range = 'Hwidth-range'

# statmode: defined the style of the statistical systematics:
# - unified: 1 up and 1 down histogram, all bins fluctuating up/down respectively
# - bybin: 2 histograms per bin, where the corresponding bin is fluctuated up/down
statmode = 'unified'

# label used for the plot's x-axis
#xlabel='m_{ll} - m_{tH}'
xlabel='m_{ll}'

# rebin=10
rebin=1



# signal definition: needed because Higgs is not the signal here
listSignals = ['ggH_sbi','ggH_b','ggH_s','qqH_sbi','qqH_b','qqH_s',   'ggH','qqH']



# directories
# path_latino: latino's files
# path_dd: data driven estimates
# path_bdt: location of bdt-trees

#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_all/'
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin/'
# not to performe datadriven estimation: just comment!
#path_dd = '/home/amassiro/Latinos/Shape/dd/Shape_ggH2j_2012_20fb/'
#path_dd = '/home/amassiro/Latinos/Shape/dd/shape_2012_195fb'

# other directories
path_shape_raw='raw'
path_shape_merged='merged'




# remove some nuisances defined in mkShapes.py
skipSyst = ['metScale_down','metScale_up','muonEfficiency_down','muonEfficiency_up','electronEfficiency_down','electronEfficiency_up']

# activate/de-activate some nuisances
shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_8TeV_hww_WJet_FakeRate_e_shape_2j',False),('CMS_8TeV_hww_WJet_FakeRate_m_shape_2j',False)]


