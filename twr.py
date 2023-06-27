# import query_jp
import genre_scraper
import spotify_caller
import random
import json
import tekore as tk

# country = query_jp.daily_upg()

def find_country():
    list = open("countries.json")
    country = random.choice(json.load(list))
    return country

country = find_country()

print(country['name'])
genres = genre_scraper.find_rock_genres(country['name'])
if len(genres) == 0:
    print("Actually, this country isn't known for its rock music.")
    genres = genre_scraper.find_genres_by_country(''.join(country['name'].split()).lower())

print(genres)


song = spotify_caller.daily_rock_song_by_country(spotify_caller.get_token(), country, genres)
print(song)
