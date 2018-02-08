'''
This script returns the restframe wavelength(s) of any line in the dictionary below.
As many lines can be added as wanted.
'''

import numpy as np
# currently holds the lines I use most frequently in my work
dic = {'ha':6562.8,'ciii':[1906.8,1908.78],'lya':1215.67,\
	'civ':1548.48,'oiii':[4959.,5007.],'cii':2326.0,'mgii':2799.12,\
	'nv':1240.81,'siiv':1397.61,'heii':1640.4,'hei':3889.0,\
	'hbeta':4862.68}

# given a line, returns the wavelength(s)
def which_lines(line):
	print('Restframe: %s angstroms'%(dic[line]))
	print()

# reads in input for scripted version
if __name__ == "__main__":
	import sys
	try:
		which_lines(str(sys.argv[1]))
	except KeyError: # if you reference a line not listed above
		print('That line does not exist in the dataset.')
		print()
