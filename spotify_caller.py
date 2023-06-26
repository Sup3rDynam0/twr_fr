from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import urllib.parse
import genre_scraper
import random

load_dotenv()

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def daily_rock_song_by_country(token, country, genres):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)

    # choose a random genre from the list
    genre = random.choice(genres)

    # query spotify for a random song with this genre
    query = f"?q=genre%{genre}&tag:new&type=track&limit=50&offset=0"
    query_url = url + query
    result = get(query_url, headers=headers)
    song_info = json.loads(result.content)

    return json.dumps(song_info, indent=4)
