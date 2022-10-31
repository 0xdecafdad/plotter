import plotter_driver

def main():
  rows = plotter_driver.get_contents_csv("./sample-input.csv")
  print(rows)

  url = "http://movable-type.co.uk/scripts/latlong.html"
  driver = plotter_driver.create_driver(url)

if __name__ == "__main__":
  main()
