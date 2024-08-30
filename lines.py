'''
This script returns the restframe wavelength(s) of any line in the dictionary below.
As many lines can be added as wanted.

Some line wavelengths come from:
http://astronomy.nmsu.edu/drewski/tableofemissionlines.html
'''

import numpy as np
import pandas as pd

# currently holds the lines I use most frequently in my work
# absorption lines are marked as negative
dic = {'lya':1215.67,'n.v':[1238.82,1242.8],'si.iv':[1393.755,1403.77],'o.iv]':[1397.232,1399.78],\
		'n.iv]':1486.496,'c.iv':[1548.19,1550.76],'he.ii':1640.4,'o.iii]':[1660.81,1666.15],\
		'si.iii]':[1882.71,1892.03],'c.iii]':[1906.68,1908.73],'c.ii':2326.0,\
		'mg.ii':[2795.53,2802.71],'ne.v':3426,'o.ii':[3726.1,3728.8],\
		'ne.iii':3869.81,'hdelta':4102.89,'hgamma':4340.462,'hbeta':4862.68,\
		'o.iii':[4959.,5007.],'he.i':5876,'n.ii':[6549.81,6585.23],\
		's.ii':[6717,6731],'ha':6562.8,'hepsilon':3970.072,\
		'ca.h+k':[-3968.47,-3933.66], 'o.i':[6302,6365.5],
		'paalpha':18750, 'pabeta':12820, 'pagamma':10940,
		'bralpha':40510,'brbeta':26250,'brgamma':21660}

# SiIV+OIV] blend in AGN: https://arxiv.org/pdf/1312.7500.pdf

# given a line, returns the wavelength(s)
def which_lines(line):
	print(f'Restframe: {dic[line]} angstroms')
	print()

# reads in input for scripted version
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('''
This script returns the restframe wavelength(s) of any line in
the dictionary below. As many lines can be added as wanted.
				 
Use the following notation:   	line [line name]
Or to see all of them:		line all
''')	

	else:
		try:
			which_lines(str(sys.argv[1]))
		except KeyError: # if you reference a line not listed above
			if str(sys.argv[1]) == 'all': # if you want to see all lines available
				'''
				This is a thing I've added so that I can see all of the emission
				lines at the same time. I'm turning the dictionary into a pandas
				dataframe really fast so that I can sort according to wavelength.
				'''
				df = pd.DataFrame({'lines':list(dic.keys()),'values':list(dic.values()),\
									'sort':np.ones(len(dic))})
				for i in df.index.values: # because some are doublets
					try: df.loc[i,'sort'] = abs(df.loc[i,'values'][0])
					except TypeError: df.loc[i,'sort'] = abs(df.loc[i,'values'])

				# sorting the values & resetting the index
				df.sort_values(by=['sort'],inplace=True) # inplace means apply to df
				df.reset_index(inplace=True,drop=True)
				
				print('\nAll of the lines currently in dictionary:',end='\n\n')
				print(df[['lines','values']],end='\n\n')
				print('Absorption lines are marked as negative.',end='\n\n')
			
			else: # line doesn't exist yet
				print('That line does not exist in the dataset.')
				print()
