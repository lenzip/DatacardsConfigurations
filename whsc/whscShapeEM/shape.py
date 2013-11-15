#
# whsc: shape 2012  - em -
#


tag='cut_whsc'
lumi=19.365
chans=['ll_whsc']

variable='mindphimlijj'
#'(jetpt2>20)*min(sqrt((2*pt1*cosh(eta1)+jetpt1*cosh(jeteta1)+jetpt2*cosh(jeteta2))*(2*pt1*cosh(eta1)+jetpt1*cosh(jeteta1)+jetpt2*cosh(jeteta2))-((2*pt1*sin(phi1)+jetpt1*sin(jetphi1)+jetpt2*sin(jetphi2))*(2*pt1*sin(phi1)+jetpt1*sin(jetphi1)+jetpt2*sin(jetphi2))+(2*pt1*cos(phi1)+jetpt1*cos(jetphi1)+jetpt2*cos(jetphi2))*(2*pt1*cos(phi1)+jetpt1*cos(jetphi1)+jetpt2*cos(jetphi2))+(2*pt1*(1-exp(-2*eta1))/(2.*exp(-eta1))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1))+jetpt2*(1-exp(-2*jeteta2))/(2.*exp(-jeteta2)))*(2*pt1*(1-exp(-2*eta1))/(2.*exp(-eta1))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1))+jetpt2*(1-exp(-2*jeteta2))/(2.*exp(-jeteta2))))),sqrt((2*pt2*cosh(eta2)+jetpt1*cosh(jeteta1)+jetpt2*cosh(jeteta2))*(2*pt2*cosh(eta2)+jetpt1*cosh(jeteta1)+jetpt2*cosh(jeteta2))-((2*pt2*sin(phi2)+jetpt1*sin(jetphi1)+jetpt2*sin(jetphi2))*(2*pt2*sin(phi2)+jetpt1*sin(jetphi1)+jetpt2*sin(jetphi2))+(2*pt2*cos(phi2)+jetpt1*cos(jetphi1)+jetpt2*cos(jetphi2))*(2*pt2*cos(phi2)+jetpt1*cos(jetphi1)+jetpt2*cos(jetphi2))+(2*pt2*(1-exp(-2*eta2))/(2.*exp(-eta2))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1))+jetpt2*(1-exp(-2*jeteta2))/(2.*exp(-jeteta2)))*(2*pt2*(1-exp(-2*eta2))/(2.*exp(-eta2))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1))+jetpt2*(1-exp(-2*jeteta2))/(2.*exp(-jeteta2))))))+(jetpt2<=20)*min(sqrt((2*pt1*cosh(eta1)+jetpt1*cosh(jeteta1))*(2*pt1*cosh(eta1)+jetpt1*cosh(jeteta1))-((2*pt1*sin(phi1)+jetpt1*sin(jetphi1))*(2*pt1*sin(phi1)+jetpt1*sin(jetphi1))+(2*pt1*cos(phi1)+jetpt1*cos(jetphi1))*(2*pt1*cos(phi1)+jetpt1*cos(jetphi1))+(2*pt1*(1-exp(-2*eta1))/(2.*exp(-eta1))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1)))*(2*pt1*(1-exp(-2*eta1))/(2.*exp(-eta1))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1))))),sqrt((2*pt2*cosh(eta2)+jetpt1*cosh(jeteta1))*(2*pt2*cosh(eta2)+jetpt1*cosh(jeteta1))-((2*pt2*sin(phi2)+jetpt1*sin(jetphi1))*(2*pt2*sin(phi2)+jetpt1*sin(jetphi1))+(2*pt2*cos(phi2)+jetpt1*cos(jetphi1))*(2*pt2*cos(phi2)+jetpt1*cos(jetphi1))+(2*pt2*(1-exp(-2*eta2))/(2.*exp(-eta2))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1)))*(2*pt2*(1-exp(-2*eta2))/(2.*exp(-eta2))+jetpt1*(1-exp(-2*jeteta1))/(2.*exp(-jeteta1))))))'

selection='whscShape-em'

#
range = 'whsc-range'
#


dataset='Data2012'

mcset='whsc'


# errore statistico

# in mkmerged
# unified  -> shift globale
# bybin ---> bin bin bin

statmode='unified'

xlabel='min2ljj'


# usato da mkmerged  -> li ricompatto dopo
# rebin=10
rebin=1

# directories
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_2j/'
#path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin/'
path_latino = '/home/amassiro/Latinos/Shape/tree_skim_wwmin_whsc/'

# not to performe datadriven estimation: just comment!
#path_dd     = '/home/amassiro/Latinos/Shape/dd/Cut_whsc_2012_20fb/'



# output other directories
path_shape_raw='raw'
path_shape_merged='merged'


#shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_hww_FakeRate_e',False),('CMS_hww_FakeRate_m',False)]





