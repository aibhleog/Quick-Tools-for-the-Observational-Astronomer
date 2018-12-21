'''
This script calculates the wavelength of a line (in Angstroms) given its
observed wavelength (in Angstroms) and a redshift.
---> I don't use this one very often but when I do it's helpful!
'''

import numpy as np
# returns the redshifted line
def de_redshift(lam,z):
	print(r'De-redshifted line: %s angstroms'%(lam / (z + 1)))
	print()

# reads in input when scripting
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':	
		print("\nThis script calculates the wavelength of a line (in Angstroms) given\n" 
			"its observed wavelength (in Angstroms) and a redshift.\n"
			"---> I don't use this one very often but when I do it's helpful!\n")
		print('Use the following notation:   dered [observed wavelength] [redshift]\n')
	else:
		de_redshift(float(sys.argv[1]),float(sys.argv[2]))
