import urllib.request
from bs4 import BeautifulSoup

#Tries to request url twice, if it fails both it will raise the error
def request_page(url):
    try:
        page = urllib.request.urlopen(url)
    except:
        try:
            page = urllib.request.urlopen(url)
        except:
            raise
    
    if page.getcode() != 200:
        raise Exception('Did not receive \'200 OK\' from ' + url)

    return page

def scraper():
    base_url = 'https://data.worldbank.org'
    country_list_url = base_url + '/country'
    try:
        page = request_page(country_list_url)
    except Exception as e:
        print(e)
        exit(1)

    soup = BeautifulSoup(page, 'html.parser')
    overview = soup.find('div', {'class': 'overviewArea body'})
    alphabet = overview.find_all('section', {'class': 'nav-item'})
    for letter in alphabet:
        countries = letter.find_all('a')
        for country in countries:
            print(country.text)
            country_url = base_url + country.get('href')
            try:
                country_page = request_page(country_url)
            except Exception as e:
                print(e)
                continue

            html = BeautifulSoup(country_page, 'html.parser')
            try:
                link = next(x for x in html.find('div', {'class': 'btn-item download'}).find_all('a') if x.text == 'CSV')
            except:
                print('Could not find CSV download link for ' + country.text)
                continue
            urllib.request.urlretrieve(link.get('href'), filename='data/' + country.text + '.zip')

def main():
    scraper()

if __name__ == "__main__":
    main()