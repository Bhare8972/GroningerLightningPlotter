#!/usr/bin/env python3

# import numpy as np

from GLP.plotter import *                         ### this is for plotting
from GLP.SPSF_readwrite import pointSource_data   ### this is for reading (and writing!) this data format

if __name__=="__main__":
    data_location = "./flash_19A1_LOFARImpulsiveImager.txt"


    width_height = None
    # width_height = [1069.2, 918.0]  ## this can be used to set a size for the plotter. IF None, a default size is choosen. Note, if the ratio is off, then the northing vs easting will not have a 1-1 ratio


    ### LOAD the data
    SPSF_file = pointSource_data( data_location )
    # data_numpy_array = SPSF_file.get_data()   ## this line returns all data as a numpy array 



    #### make color maps and coordinate systems ####
    cmap = gen_olaf_cmap()
    coordinate_systemA = typical_transform([0.0, 0.0, 0.0], 1.153)  ## this can be used to shift the 0 in X,Y,Z and T
    
    
    #### make the widget ####
    plotter = Active3DPlotter( [coordinate_systemA], width_height=width_height )
    plotter.show()
    
    

    ## this is just a helper function to turn the data in to dataset to be plotted
    ## Unlike everything else, it is rather simple. It is not hard to make numpy arrays of source locations (and other info), into a dataset to be plotted
    new_dataset = SPSF_to_DataSet(SPSF_file, name='19A-1', cmap=cmap, marker='s', marker_size=5, color_mode='time')
    plotter.add_dataset( new_dataset )




    ## RUN!
    plotter.qApp.exec_()
