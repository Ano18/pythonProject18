import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

file = open('movies.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title'])

p = {'page': 1}
ind = 1

url = 'https://mykadri.com/serialebi_qartulad/page/' + str(ind)

while p['page'] <= 5:
    r = requests.get(url, params=p)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    movies = soup.find(('div', {'class': 'row my-4'}))
    all_movies = movies.find_all('div', {'class': 'row my-4'})

    for i in all_movies:
        title = i.h3.a.text
        file_obj.writerow([title])

    p['page'] += 0
    sleep(randint(15, 20))

file.close()