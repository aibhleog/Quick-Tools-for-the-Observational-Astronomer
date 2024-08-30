'''

Module that reads in & assigns the filters names.

The user can specify the telescope & instrument (e.g., "Keck/MOSFIRE") and then the bandpass (e.g., "J") and it will pull the correct dictionary.  The way that this is set up, the user can add as many telescopes & instruments that they want -- then they just specify the one that they want in the main script.

-------------------------------------------------------
ALL FILTER CURVES (except Keck/MOSFIRE) can be found at
http://svo2.cab.inta-csic.es/svo/theory/fps3/
-------------------------------------------------------


NOTES:  for now, the order the filters plot is the order they're added into the dictionaries below.

'''

import pandas as pd
path = '/Users/tahutch1/code/useful-code/filters/'

# ------ reading in filter curves ------ #
# ------- & creating dictionaries ------ #

# note: all in angstroms
cols = ['wave','throughput']

# HST/WFC3 NIR photometric bandpasses
f105w = pd.read_csv(path+'HST-WFC3_IR.F105W.dat',names=cols,sep='\s+')
f160w = pd.read_csv(path+'HST-WFC3_IR.F160W.dat',names=cols,sep='\s+')

# building HST/WFC3 dictionary
hst_wfc3 = {'f105w': f105w, 'f160w': f160w}


# Keck/MOSFIRE NIR spectroscopic bandpasses
mos_y = pd.read_csv(path+'mosfire_yband_throughput.txt',names=cols,sep='\s+')
mos_j = pd.read_csv(path+'mosfire_jband_throughput.txt',names=cols,sep='\s+')
mos_h = pd.read_csv(path+'mosfire_hband_throughput.txt',names=cols,sep='\s+')
mos_k = pd.read_csv(path+'mosfire_kband_throughput.txt',names=cols,sep='\s+')
mos_j['wave'] *= 1e4 # because everything else
mos_k['wave'] *= 1e4 # is in Angstroms

# building Keck/MOSFIRE dictionary
keck_mosfire = {'y': mos_y, 'j': mos_j, 'h': mos_h, 'k': mos_k}


# Spitzer/IRAC IR channels
spitzer36 = pd.read_csv(path+'Spitzer_IRAC.I1.dat',names=cols,sep='\s+')
spitzer45 = pd.read_csv(path+'Spitzer_IRAC.I2.dat',names=cols,sep='\s+')
spitzer58 = pd.read_csv(path+'Spitzer_IRAC.I3.dat',names=cols,sep='\s+')
spitzer80 = pd.read_csv(path+'Spitzer_IRAC.I4.dat',names=cols,sep='\s+')

# building Spitzer/IRAC dictionary
spitzer_irac = {'3.6': spitzer36, '4.5': spitzer45, '5.8': spitzer58, '8.0': spitzer80}


# JWST/MIRI, JWST/NIRISS, JWST/NIRCam, JWST/NIRSpec
miri_lrs = pd.DataFrame({'wave':[5e4,12e4],'throughput':[1,1]}) # microns
miri_mrs = pd.DataFrame({'wave':[5.9e4,28.1e4],'throughput':[1,1]}) # microns
niriss_wfss = pd.DataFrame({'wave':[0.8e4,2.2e4],'throughput':[1,1]}) # microns
niriss_soss = pd.DataFrame({'wave':[0.6e4,2.8e4],'throughput':[1,1]}) # microns
nircam_wfss = pd.DataFrame({'wave':[2.4e4,5e4],'throughput':[1,1]}) # microns
nirspec_prism = pd.DataFrame({'wave':[0.6e4,5.3e4],'throughput':[1,1]}) # microns
nirspec_mrs1 = pd.DataFrame({'wave':[0.7e4,1.27e4],'throughput':[1,1]}) # microns
nirspec_mrs2 = pd.DataFrame({'wave':[0.97e4,1.89e4],'throughput':[1,1]}) # microns
nirspec_mrs3 = pd.DataFrame({'wave':[1.66e4,3.17e4],'throughput':[1,1]}) # microns
nirspec_mrs4 = pd.DataFrame({'wave':[2.87e4,5.27e4],'throughput':[1,1]}) # microns

jwst_miri = {'lrs': miri_lrs, 'mrs': miri_mrs}
jwst_niriss = {'wfss': niriss_wfss, 'soss': niriss_soss}
jwst_nircam = {'wfss': nircam_wfss}
jwst_nirspec = {'prism': nirspec_prism, 'f070lp': nirspec_mrs1,
				'f100lp': nirspec_mrs2, 'f170lp': nirspec_mrs3, 'f290lp': nirspec_mrs4}



# final dictionary
# ----------------
filters = {'keck/mosfire': keck_mosfire, 'hst/wfc3': hst_wfc3, 'spitzer/irac': spitzer_irac}

# jwst filters, to be added differently
jwst_filters = {'jwst/nirspec': jwst_nirspec, 'jwst/niriss': jwst_niriss,
				'jwst/nircam': jwst_nircam, 'jwst/miri': jwst_miri}


# ----- function that returns specified ----- #
# ------- telescope/instrument pairing ------ #
# ----------- with chosen bandpass ---------- #

def get_filter(telinst,band,jwst=False):
	# added a jwst tag because those are plotted differently
	if jwst == True: filters_list = jwst_filters
	else: filters_list = filters

	try:
		pairing = filters_list[telinst.lower()]
		try:
			bandpass = pairing[band.lower()]
			return bandpass

		except: print('\nChosen bandpass is not in specified telescope/instrument database.')
	except: print('\nChosen telescope/instrument is not in database.')



