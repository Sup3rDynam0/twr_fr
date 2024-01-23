from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import urllib.parse
import genre_scraper
import random
import tekore as tk
import pprint

# special thanks to Felix Hildén and Tekore

load_dotenv()

# conf = tk.config_from_environment()
# scope = tk.scope.user_follow_modify
# token = tk.prompt_for_user_token(*conf, scope=scope)
# spotify = tk.Spotify(token)

client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")

def get_token():
    # pprint.pprint(dict(os.environ), width = 1)
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

def daily_rock_song_by_country(token, genre):

    # spotify = tk.Spotify(token)

    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)

    # query spotify for a random song with this genre
    first_query = f"?q=genre%{genre}&tag:new&type=track&limit=1&offset={random.randrange(50)}"
    first_query_url = url + first_query
    first_result = get(first_query_url, headers=headers)
    song_info = json.loads(first_result.content)

    return song_info

    # using the 'total' value from this song, we can query for a random song

"""
    total = song_info['tracks']['total']
    if isinstance(total, int):
        pick = random.randrange(total)
    else:
        pick = 1

    query = f"?q=genre%{genre}&tag:new&type=track&limit=1&offset={pick}"
    query_url = url + query
    result = get(query_url, headers=headers)
    song_info = json.loads(result.content)

    """


