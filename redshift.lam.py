'''
This script calculates the wavelength of a line (in Angstroms) given its
restframe wavelength (in Angstroms) and a redshift.
'''

import numpy as np
# returns the redshifted line
def redshift_which(lam0,z):
	print(r'Redshifted line: %s angstroms'%(lam0 * (z + 1)))
	print()

# reads in input when scripting
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('\nThis script calculates the wavelength of a line (in Angstroms) given\n' 
			'its restframe wavelength (in Angstroms) and a redshift.\n')
		print('Use the follwing notation:   zlam [rest wavelength] [redshift]\n')
	else:
		redshift_which(float(sys.argv[1]),float(sys.argv[2]))
