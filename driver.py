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
    print(plotter.send_coords(driver, lat_init, long_init))
  except Exception as e:
    print(e)

  # Exit Selenium driver after three second delay
  time.sleep(3)
  driver.quit()
  print("Driver exited successfully...") # optional console output

if __name__ == "__main__":
  main()
