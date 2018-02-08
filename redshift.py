'''
This script calculates the redshift between two lines given
1. the restframe value (in Angstroms)
2. the redshifted value (also in Angstroms)
'''

import numpy as np
# returns the redshift of the line
def redshift_which(lam0,lam):
	print('Redshift: %s'%((lam/lam0) - 1))
	print()

# reads in input when scripting
if __name__ == "__main__":
	import sys
	redshift_which(float(sys.argv[1]),float(sys.argv[2]))
