import requests
from bs4 import BeautifulSoup
from contextlib import redirect_stdout

def find_genres_by_country(country):

    genres = []
    # big big thanks to Glenn MacDonald
    link = "https://everynoise.com/countries.html"
    link_text = requests.get(link).text

    # BeautifulSoup Object
    soup = BeautifulSoup(link_text, 'html.parser')

    # Save the genre information to a local file
    with open('genre_list.txt', 'w') as f:
        print(soup.encode("utf-8"), file=f)

    # find our td_tags from everynoise
    table = soup.find('table')
    tr = table.find('tr')
    td_tags = tr.find_all('td', {'class': 'column'})

    # loop through to find our country and all valid genres 
    for tag in td_tags:
        div = tag.find('div', {'class': 'country'})
        if div:
            if div.attrs == {'class': ['country'], 'id': country}:
                for sibling in div.next_siblings:
                    genre = sibling.string
                    if genre:
                        genres.append(genre)
    
    return genres

def surgenre(list, term):
    newlist = []
    for genre in list:
        if term in genre:
            newlist.append(genre)
    return newlist

def find_rock_genres(country):
    genrelist = find_genres_by_country(''.join(country.split()).lower())
    genre_options = surgenre(genrelist, 'metal') + surgenre(genrelist, 'rock') + surgenre(genrelist, 'indie') + surgenre(genrelist, 'punk')
    return genre_options
