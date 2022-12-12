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
  input_file = sys.argv[3] # file containing bearing and distance for each point
  #multiplier = sys.argv[4] # multiplier for distance (affects scale)

  # Create Selenium driver
  driver = webdriver.Firefox()
  driver.get("http://movable-type.co.uk/scripts/latlong.html")
  print("Driver created successfully...") # optional console output
  
  # Send initial coordinates to webpage
  try:
    plotter.send_coords(driver, lat_init, long_init)
  except Exception as e:
    print(e)

  # Main loop
  # Open input file for reading and output file for writing
  with open(input_file, 'r') as input_file, open('output_file.txt', 'w', newline='') as output_file:
    for line in input_file:
      # Process input and send to webpage
      line_proc = line.strip().split(',')
      bearing = line_proc[0]
      distance_raw = line_proc[1]
      plotter.send_bearing_and_distance(driver, bearing, distance_raw)
      time.sleep(1)

      # Get destination coordinates now that all necessary info has been passed to webpage
      dest_point = plotter.get_dest(driver)
      print(dest_point)

      # Write to output file in format xx.xxxx, xx.xxxx

  # Exit Selenium driver after a five second delay
  time.sleep(3)
  driver.quit()
  print("Driver exited successfully...") # optional console output

if __name__ == "__main__":
  main()
