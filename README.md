# Lipid-Density-Heatmap
This collection of scripts collects and analyzes the coordinate density of phospholipid head groups during membrane formation
using the output files from an AMBER simulation.  They work in conjunction with one another as follows:

trajscriptgenerator.py      - generates a cpptraj script to strip all but the P atoms
(run cpptraj script)
axisort.py                  - sorts the P atom coordinates into three separate files, one for each axis x,y,and z
mapbinsort.py               - generates the .csv file that can be used to generate a density/time histogram, or to calculate the 0-value
                              proportions of each frame's density values (for use in determining membrane formation point)
colormap.R                  - generates heatmap of membrane formation process


propcalcscriptgenerator.py  - generates an R script to calculate the proportion of 0-density values in each frame of a desired region of
                              the formation process
propcalc.R                  - calculates the proportion of 0-values in each frame and outputs proportions to a graph-ready text file
