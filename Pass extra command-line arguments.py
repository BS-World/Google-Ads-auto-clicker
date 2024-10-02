from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("headless")

driver = webdriver.Edge(options = options)