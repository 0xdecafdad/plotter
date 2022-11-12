from selenium import webdriver
import csv
import time

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

# Connect to webpage
def create_driver(
    url):
  driver = webdriver.Firefox()
  driver.get(url)

  return driver

# Gracefully exit driver after three second delay
def destroy_driver(
    driver):
  time.sleep(3)
  driver.quit()
  print("Driver successfully closed.")

# Locate element on page
def locate_element(
    driver):
  return driver.find_element(By.ID, "rhumb-dest")

##############
# CONVERSION #
##############

# Convert decimal to triple (degree, minute, second)
def convert_decimal_to_triple(
    coord):
  degree = coord[:2]
  minute = coord[3:5]
  second = coord[5:]

  return (degree,minute,second)

# Convert coordinate to decimal
def convert_degree_to_decimal(
    coord):
  return coord[:2] + "." + coord[4:6] + coord[8:10]

# Convert coords from decimal to degrees
def convert_coords_decimal_to_degree(
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
  return "({}, {})".format(lat_degree, long_degree)


# Convert coords from degrees to decimal
#def convert_coords_degree_to_decimal(
#    lat,
#    long):

# Send initial latitude and longitude to webpage
#def send_coords(
#    lat,
#    long):
