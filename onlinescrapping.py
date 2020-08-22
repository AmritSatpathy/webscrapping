import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.linkedin.com/in/pallavi-satpathy-a9910b108/')


soup = BeautifulSoup(response.text,'html.parser')

posts = soup.find_all(class_="someclass name")
with open('csv.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title','Link','Date']
    csv_writer.writerow(headers)
    for post in posts:
        tilte = soup.find_all(class_='container-fluid blog-hero')[0].get_text().replace('\n','')
        link = post.find('a')['href']
        date = post.select('.id')[0].get_text()
        csv_writer.writerow([tilte,link,date])