import plotter_driver

def main():
  rows = plotter_driver.get_contents_csv("./sample-input.csv")

  print(rows)

if __name__ == "__main__":
  main()
