from selenium import webdriver
import csv

# Return contents of csv file as list of dictionaries
def get_contents_csv(
    path_to_csv):
  with open(path_to_csv) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = []
    for row in csv_reader:
      rows.append(row)

  return rows

# Create Selenium driver
def create_driver(
    url):
  driver = webdriver.Firefox()

  return driver.get(url)
