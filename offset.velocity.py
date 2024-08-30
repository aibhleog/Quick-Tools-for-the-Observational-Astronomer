'''
This code calculates the velocity offset or radial velocity of an object at either high
or low redshift, specified by the redshift flag
'''

import numpy as np
# this function will default to high redshift unless otherwise specified
# speed of light in units of km/s
def radial_vel(z1,z2,high):
	# will return the radial velocity of z1 unless z2 specified
	# then it will return the difference
	if high == True:
		# for high-z, currently only returns the difference
		delv = 2.998e5 * (z2 - z1) / (1 + z1)
		print(f'Velocity offset of specified redshifts: {delv} km/s',end='\n\n')
	elif high == False:
	
		# for low-z, don't need to account for relativistic effects
		v1 = 2.998e5 * z1
		if z2 == 0.:
			print(f'Radial velocity of specified redshift: {v1} km/s',end='\n\n')

		else:
			v2 = 2.998e5 * float(z2)
			print(f'Velocity offset of specified redshifts: {v1-v2} km/s',end='\n\n')


# the following reads in input -- so that script can be run from terminal
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('\nThis code calculates the velocity offset or radial velocity of an\n'
			'object at either high or low redshift, specified by the redshift flag\n')
		print('Use the following notation:   offset [redshift 1] [redshift 2]\n')
	else:
		try:
			yeshi = sys.argv[3]
			yeshi = yeshi == 'True' or yeshi == 'true'
		except IndexError:
			yeshi = True
		try:
			z2 = sys.argv[2]
		except IndexError:
			z2 = 0.
			yeshi = False
		radial_vel(float(sys.argv[1]),float(z2),bool(yeshi))

