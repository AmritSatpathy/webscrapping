import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers')


soup = Beautiful(response.text,'html.parser')

print(soup.find_all(class_='container-flui'))