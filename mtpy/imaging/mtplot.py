"""
========    
mtplot
========

**Provides** 

    1. Different plotting options to represent the MT response.
    2. Ability to create text files of the plots for further analysis
    3. Class object that contains all the important information for an MT
       station.
============================= =================================================   
Functions                      Description
============================= =================================================                
plot_mt_response              plots resistivity and phase for a single station 
                              Options include tipper, strike and skew.                      
plot_multiple_mt_responses    plots multiple stations at once with options
                              of plotting in single figure, all in one
                              figure as subplots or all in one plot for
                              direct comparison.                              
plot_pt                       plots the phase tensor ellipses and parameters
                              in one plot including strike angle, minimum
                              and maximum phase, skew angle and ellipticity                           
plot_pt_pseudosection         plots a pseudo section of phase
                              tensor ellipses assuming the 
                              stations are along a profile line.
                              Options to plot induction arrows.                                   
plot_mt_map                   plots phase tensor ellipses in map view for
                              a single frequency.  Options to plot 
                              induction arrows.                                 
plot_strike                   plots strike angle estimated from the
                              invariants of the impedance tensor defined
                              by Weaver et al. [2000,2003], strike angle
                              from the phase tensor and option to plot
                              strike estimated from the induction arrows.
============================= =================================================

All plot function return plot classes where the important properties are made
attributes which can be manipulated by the user.  All classes have been
written with the basic input being edi files.  This was assumed to be the 
standard MT response file, but turns out to be not as widely used as thought. 
So the inputs can be other arrays and class objects (see MTplot doc string for
details).  If you have a data file format you can create a class using the 
objects in mtpy.core to create an input, otherwise contact us and we can try 
to build something. 

A typical use might be loading in all the .edi files in and plotting them in 
different modes, like apparent resistivity and phase, phase tensor pseudo 
section and strike angle.
 
:Example: ::
    
    >>> import mtpy.imaging.mtplot as mtplot
    >>> import os
    >>> import matplotlib.pyplot as plt
    >>> edipath = r"/home/MT/EDIfiles"
    >>> #create a list of full paths to the edi files
    >>> edilst = [os.path.join(edipath,edi) for edi in os.listdir(edipath)
    >>> ...        if edi.find('.edi')>0]
    >>> #plot apparent resisitivity, phase and induction arrows as individual
    >>> #figures
    >>> rpm = mtplot.plot_multiple_mt_responses(fn_lst=edilst, plot_style='1',
    >>> ...                                     plot_tipper='yr')
    >>> #close all the plots after done looking at them
    >>> plt.close('all')
    >>> #plot phase tensor pseudo section with induction arrows
    >>> pts = mtplot.plot_pt_pseudosection(fn_lst=edilst, 
    >>> ...                                plot_tipper='yr')
    >>> # write out the phase tensor parameter values to files
    >>> pts.writeTextFiles()
    >>> #change coloring scheme to color by skew and a segmented colormap
    >>> pts.ellipse_colorby = 'skew_seg'
    >>> pts.ellipse_cmap = 'mt_seg_bl2wh2rd'
    >>> pts.ellipse_range = (-9, 9, 3)
    >>> pts.redraw_plot()

:Authors:
    Lars Krieger,
    Jared Peacock, and
    Kent Invariarty
    

:Version: 0.0.1 of 2013


"""
#==============================================================================

from mtpy.imaging.plotnreponses import PlotMultipleResponses as plotnresponses
from mtpy.imaging.plotpseudosection import PlotResPhasePseudoSection as plotrpps
from mtpy.imaging.plotpt import PlotPhaseTensor as plotpt
from mtpy.imaging.plotptpseudosection import PlotPhaseTensorPseudoSection as plotptps
from mtpy.imaging.plotptmaps import PlotPhaseTensorMaps as plotptmaps
from mtpy.imaging.plotresponse import PlotResponse as plotresponse
from mtpy.imaging.plotstrike import PlotStrike as plotstrike

#==============================================================================


def plot_mt_response(**kwargs):
                         
    """
    plots the MT response for a single station.  
    
    """
    
    return plotresponse(**kwargs)

def plot_multiple_mt_responses(**kwargs):
    """
    plot multiple MT responses    
    
    """
    
    return plotnresponses(**kwargs)

def plot_pt(**kwargs):
                
    """
    plots the phase tensor ellipses along with the strike, minimum phase,
    maximum phase, skew and ellipticity.    
    
    """
              
    return plotpt(**kwargs)

def plot_pt_pseudosection(**kwargs):
              
    return plotptps(**kwargs)

def plot_pt_map(**kwargs):
                    
    """
    plots a map of phase tensor ellipses for a given frequency.
    
    """
    
    return plotptmaps(**kwargs) 

def plot_strike(**kwargs):
    """
    plots the strike angle.    
    
    """
                    
              
    return plotstrike(**kwargs)

def plot_resphase_pseudosection(**kwargs):
    """
    plots resistivity and phase as a pseudo section    
    
    """
    
    return plotrpps(**kwargs)
