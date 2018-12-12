'''
This script calculates the wavelength of a line (in Angstroms) given its
observed wavelength (in Angstroms) and a redshift.
'''

import numpy as np
# returns the redshifted line
def de_redshift(lam,z):
	print(r'De-redshifted line: %s angstroms'%(lam / (z + 1)))
	print()

# reads in input when scripting
if __name__ == "__main__":
	import sys
	de_redshift(float(sys.argv[1]),float(sys.argv[2]))
