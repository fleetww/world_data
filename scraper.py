import urllib.request
from bs4 import BeautifulSoup

base_url = 'https://data.worldbank.org'
country_list_url = base_url + '/country'

page = urllib.request.urlopen(country_list_url)
if page.getcode() != 200:
    print('Failed to retrieve country list from ' + country_list_url)

soup = BeautifulSoup(page, 'html.parser')

overview = soup.find('div', {'class': 'overviewArea body'})
alphabet = overview.find_all('section', {'class': 'nav-item'})
for letter in alphabet:
    countries = letter.find_all('a')
    for country in countries:
        country_url = base_url + country.get('href')
        print(country.text)
        country_page = urllib.request.urlopen(country_url)
        if country_page.getcode() != 200:
            print('Failed to retrieve page for ' + country.text)
        html = BeautifulSoup(country_page, 'html.parser')
        try:
            link = next(x for x in html.find('div', {'class': 'btn-item download'}).find_all('a') if x.text == 'CSV')
        except:
            print('Could not find CSV download link for country')
            continue
        print(link.get('href'))
        urllib.request.urlretrieve(link.get('href'), filename='data/' + country.text + '.zip')