The Groninger Lightning Plotter (GLP) is a python interactive plotting code for displaying lightning point sources located in 3D and time. Very heavily inspired by the great work done by New Mexico Tech.

The package includes some code to read the LMA format, and my personal format. The LMA-format reading code was written some time ago, and I don't remember it well. So good luck using it!

Required packages:
Python 3
Matplotlib
Numpy 
PyQt5


How to use:
The GLP package is called from a python script. An example is included. Note that if the script that calls GLP (e.g. the attached example) is in the same folder that includes the GLP folder (NOT inside!), then GLP does not need any kind of installation. For other uses, an install script is included. Since I do not really understand Python package management, this install script is dead-simple. It simply places a sym-link named 'GLP' in your python library. So that if a script calls "import GLP", then the python interpreter will find the sym-link to the GLP folder.

Note that GLP works with "datasets", where you can have multiple datasets. A dataset can represent a flash, piece of a flash, locations of the antennas, etc... The kind of datasets is ostensibly easy to extend so that wierd things could be plotted (e.g. maybe radar data if one is determined enough ), however such extension is probably difficult to anyone note intimately familiar with how GLP internally works.

The included example script opens up a lightning flash, turns it into a dataset, and then plots that dataset. It is relatively easy to turn numpy arrays of X, Y, Z, T source coordinates into a nice data set. The script uses a helper function, "SPSF_to_DataSet"; however this helper function is relatively simple and (unlike all the other code) I recommend any end user to read this function if they want to plot their own pointsource data that may be in a weird data format.

If you want to run this code, but don't have a nice lightning data set to plot, then please contact me.



Below is now a description of how to use the plotter once it is running. (first describe the buttons, then the mouse, then top menu bar)



BUTTONS:

On the left is a number of controls. The first drop-down menu is all available data sets. (The example only has one, named 19A-1).

Below the dataset menu are five buttons:
"show all"  : adjusts ALL bounds and cuts so that all data in this dataset is shown. 
"toggle" : makes dataset display (green) or not (red)
"delete" : removes dataset
"U"/"D"  : moves dataset up/down in the list. Useful if you have multiple datasets that you want plotted on top or below each other.

The lower drop down menu shows various properties of the dataset. The text box shows the value of that property, and the "get", "set" buttons apply to this setting to this dataset. Some common properties:
"marker size"  :  exactly what it says
"color mode"  : how the dataset is colored. Default is "time". is starts with a *, then following text is sent to matplotlib. (e.g., "*b" for a color mode will color all sources blue)
"max points" : maximum number of points to display for speed reasons. If the displayed points exceed this, random points are thrown out until this is met. 
min/max X:  cuts on the value X to control the quality of the data.


some other buttons:

"ignore time" : the dataset is no longer cut on the time bounds. This is useful to comparing lightning phenomena at different times. (e.g. if a negative leader is in one dataset, a dart leader in a second dataset, and you want to see if they overlap in space, but you want to zoom-in to one in time).

"show all time" : expands the time bounds to show all points inside the XYZ bounds and cuts (for this dataset only).


Next there are eight boxes, in four pairs, labeled x, y, z , and t. 
If "set" is clicked, these 8 boxes show the current XYZT bounds (left is minimum, right is maximum).
"to CB" / "from CB" copies the bounds to and from the clipboard. This is for interacting with scripts and saving the thing you are looking at. (format is a text python nested list. Is obvious when you look at it, just paste to a text file).

"set. pos" : sets the XYZT bounds to those in the above 8 boxes.
"show all position" : adjusts the XYZT bounds to show all sources. Similar to "show all", but doesn't change the cuts.

Search is hard to explain. It's to search for a specific source (by ID)

"zoom : in" : changes behavior zooming by-mouse (explained below), zooms in or out.

"1:1 aspect ratio" : when checked, the plotter does it's best to keep the aspect ratio of the northing/easting projection constant.
	this means that if the user drags the edges of the plotter to have a 1-1 ratio of the northing/easting projection, then it will stay 1-1. 




MOUSE:

left button : if clicked and dragged on altitude vs time, or North vs East, then will zoom out/ in (depending on setting on the left). Note, change will only occur once you release the button!

right button : if clicked and dragged on a panel, will translate the bounds appropriately. Note, change will only occur once you release the button!

middle button : undoes last action (may need many clicks...)




TOP MENU BAR
File:
	options for exporting current picture. Note that png should be prefered for plots with large number of sources.

Plot Settings: change number of ticks and font size. Takes text from dataset-options text box. (i.e. set what you want in the text box, then click the button).  Currently changes are only temperaory, and revert if you zoom or shift the plot.

Analysis:
	many interesting options that may even work!
	"print info" : prints info on all currently seen sources.
	"copy view" : creates a new dataset out of the currently seen sources. Very slow with large number of sources. Not always functional...
	"output text" : tries to output current seen sources in a text file. 
	Other options are too wierd to explain
	
"Coordinate Systems" : GLP can have different coordinate systems (how the given 3D data is mapped to each projection). This menu changes between coordinate systems.

"Help" : Does exactly what it says, but only if what you need help with is a fifth menu that does nothing useful. 



About the name:

This package is named as such, since it was originally developed in the Dutch city of Groningen.

