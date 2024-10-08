## Playing with your `.bashrc`
Here I'll show you ways you can manipulate your `.bashrc` file to get the most out of your terminal. 
Although, as a warning, once you start tweaking your `.bashrc`, it's hard to stop.

### I. Finding your `.bashrc` file
In case you're unsure of where this file is located, open your terminal to your home directory (`~/`) and type ```ls --all```. 
Among the list of hidden (start with '.') and visible folders and files, you'll see the `.bashrc` file.
Open it in either your default text editor (ie. `gedit .bashrc &`) or edit it in the terminal by typing `nano .bashrc`.

Generally, unless you've modified it before, your `.bashrc` should look something like this:
```
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions

# added by Anaconda3 4.3.0 installer
export PATH="/home/aibhleog/path/to/anaconda3/bin:$PATH"
```
The only things you would normally find in here are the default specifications and path exports added by package 
management software like `Anaconda`.

### II. Creating an alias
The next step is to create an alias. This is a wonderful trick that I have taken advantage of many times. 
Essentially, an alias is a keyword that you create which is representative of a phrase. For example:
```
# alias for opening jupyter notebooks
alias jn='jupyter notebook'
```
Instead of having to type `jupyter notebook` every time you want to open up your `jupyter` workspace, 
you would be able to type ```jn file.ipynb``` to open a particular file or simply ```jn``` to open up your working directory 
(as long as you're in that directory in your terminal).

The difference isn't that great, but those few seconds you save (and in my case the many seconds saved from my misspelling 
one or both of those words due to typing quickly) add up over time. But again, this is mostly a convenience -- not at all
something that you would have to have.
##### NOTE: be sure to check that the aliases you make aren't already associated with commands in your terminal.  The easiest way to check this is to open your terminal and type the alias name you want and press [Tab] a few times.  If nothing with your exact spelling (and nothing extra) pops up, then you're good to use it as an alias!

### III. Setting aliases for the 'Quick Tools' `python` scripts
Below I'll show you how I've set up the aliases in my `.bashrc` for the `python` scripts shared in this repository. 
```
# alias for printing all current python scripts by their aliases
alias pycommands='python /home/aibhleog/path/to/all_pycommands.py'

# alias for velocity offset btw two z -- useful for z(Lyman-alpha) and z(systemic)
alias offset='python /home/aibhleog/path/to/offset.velocity.py'

# alias for plot of redshifted spectrum with bandpasses overlaid
alias zlines='python /home/aibhleog/path/to/bandpass_zlines.py'

# alias for redshifted wavelength
alias zlam='python /home/aibhleog/path/to/redshift.lam.py'

# alias for redshift given two wavelengths
alias redshift='python /home/aibhleog/path/to/redshift.py'

# alias for wavelength of given line
alias line='python /home/aibhleog/path/to/lines.py'

# alias for separation between two coordinates of same units
alias sep='python /home/aibhleog/path/to/separation.py'

# alias for separation between two coordinates of different units
# NOTE: put decimal units second
alias sepmix='python /home/aibhleog/path/to/separation-mix.py

# alias for converting coordinates to specified form
alias coord='python /home/aibhleog/path/to/convert-coord.py

# alias for de-redshifting an observed wavelength given a redshift
### disclaimer: I don't use this one very often but it is helpful
alias dered='python /home/aibhleog/path/to/de.redshift.py

```
So, to see them in use:
```
[aibhleog@earth ~]$ line ha
Restframe: 6562.8 angstroms

[aibhleog@earth ~]$ zlam 6562.8 4.0
Redshifted line: 3.2814 microns

[aibhleog@earth ~]$ redshift 6562.8 32814.0
Redshift: 4.0

[aibhleog@earth ~]$ offset 7.4089 7.4095
Velocity offset of specified redshifts: 21.391620782755577 km/s

[aibhleog@earth ~]$ offset 0.5 0.502 False
Low redshift specified
Velocity offset of specified redshifts: 599.6000000000058 km/s

[aibhleog@earth ~]$ coord 00h00m00s +00d00m00s decimal
Coordinate: 0 0

[aibhleog@earth ~]$ coord 0.00 +0.00 '' false
Coordinate: 00h00m00s +00d00m00s

[aibhleog@earth ~]$ dered 3.2814 4.0
De-redshifted line: 6562.8 angstroms
```
And finally, the new script I've added, called **all_pycommands.py** (defined with an alias **pycommands** at the top of the list above), would output the following:
```
CURRENT PYTHON COMMANDS:
-----------------------------
line -- returns restframe wavelength of a line given a key
offset -- calculates the velocity offset between two redshifts
redshift -- calculates the redshift given a restframe & observed line
zlam -- redshifts a line given restframe wavelength and redshift
dered -- returns the rest wavelength given an observed line and redshift
zlines -- pops up a plot that shows a model spectrum redshifted with bandpasses overlaid

sep -- returns the separation between two coordinates of same units
sepmix -- returns the separation between two coordinates of different units
coord -- converts given coordinates to a specified format
```
This is very helpful for me personally, because I keep adding more and more things to my `.bashrc` so it's hard to keep track without this!
### *That's it!*
I hope you have fun playing with your `.bashrc` and modifying it to improve your productivity!


