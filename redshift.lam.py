'''
This script calculates the wavelength of a line (in Angstroms) given
1. its restframe wavelength (in Angstroms)
2. a redshift
'''

import numpy as np
# returns the redshifted line
def redshift_which(lam0,z):
	print(r'Redshifted line: %s angstroms'%(lam0 * (z + 1)))
	print()

# reads in input when scripting
if __name__ == "__main__":
	import sys
	redshift_which(float(sys.argv[1]),float(sys.argv[2]))
