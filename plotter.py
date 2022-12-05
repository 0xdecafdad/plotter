# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

########################
# FILE READING/WRITING #
########################

# Return contents of csv file as list of dictionaries
def get_contents_csv(
    path_to_csv):
  with open(path_to_csv) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = []
    for row in csv_reader:
      rows.append(row)

  return rows

############
# SELENIUM #
############

# Input specified latitude and longitude to respective fields on webpage
def send_coords(
    driver,
    lat,
    long):
  # Locate element on page and clear fields
  form = driver.find_element(By.ID, "rhumb-dest")
  lat_field = form.find_element(By.NAME, "lat1")
  long_field = form.find_element(By.NAME, "lon1")
  lat_field.clear()
  long_field.clear()

  # Convert lat and long to desired form
  (lat_converted, long_converted) = convert_decimal_to_degree(lat, long)

  # Enter lat and long into respective fields on webpage
  lat_field.send_keys(lat_converted)
  long_field.send_keys(long_converted)

  return 0

# Get destination point from webpage
# BUG: Lat and long output with strange characters instead of proper symbols
def get_dest(
    driver):
  # Locate element on page
  form = driver.find_element(By.ID, "rhumb-dest")
  
  # Split text of destination point element into latitude and longitude
  dest_point = form.find_element(By.CLASS_NAME, "result-point").text.split(", ")
  lat = dest_point[0]
  long = dest_point[1]
 
  # Return destination point as tuple
  return (lat, long)

# Input bearing and distance to respective fields on webpage
def send_bearing_and_distance(
    driver,
    bearing,
    distance,
    multiplier=None):
  # Locate elements on page and clear fields
  form = driver.find_element(By.ID, "rhumb-dest")
  bearing_field = form.find_element(By.NAME, "brng")
  distance_field = form.find_element(By.NAME, "dist")
  bearing_field.clear()
  distance_field.clear()

  # Multiply distance by multiplier
  distance_multiplied = distance
  if(multiplier != None):
    distance_multiplied *= multiplier

  # Enter bearing and distance to respective fields on webpage
  bearing_field.send_keys(bearing)
  distance_field.send_keys(distance_multiplied)

  return 0

##############
# CONVERSION #
##############

# Convert coordinate in form xx.xxxx (gplates decimal) to
# triple with form (degree, minute, second)
def convert_decimal_to_triple(
    coord):
  degree = coord[:2]
  minute = coord[3:5]
  second = coord[5:]

  return (degree,minute,second)

# Convert coordinate in long format to form xx.xxxx (gplates decimal)
def convert_degree_to_decimal(
    coord):
  return coord[:2] + "." + coord[4:6] + coord[8:10]

# Convert coordinate in form xx.xxxx (gplates decimal) to long format
def convert_decimal_to_degree(
    lat,
    long):
  lat_triple = convert_decimal_to_triple(lat)
  long_triple = convert_decimal_to_triple(long)

  # Latitude
  lat_degree = "%s%s %s' %s\" {}" % (lat_triple[0], u'\N{DEGREE SIGN}', lat_triple[1], lat_triple[2])

  if float(lat) >= 0:
    lat_degree = lat_degree.format('N')
  else:
    lat_degree = lat_degree.format('S')

  # Longitude
  long_degree = "%s%s %s' %s\" {}" % (long_triple[0], u'\N{DEGREE SIGN}', long_triple[1], long_triple[2])

  if float(long) >= 0:
    long_degree = long_degree.format('E')
  else:
    long_degree = long_degree.format('W')

  # Return latitude and longitude as a tuple
  #return "({}, {})".format(lat_degree, long_degree)
  return (lat_degree, long_degree)
