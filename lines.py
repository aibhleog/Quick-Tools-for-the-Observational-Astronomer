'''
This script returns the restframe wavelength(s) of any line in the dictionary below.
As many lines can be added as wanted.
'''

import numpy as np
# currently holds the lines I use most frequently in my work
dic = {'ha':6562.8,'c.iii]':[1906.8,1908.73],'lya':1215.67,\
	'c.iv':[1548.19,1550.76],'o.ii':[3726.1,3728.8],'o.iii':[4959.,5007.],\
	'si.iii]':[1882.71,1892.03],'cii':2326.0,'mg.ii':[2795.53,2802.71],\
	'n.v':[1238.82,1242.8],'o.iii]':[1660.81,1666.15],'he.i':5876,\
	'ne.v':3426,'si.iv':1397.61,'he.ii':1640.4,'he.i':[3889,5876],\
	's.ii':[6717,6731],'hbeta':4862.68,'ne.iii':3869.81,'n.ii':[6549.81,6585.23],\
	'si.iv+o.iv]':1400,'niv]':1486,'hdelta':4102.89,'hgamma':4341.68}
# SiIV+OIV] blend in AGN: https://arxiv.org/pdf/1312.7500.pdf


# given a line, returns the wavelength(s)
def which_lines(line):
	print('Restframe: %s angstroms'%(dic[line]))
	print()

# reads in input for scripted version
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('\nThis script returns the restframe wavelength(s) of any line in\n'
			'the dictionary below. As many lines can be added as wanted.\n')
		print('Use the following notation:   line [line name]\n')

	else:
		try:
			which_lines(str(sys.argv[1]))
		except KeyError: # if you reference a line not listed above
			print('That line does not exist in the dataset.')
			print()
