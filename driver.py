# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import plotter
import sys
import time

def main():
  # Get command line arguments
  lat_init = sys.argv[1] # initial latitude
  long_init = sys.argv[2] # initial longitude
  #multiplier = sys.argv[3] # multiplier for distance (affects scale)
  #input_file = sys.argv[4] # file containing bearing and distance for each point

  # Create Selenium driver
  driver = webdriver.Firefox()
  driver.get("http://movable-type.co.uk/scripts/latlong.html")
  print("Driver created successfully...") # optional console output
  
  # Send initial coordinates to webpage
  try:
    plotter.send_coords(driver, lat_init, long_init)
  except Exception as e:
    print(e)

  time.sleep(3) # give time for coordinates to send

  # Send bearing and distance to webpage
  try:
    plotter.send_bearing_and_distance(driver, 75, 250)
  except Exception as e:
    print(e)

  time.sleep(3) # give time for bearing and distance to send

  # Get destination point
  try:
    print(plotter.get_dest(driver))
  except Exception as e:
    print(e)

  # Exit Selenium driver after a five second delay
  time.sleep(5)
  driver.quit()
  print("Driver exited successfully...") # optional console output

if __name__ == "__main__":
  main()
