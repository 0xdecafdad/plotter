import plotter_driver
import sys
import time

def main():
  # Get command line arguments
  latitude = sys.argv[1]
  longitude = sys.argv[2]
  #multiplier = sys.argv[3]
  #csv_file = sys.argv[4]

  #print(plotter_driver.convert_coords_decimal_to_degree(latitude, longitude))

  driver = plotter_driver.create_driver("http://movable-type.co.uk/scripts/latlong.html")
  
  try:
    print(plotter_driver.input_coords(driver, latitude, longitude))
  except Exception as e:
    print(e)

  print(plotter_driver.get_dest(driver))

  #plotter_driver.destroy_driver(driver)

if __name__ == "__main__":
  main()