# this script returns the redshifted start and end bounds for a given filter
# (should help with making the legend at the top)
def get_filter_bounds(filt,z):
	min_wave, max_wave = filt.wave.min(), filt.wave.max()
	return min_wave, max_wave



# checking all bandpasses to see which ones are within the z range
# returns list of filters in each telescope/instrument pairing that work
def is_it_in_range(z,jwst=False):
	zrange = [800*(1+z), 6680*(1+z)] # in A

	# added a jwst tag because those are plotted differently
	if jwst == True: filters_list = jwst_filters
	else: filters_list = filters

	in_range = {}
	for telinst in filters_list.keys(): # going through telescope/instruments
		in_range[telinst] = [] # will add bands to it
		pairing = filters_list[telinst]
		for band in pairing.keys():
			bounds = get_filter_bounds(pairing[band],z)

			# checks to see if a filter falls within the range
			if zrange[0]  <= bounds[0] <= zrange[1] \
				or zrange[0]  <= bounds[1] <= zrange[1]:
				in_range[telinst].append(band) # adds to list

	# counts up the total number of filters in range
	# (useful for legend)
	total = sum([len(in_range[x]) for x in in_range if isinstance(in_range[x], list)])

	return in_range, total




# ----- filter color info ----- #
# ----------------------------- #

# building HST/WFC3 plotting dictionary
f105w = {'name': 'F105W', 'color':'#1FAF2F', 'edgecolor':'#1FAF2F'}
f160w = {'name': 'F160W', 'color':'#90CA69', 'edgecolor':'#90CA69'}
hst_wfc3 = {'f105w': f105w, 'f160w': f160w}

# building Keck/MOSFIRE plotting dictionary
mos_y = {'name':'MOS Y', 'color':'#1F618D', 'edgecolor':'#1F618D'}
mos_j = {'name':'MOS J', 'color':'C0', 'edgecolor':'C0'}
mos_h = {'name':'MOS H', 'color':'#5DADE2', 'edgecolor':'#5DADE2'}
mos_k = {'name':'MOS K', 'color':'C9', 'edgecolor':'C9'}
keck_mosfire = {'y': mos_y, 'j': mos_j, 'h': mos_h, 'k': mos_k}

# building Spitzer/IRAC plotting dictionary
spitzer36 = {'name':'[3.6]', 'color':'#F4D03F', 'edgecolor':'#F4D03F'}
spitzer45 = {'name':'[4.5]', 'color':'#DA9B27', 'edgecolor':'#DA9B27'}
spitzer58 = {'name':'[5.8]', 'color':'#DA7B27', 'edgecolor':'#DA7B27'}
spitzer80 = {'name':'[8.0]', 'color':'#DA4027', 'edgecolor':'#DA4027'}
spitzer_irac = {'3.6': spitzer36, '4.5': spitzer45, '5.8': spitzer58, '8.0': spitzer80}



# JWST/MIRI, JWST/NIRISS, JWST/NIRCam, JWST/NIRSpec
miri_lrs = {'name': 'LRS', 'color': '#0a0107', 'edgecolor': '#0a0107'}
miri_mrs = {'name': 'MRS', 'color': '#420c32', 'edgecolor': '#420c32'}
niriss_wfss = {'name': 'WFSS', 'color': '#D98A4D', 'edgecolor': '#D98A4D'}
niriss_soss = {'name': 'SOSS', 'color': '#FF5733', 'edgecolor': '#FF5733'}
nircam_wfss = {'name': 'WFSS', 'color': '#900C3F', 'edgecolor': '#900C3F'}
nirspec_prism = {'name': 'PRISM', 'color': '#D3BE58', 'edgecolor': '#D3BE58'}
nirspec_mrs1 = {'name': 'F070LP', 'color': '#FFC300', 'edgecolor': '#FFC300'}
nirspec_mrs2 = {'name': 'F100LP', 'color': '#FFC300', 'edgecolor': '#FFC300'}
nirspec_mrs3 = {'name': 'F170LP', 'color': '#FFC300', 'edgecolor': '#FFC300'}
nirspec_mrs4 = {'name': 'F290LP', 'color': '#FFC300', 'edgecolor': '#FFC300'}

jwst_miri = {'lrs': miri_lrs, 'mrs': miri_mrs}
jwst_niriss = {'wfss': niriss_wfss, 'soss': niriss_soss}
jwst_nircam = {'wfss': nircam_wfss}
jwst_nirspec = {'prism': nirspec_prism, 'f070lp': nirspec_mrs1,
				'f100lp': nirspec_mrs2, 'f170lp': nirspec_mrs3, 'f290lp': nirspec_mrs4}



# final plotting dictionary
# ----------------
plotting = {'keck/mosfire': keck_mosfire, 'hst/wfc3': hst_wfc3, 'spitzer/irac': spitzer_irac}

# jwst filters, to be added differently
jwst_plotting = {'jwst/nirspec': jwst_nirspec, 'jwst/niriss': jwst_niriss,
				 'jwst/nircam': jwst_nircam, 'jwst/miri': jwst_miri}


def get_filter_info(telinst,band,jwst=False):
	# added a jwst tag because those are plotted differently
	if jwst == True: plotting_list = jwst_plotting
	else: plotting_list = plotting

	try:
		pairing = plotting_list[telinst.lower()]
		try:
			bandpass = pairing[band.lower()]
			return bandpass

		except: print('\nChosen bandpass is not in specified telescope/instrument database.')
	except: print('\nChosen telescope/instrument is not in database.')
