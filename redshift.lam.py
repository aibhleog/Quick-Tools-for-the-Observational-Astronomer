'''
This script calculates the wavelength of a line (in Angstroms) given its
restframe wavelength (in Angstroms) and a redshift.
'''

import numpy as np
# returns the redshifted line
def redshift_which(lam0,z):

	if np.log10(lam0) > 2: units_scale = 1e4 # angstroms --> microns
	else: 
		units_scale = 1 # microns
		
	units = 'microns'
	zlam = (lam0/units_scale) * (z + 1)
	
	# if the redshifted value is below 1 micron
	if np.log10(zlam) < 0: 
		zlam *= 1e4 # microns --> angstroms
		units = 'angstroms'
	
	print(f'Redshifted line: {zlam} {units}',end='\n\n')


# reads in input when scripting
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('\nThis script calculates the wavelength of a line (in Angstroms) given\n' 
			'its restframe wavelength (in Angstroms) and a redshift.\n')
		print('Use the follwing notation:   zlam [rest wavelength] [redshift]\n')
	else:
		redshift_which(float(sys.argv[1]),float(sys.argv[2]))
