import requests
from bs4 import BeautifulSoup

domain = 'https://chelyabinsk.n1.ru'
URL = f'{domain}/kupit/kvartiry/vtorichka/district-Kalininskiy-rayon/'

response = requests.get( URL )
print( response.status_code )

soup = BeautifulSoup( response.text, 'html.parser')

div_tags = soup.find_all( 'div', class_='living-list-card__col _main' )
#print( len( div_tags ), type( div_tags ))

for v1 in div_tags:
    #print( v1 )
    try:
        tags = v1.find('a', class_='link')
        print(tags.text)
    except  AttributeError:
        pass
    try:
        tags = v1.find('div', class_='search-item-district living-list-card__inner-block')
        print(  tags.text )
    except  AttributeError:
        pass

    try:
        tags = v1.find('div', class_='living-list-card__city-with-estate living-list-card-city-with-estate living-list-card__inner-block')
        print(tags.text)
    except  AttributeError:
        pass

    try:
        tags = v1.find('div', class_='living-list-card__area living-list-card-area living-list-card__inner-block')
        print(tags.text)
    except  AttributeError:
        pass

    try:
        tags = v1.find('div', class_='living-list-card__floor living-list-card-floor living-list-card__inner-block')
        print(tags.text)
    except  AttributeError:
        pass

    try:
        tags = v1.find('div', class_='living-list-card__material living-list-card-material living-list-card__inner-block')
        print(tags.text)
    except  AttributeError:
        pass

    print('-----------')


