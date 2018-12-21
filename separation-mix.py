'''
Calculating the separation between two points given their ra and dec.
Used when one coordinate given in hh:mm:ss +dd:mm:ss and the other in
hour and decimal degrees.

-----------------------------------------
Put hh:mm:ss +dd:mm:ss coordinates first.
-----------------------------------------

-----------------
TO USE AS SCRIPT:	(notice the syntax)
-----------------
To get output in form of arcminutes:
	type 'python separation-mix.py 00h00m00s +00d00m00s 00.000 +0.000 arcmin'

If you want the separation in degrees:
	type 'python separation-mix.py 00h00m00s +00d00m00s 00.000 +0.000'
	---> note that you don't need to add any output unit specifier for degrees.

'''

import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

def sep_mix_coordinates(c1ra,c1dec,c2ra,c2dec,out):
# assumes J2000 coordinates
	c1 = SkyCoord(c1ra,c1dec)
	c2 = SkyCoord(c2ra,c2dec,unit='degree')
	sep = c1.separation(c2)
	if out == 'arcmin':
		print('Separation:',sep.arcminute,'[arcmin]',end='\n\n')
	elif out == 'arcsec':
		print('Separation:',sep.arcsecond,'[arcsec]',end='\n\n')
	elif out == 'hour':
		print('Separation:',sep.hour,'[hour]',end='\n\n')
	elif out == 'radian':
		print('Separation:',sep.radian,'[radian]',end='\n\n')
	else:
		print('Separation:',sep,'[deg]',end='\n\n')

# reads in input when scripting
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('''
Calculating the separation between two points given their ra and dec.
Used when one coordinate given in hh:mm:ss +dd:mm:ss and the other in
hour and decimal degrees.

-----------------------------------------
Put hh:mm:ss +dd:mm:ss coordinates first.
-----------------------------------------

-----------------
TO USE AS SCRIPT:	(notice the syntax)
-----------------
To get output in form of arcminutes:
   type 'python separation-mix.py 00h00m00s +00d00m00s 00.000 +0.000 arcmin'

If you want the separation in degrees:
   type 'python separation-mix.py 00h00m00s +00d00m00s 00.000 +0.000'
   ---> note that you don't need to add any output unit specifier for degrees.\n''')
	else:
		try:
			out = sys.argv[5]
		except IndexError:
			out = ''
		sep_mix_coordinates(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),\
			str(sys.argv[4]),str(out))
		
