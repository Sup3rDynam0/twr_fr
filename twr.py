# import query_jp
import genre_scraper
import spotify_caller
import twitter_caller
import random
import json
import tekore as tk
import requests

# country = query_jp.daily_upg()

def find_country():
    list = open("countries.json")
    country = random.choice(json.load(list))
    return country

def build_tweet(item, genre, country):
    genre = genre
    name = item["name"]
    track_link = item["external_urls"]["spotify"]
    artist = item["artists"][0]["name"]
    album = item["album"]["name"]
    artist_link = item["artists"][0]["external_urls"]["spotify"]
    preview = item["preview_url"]
    album_link = item["album"]["href"]
    release_date = item["album"]["release_date"]

    tweet = f"Today's song is {name} by {artist}\n{genre.capitalize()} from {country}\nFeatured on the album \"{album}\" ({release_date})\nSpotify Link: {track_link}\nDon't forget to follow the artist here: {artist_link}"
    return tweet

country = find_country()

print(country['name'])
genres = genre_scraper.find_rock_genres(country['name'])

if len(genres) == 0:
    print("Actually, this country isn't known for its rock music.")
    genres = genre_scraper.find_genres_by_country(''.join(country['name'].split()).lower())
    if len(genres) == 0:
        print("Actually, this country isn't known for its rock music.")
        raise Exception("The Spotify API doesn't have anything to return for the chosen genre. Please run the twr.py script agan.")

print(genres)

# choose a random genre from the list
genre = random.choice(genres)

song = spotify_caller.daily_rock_song_by_country(spotify_caller.get_token(), genre)
print(song["tracks"]["items"])

if (song["tracks"]["items"] == []):
    raise Exception("This query resulted in no tracks being returned. This can happen from time to time, but I'm working on a fix. Please run the twr.py script again.")

# if (song["album"]["explicit"] == 'true'):
#     raise Exception("The chosen song contains culturally insensitive or explicit lyrics. Trying to be family-friendly here. Please run the twr.py script again.")


# retrieve the album art and temporarily save it locally 
album_art = requests.get(song["tracks"]["items"][0]["album"]["images"][0]["url"]).content

f = open('album_art.jpg','wb')
f.write(album_art)
f.close()

tweet_text = build_tweet(song["tracks"]["items"][0], genre, country["name"])
print(tweet_text)

#tweet it
twitter_caller.create_tweet(tweet_text)