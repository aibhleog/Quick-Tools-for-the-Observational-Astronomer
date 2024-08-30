'''
This script calculates the wavelength of a line (in Angstroms) given its
observed wavelength (in Angstroms) and a redshift.
---> I don't use this one very often but when I do it's helpful!
'''

import numpy as np
# returns the redshifted line
def de_redshift(lam,z):
	if np.log10(lam) > 2: units_scale = 1 # angstroms
	else: units_scale = 1e4 # microns --> angstroms
	
	dered = (lam*units_scale) / (z + 1)
	if np.log10(dered) >= 4: 
		dered /= 1e4 # angstroms --> microns
		units = 'microns'
	else: units = 'angstroms'
	
	print(f'De-redshifted line: {dered} {units}')
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
