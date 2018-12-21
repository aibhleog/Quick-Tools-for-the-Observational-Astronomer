'''
Calculating the separation between two points given their ra and dec.
Coordinates can be given in hh:mm:ss +dd:mm:ss or hour and decimal degrees,
specified by the degree flag. 

NOTE: both coordinates must be in the same format -- use separation-mix.py
if they are not.

-----------------
TO USE AS SCRIPT:	(notice the syntax)
-----------------
To get output in form of arcminutes:
	type 'python separation.py 00h00m00s +00d00m00s 00h00m00s +00d00m00s arcmin'

The same as above but with decimal hour & degrees:
	type 'python separation.py 00.000 +0.000 00.000 +0.000 arcmin false'

If you want the separation in degrees:
	type 'python separation.py 00h00m00s +00d00m00s 00h00m00s +00d00m00s'
	type 'python separation.py 00.000 +0.000 00.000 +0.000 '' false'
	---> note that you don't need to type anything if in hmsdms units,
		 but you need to add an empty string '' if in decimal units.

'''

from astropy import units as u
from astropy.coordinates import SkyCoord

def sep_coordinates(c1ra,c1dec,c2ra,c2dec,out,notdeg):
# assumes J2000 coordinates
	if notdeg == False:
		c1 = SkyCoord(c1ra,c1dec,unit='degree')
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

	elif notdeg == True:
		c1 = SkyCoord(c1ra,c1dec)
		c2 = SkyCoord(c2ra,c2dec)
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
Coordinates can be given in hh:mm:ss +dd:mm:ss or hour and decimal degrees,
specified by the degree flag. 

NOTE: both coordinates must be in the same format -- use separation-mix.py
if they are not.

-----------------
TO USE AS SCRIPT:	(notice the syntax)
-----------------
To get output in form of arcminutes:
   type 'python separation.py 00h00m00s +00d00m00s 00h00m00s +00d00m00s arcmin'

The same as above but with decimal hour & degrees:
   type 'python separation.py 00.000 +0.000 00.000 +0.000 arcmin false'

If you want the separation in degrees:
   type 'python separation.py 00h00m00s +00d00m00s 00h00m00s +00d00m00s'
   type 'python separation.py 00.000 +0.000 00.000 +0.000 '' false'
   ---> note that you don't need to type anything if in hmsdms units,
        but you need to add an empty string '' if in decimal units.\n''')		

	else:
		try:
			out = sys.argv[5]
		except IndexError:
			out = ''
		try:
			yeshi = sys.argv[6]
			yeshi = yeshi == 'True' or yeshi == 'true'
		except IndexError:
			yeshi = True
		sep_coordinates(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),\
			str(sys.argv[4]),str(out),bool(yeshi))
		
