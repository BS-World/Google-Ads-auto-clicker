from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service(verbose = True)

driver = webdriver.Edge(service = service)