
'''
Code used to add the lines into the zlines script.

Requires an axes variable, a y-axis value, and a redshift.

Optional commands include:
    text flag : defaults 'yes', will add lines if 'yes'
    aa flag : defaults False; will convert to angstroms if True
    xlim flag : defaults False; will cut down line list if True


NOTES:
Eventually would like to include a way to EXCLUDE specific lines, in addition to the zooming in on lines that I already have.

'''

__author__ = 'Taylor Hutchison'
__email__ = 'astro.hutchison@gmail.com'


# plotting relevant lines -- feel free to add more!
lines = {'lya':[1215.67,r'Ly$\alpha$'],'nv':[1240,'NV $\lambda$1240'],
         'civ':[1548,'CIV $\lambda$1549'],'heii1':[1640.4,'HeII $\lambda$1640'],
         'oiii]':[1664,'OIII] $\lambda$1660,1666'],
         'siiii]':[1883,'SiIII] $\lambda$1883,1892'],
         'ciii]':[1906.8,'CIII] $\lambda$1907\n  & $\lambda$1909'],
         'mgii':[2798,'MgII $\lambda$2796\n  & $\lambda$2803'],
         '[oii]':[3727,'[OII] $\lambda$3727\n    & $\lambda$3729'],
         '[neiii]':[3869,'[NeIII] $\lambda$3870'],
         'hdelta':[4102,'H$\delta$'],'hgamma':[4341,'H$\gamma$'],
         'heii2':[4686,'HeII $\lambda$4686'],
         'hbeta':[4862.68,r'H$\beta$ $\lambda$4863'],'[oiii]1':[4959,''],
         '[oiii]2':[5007,'[OIII] $\lambda$4959\n    & $\lambda$5007'],
         'hei1':[5876,'HeI $\lambda$5876'],'nii1':[6549.81,'[NII] $\lambda$6550'],
         'halpha':[6563,r'H$\alpha$ $\lambda$6563'],'nii2':[6585.23,'[NII] $\lambda$6585'],
         'sii':[6717,'[SII] $\lambda$6717,6731'],'siii1':[9069,'[SIII] $\lambda$9069'],
         'siii2':[9531,'[SIII] $\lambda$9531'],'hei2':[10830,'HeI $\lambda$1.083$\mu$m'],
         'pagamma':[10940,r'Pa$\gamma$ $\lambda$1.094$\mu$m'],
         'pabeta':[12820,r'Pa$\beta$ $\lambda$1.282$\mu$m'],
         'paalpha':[18756.137,r'Pa$\alpha$ $\lambda$1.875$\mu$m']
         }

shifts = {'lya':[-140,2.8],'nv':[40,0],
          'civ':[-90,-0.4],'heii1':[-70,.4],
          'oiii]':[25,-0.2],'siiii]':[-85,-0.5],
          'ciii]':[50,0.4],'mgii':[40,0],
          '[oii]':[-180,0],'[neiii]':[-80,0],
          'hdelta':[40,0],'hgamma':[40,0],'heii2':[-100,0],
          'hbeta':[-105,0.8],'[oiii]1':[40,0],
          '[oiii]2':[70,0],'hei1':[-100,0],
          'nii1':[-110,0],'halpha':[-110,0],'nii2':[40,0],
          'sii':[40,0],'siii1':[40,0],
          'siii2':[40,0],'hei2':[40,0],
          'pagamma':[40,0],'pabeta':[40,0],'paalpha':[40,0]
          }



def get_lines(return_names=False):
    '''
    Returns the list of line ids

    INPUT --
    return_names (opt) : default False; if True will return as list.	
    '''
    line_names = list(lines.keys())

    print(line_names)
    if return_names == True: return line_names



def modify_yval(line,yval):
    '''
    Modifying the y value for a given line.	
    '''
    shifts[line][1] = yval



def modify_xval(line,xval):
    '''
    Modifying the x value for a given line.	
    '''
    shifts[line][0] = xval



def rename_line(line,name):
    '''
    Modifying the name that is plotted.
    '''
    lines[line][1] = name



def add_line(ax,wave,yval=False,name=False,aa=False,shift=30,z=0,fontsize=False):
    '''
    Manually adding a line.
    '''
    # checking if angstroms or microns
    if aa == True: xscale = 1
    else: xscale = 1e4

    ax.axvline(wave/xscale*(1+z),ls='--',color='k',alpha=.5,zorder=0)
    if name != False and yval != False: 
        if fontsize == False: font = 15
        else: font = fontsize
        ax.text((wave+shift)/xscale*(1+z),yval,'%s'%(name),\
                fontsize=font,verticalalignment='bottom',rotation='vertical')



def draw_lines(ax,yo,z,text='yes',aa=False,xlim=False,xo=1,exclude=None,noline=False,fontsize=False,alpha=None):
    '''
    INPUT --
    ax : 
    yo : 
    z : 

    text (opt) : 
    aa (opt) : default False, assumes microns; if True, angstroms
    xlim (opt) : default False; can be either one line ID or two.
                 If one, will treat that as the end of list.
                 If two, will choose only lines within that range.
    xo (opt) : default 1; can use to scale x shift up or down 
               (good for when zooming in or out of spectrum)
    exclude (opt): default None; list names of lines you'd like to
                   exclude from the plot
	noline (opt) : only adds text, no lines
	fontsize (opt) : modify fontsize
	alpha (opt) : change transparency of text boxes

    '''


    # checking if angstroms or microns
    if aa == True: xscale = 1
    else: xscale = 1e4
    
    # checking if alpha is on
    if alpha != None: props = {'facecolor':'white', 'alpha':float(alpha), 'lw':0}
    else: props=None


    line_names = list(lines.keys()) # just to get the list of all of the lines

    # checking if there's an xlimit
    # if so, will be truncating list of lines from red end
    # (will eventually do blue end too)
    if xlim != False:
        try:
            if isinstance(xlim,str) == True: # checks if string or list
                xlim_index = line_names.index(xlim)
                line_names = line_names[:xlim_index+1]
            elif len(xlim) == 2: # when there's two IDs
                xlim_start_index = line_names.index(xlim[0])
                xlim_end_index = line_names.index(xlim[1])
                line_names = line_names[xlim_start_index:xlim_end_index+1]
        except ValueError:
            print('Line specified not in list.  Here are the available line IDs:',end='\n\n')
            print(line_names,end='\n\n')
            print('Showing all lines on plot...')


    # removes line or lines from list 
    if exclude != None:
        try:
            if isinstance(exclude,str) == True: # checks if string or list
                line_names.remove(exclude)
            else:
                for remove_name in exclude:
                    line_names.remove(remove_name)
        except ValueError:
            print('The "exclude" kwarg needs to be either a string or list of strings.')



    for l in line_names: # walking through the lines
        shift, y_shift = shifts[l] # accessing shifts for line
        wave,name = lines[l] # accessing line info for line

        # setting up shifts
        y = yo + yo*y_shift # for the lines that need shifting
        shift /= xo # xo can change to help when zooming in or out

        if noline != True: ax.axvline(wave/xscale*(1+z),ls='--',color='k',alpha=.5,zorder=0)

        if text == 'yes':
            if fontsize == False: 
                if l == 'heii1' or l == 'oiii]': font = 13
                else: font = 15
            else: font = fontsize
            ax.text((wave+shift)/xscale*(1+z),y,'%s'%(name),\
                fontsize=font,verticalalignment='bottom',rotation='vertical',bbox=props)
