## Quick Tools for the Observational Astronomer
These are some of the quick tools I use while observing and writing proposals.
Mostly they are scripts I've integrated into my `.bashrc` (which I will describe) so that I can run them from the terminal using keywords -- a wonderfully useful trick.

### 'Quick Tools' `python` scripts
+ **offset.velocity.py** -- calculates velocity offset between two redshifts; for example: z(Lyman-alpha) and z(systemic)
+ **redshift.lam.py** -- calculates the redshifted wavelength (in Angstroms) of a line given a restframe wavelength and a redshift
+ **redshift.py** -- calcuates the redshift given a restframe wavelength (in Angstroms) and a redshifted wavelength (in Angstroms)
+ **lines.py** -- returns restframe wavelength(s) of a line given the line's key (string; ie. 'ha' for H-alpha)

Be sure to look at **`playing-with-your-bashrc.md`** for an outline of how to integrate the `python` scripts into your terminal!
##### NOTE: the scripts assume your default `python` is `python 3.6.0`
