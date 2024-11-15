import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
webar = response.text

soup = BeautifulSoup(webar, 'html.parser')
h3s = soup.find_all('h3')

with open('./movies', mode="w", encoding='utf-8') as file:
  for i in h3s[::-1]:
    file.write(f'{i.getText()}\n')

