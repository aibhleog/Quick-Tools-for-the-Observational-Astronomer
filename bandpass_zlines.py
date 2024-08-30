'''
This is a script that can be implemented into your .bashrc and used
to plot a redshifted spectrum and show relevant lines of interest.

As Taylor mostly works in the NIR and IR, the bandpasses plotted only
cover that wavelength space, although this code can easily be adapted
to fit your needs.

One possible way to do this would be, based upon the redshift and
resulting spectral range covered, you could only plot the bandpasses
that would show up there.  That could cut down on the number of
unnecessary filters shown in your legend.

Filters for most every telescope/instrument pair can be found using
the SVO Filter Profile Service:
http://svo2.cab.inta-csic.es/svo/theory/fps3/

Credit: 	Taylor Hutchison
		astro.hutchison@gmail.com
'''

import numpy as np
import matplotlib.pyplot as plt
import igm_absorption as igm # 	another script written by Taylor Hutchison
				 #	which adds in IGM absorption for the higher redshifts
import os
import add_lines # written by TAH
import filters as filt


def bandpass_zlines(redshift):

	# Cloudy model provided by Taylor Hutchison
	# Single stellar population from BPASS with age=10Myr & IMF that goes to 100 Msolar,
	# Z(stellar)=Z(nebular)=0.2 Zsolar, ionization parameter log_10(U)=-2.1, n_H=300 cm^(-3)
	z,zneb,u = 0.2,0.2,-2.1
	model = 'information/age7z%szneb%su%s_100.con'%(z,zneb,u)
	path = '/Users/tahutch1/code/useful-code/'
	con = np.loadtxt(path+model,usecols=[0,6])
	wave,vfv = con[:,0],con[:,1]
	#print(wave[0]*1e4,wave[-1]*1e4)
	nu = 2.998e+14 / wave
	sed_0 = vfv / nu

	# plotting the redshifted spectrum
	plt.figure(figsize=(16.5,5))
	ax = plt.gca()

	# --- adding filters --- #
	# ---------------------- #
	# plotting the filters that are in the range

	filts, filt_total = filt.is_it_in_range(redshift)
	for telinst in filts.keys(): # going through telescope/instruments
		bands = filts[telinst]
		if len(bands) > 0:
			for band in bands:
				f = filt.get_filter(telinst,band)
				f_info = filt.get_filter_info(telinst,band)

				scale = (1e-14/max(f.throughput.values)) # just to scale them all the same
				ax.fill_between(f.wave/1e4,f.throughput*scale,0,alpha=0.3,zorder=0,\
					label=f_info['name'],facecolor=f_info['color'],edgecolor=f_info['edgecolor'])
				ax.plot(f.wave/1e4,f.throughput*scale,alpha=0.8,color=f_info['color'])


	# applying IGM absorption depending upon z
	sed = sed_0 * igm.igm_absorption(wave*1e4*(1+redshift),redshift)
	ax.plot(wave*(1+redshift),sed,color='k',lw=2.)
	add_lines.draw_lines(ax,2e-14,redshift,xlim='halpha',exclude='nii1') # adding in the line labels

	ax.set_yscale('log')
	ax.set_yticklabels([])
	ax.tick_params(labelsize=16)
	ax.set_xlabel(f'observed wavelength for $z=\,${redshift} [microns]',fontsize=16)
	ax.set_xlim(0.08*(1+redshift),0.668*(1+redshift))
	ax.set_ylim(1e-15,3.5e-13)

	leg = ax.legend(frameon=False,loc=9,fontsize=13,ncol=filt_total,bbox_to_anchor=(0.5,1.14)) # was 1.12
	#for lh in leg.legendHandles:
	#	lh.set_alpha(1)

	plt.tight_layout()
	#plt.show()
	plt.savefig(f'{path}information/spec-with-lines-bandpass.png',dpi=300)
	plt.close('all')

	# opening image from the terminal
	os.system(f'open {path}information/spec-with-lines-bandpass.png')


# reads in input for scripted version
if __name__ == "__main__":
	import sys
	if sys.argv[1] == 'help':
		print('''
Given a redshift, this command will show a spectrum that
has been redshifted with relevant lines marked. In addition,
it will show relevant NIR and IR bandpasses.

Use the following notation:   zlines [redshift]
''')
	else:
		try:
			bandpass_zlines(float(sys.argv[1]))
		except IndexError: # if you don't list a redshift
			z = 0.
			print('Redshift not specified, set to z=0.',end='\n\n')
			bandpass_zlines(z)
