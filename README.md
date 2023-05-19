# Plotter
Quickly convert a flat map to a 3D Orthographic projection given starting coordinates and a list of distances and bearings!

This program uses the Rhumb Lines formula from [this site](http://movable-type.co.uk/scripts/latlong.html) to calculate the the coordinates on a globe for a series of points determined by a distance and absolute bearing.

## Usage
To use this program, run the following command with arguments...

	python plotter_main.py starting-latitude starting-longitude

## Methods
plotter.py contains the following methods..

**get_contents_csv(**\
	**path_to_csv)**\
Read from a csv with 2 columns and *x* rows where the first row is the columns headings. First column should be absolute bearing and the second should be distance (cm). Returns contents of csv as a list of dictionaries.

**input_coords(**\
	**driver,**\
	**latitude,**\
	**longitude)**\


**convert_decimal_to_triple(**\
	**coord)**\
Convert coordinate in format xx.xxxx to xx° xx′ xx″ N/S/E/W.

**convert_degree_to_decimal(**\
	**coord)**\
Convert coordinate in format xx° xx′ xx″ N/S/E/W to xx.xxxx.

**convert_coords_decimal_to_degree( lat, long )**
Convert tuple of coordinates in format xx.xxxx, xx.xxxx to tuple of coordinates in format xx° xx′ xx″ N/S, xx° xx′ xx″ E/W.

## Logic 
Quick overview of the logic behind driver.py...

1. Create Selenium driver
2. Send initial coordinates to webpage
3. Initialize iterator for input file
4. Send bearing and distance from first line of input file to webpage
5. Get destination coordinates output by webpage
6. Write destination coordinates to file in specified format (xx.xxxx, xx.xxxx)
7. Send destination coordinates to webpage along with bearing and distance from next line of input file to webpage
8. Repeat for all subsequent lines of input file
9. Exit Selenium driver

-----

Description: Plot points using script on website given latitude and longitude of initial point then bearing and distance for all points to be plotted

Input: one string and one int
	string: path to csv file which will be used to plot points
	int: integer to multiply distances provided in input csv file by

Output: csv file

Input csv file
--------------
30.0000 # latitude of initial point (must be to four decimal places)
60.0000 # longitude of initial point (must be to four decimal places)
55, 1.4 # bearing of point one, distance in cm of point one
77, 3 # bearing of point two, distance in cm of point two

Output csv file
---------------
1,30.0000,60.0000 # point (for convenience), latitude, longitude
2,31.2640,62.2358

Webpage: http://movable-type.co.uk/scripts/latlong.html
Section: Rhumb lines

Pseudocode
1. Read csv file
2. Establish connection to webpage using Selenium
3. Input initial latitude and longitude to webpage
 3.1. If latidude is positive, append N to end; if negative, append S
 3.2. If longitude is positive, append E to end; if negative, append W
4. Multiply distance in cm by multiplier
5. Input bearing and multiplied distance to webpage
6. Get latitude and longitude of destination point from webpage as string
7. Convert latitude and longitude from webpage into desired format (xx.xxxx)
8. Write converted latitude and longitude to output csv
9. Input latitude and longitude (not converted) to webpage along with next bearing and multiplied distance
10. Repeat until EOF (input csv) is reached

# Documentation
--
## plotter_driver.py
**get_contents_csv( path_to_csv )**
Read from a csv with 2 columns and *x* rows where the first row is the columns headings. First column should be absolute bearing and the second should be distance (cm). Returns contents of csv as a list of dictionaries.

**create_driver( url )**
Create a Selenium Firefox driver at specified url.

**convert_decimal_to_triple( coord )**
Convert coordinate in format xx.xxxx to xx° xx′ xx″ N/S/E/W.

**convert_degree_to_decimal( coord )**
Convert coordinate in format xx° xx′ xx″ N/S/E/W to xx.xxxx.

**convert_coords_decimal_to_degree( lat, long )**
Convert tuple of coordinates in format xx.xxxx, xx.xxxx to tuple of coordinates in format xx° xx′ xx″ N/S, xx° xx′ xx″ E/W.

