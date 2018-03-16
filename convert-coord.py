'''
Converting coordinate to specified form.
Default is hmsdms.

-----------------
TO USE AS SCRIPT:	(notice the syntax)
-----------------
To get output in form of decimal units:
	type 'python convert-coord.py 00h00m00s +00d00m00s decimal'

If you want the coordinates in hmsdms:
	type 'python convert-coord.py 00.000 +0.000 '' false'
	---> note that you need to add an empty string ''.

'''

from astropy import units as u
from astropy.coordinates import SkyCoord

def convert(c1,c2,out,notdeg):
# assumes J2000 coordinates
	if notdeg == False:
		c = SkyCoord(c1,c2,unit='degree')
		if out == 'decimal':
			print('Coordinate:',c.to_string('decimal'),end='\n\n')
		elif out == 'dms':
			print('Coordinate:',c.to_string('dms'),end='\n\n')
		else:
			print('Coordinate:',c.to_string('hmsdms'),end='\n\n')

	elif notdeg == True:
		c = SkyCoord(c1,c2)
		if out == 'decimal':
			print('Coordinate:',c.to_string('decimal'),end='\n\n')
		elif out == 'dms':
			print('Coordinate:',c.to_string('dms'),end='\n\n')
		else:
			print('Coordinate:',c.to_string('hmsdms'),end='\n\n')
		

# reads in input when scripting
if __name__ == "__main__":
	import sys
	try:
		out = sys.argv[3]
	except IndexError:
		out = ''
	try:
		yeshi = sys.argv[4]
		yeshi = yeshi == 'True' or yeshi == 'true'
	except IndexError:
		yeshi = True
	convert(str(sys.argv[1]),str(sys.argv[2]),str(out),bool(yeshi))
		
