import plotter_driver
import sys

def main():
  # Get command line arguments
  latitude = sys.argv[1]
  longitude = sys.argv[2]
  #multiplier = sys.argv[3]
  #csv_file = sys.argv[4]

  print(plotter_driver.convert_coords_decimal_to_degree(latitude, longitude)) 

if __name__ == "__main__":
  main()
