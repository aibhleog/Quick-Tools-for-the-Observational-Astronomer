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
		print('Velocity offset of specified redshifts: %s km/s'%(delv))
		print()
	elif high == False:
		# for low-z, don't need to account for relativistic effects
		v1 = 2.998e5 * z1
		if z2 == 0.:
			print('Radial velocity of specified redshift: %s km/s'%(v1))
			print()
		else:
			v2 = 2.998e5 * float(z2)
			print('Velocity offset of specified redshifts: %s km/s'%(v1-v2))
			print()

# the following reads in input -- so that script can be run from terminal
if __name__ == "__main__":
	import sys
	try:
		yeshi = sys.argv[3]
		yeshi = yeshi == 'True' or yeshi == 'true'
	except IndexError:
		yeshi = True
	radial_vel(float(sys.argv[1]),float(sys.argv[2]),bool(yeshi))

