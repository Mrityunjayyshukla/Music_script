from dotenv import load_dotenv
import os, base64, json
from requests import post, get, put
import streamlit as st

# TODO: Use Spotify API to get the name of the song then
# use the name of the song to get the information and lyrics of the song

# Load the environment variables
load_dotenv()   
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
scope = os.getenv('SCOPE')

# Get the token
@st.cache_data
def get_token():
    auth_str = client_id + ":" + client_secret
    auth_bytes = auth_str.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

# Get the authorization header
@st.cache_data
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Search the song
@st.cache_data
def search_song(token, song_name, no_of_result):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={song_name}&type=track&limit={no_of_result}"

    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    if result.status_code != 200:
        return f"Error: {result.status_code} - {result.text}"
    try:
        json_result = result.json()
        if 'tracks' in json_result and 'items' in json_result['tracks']:
            tracks = json_result['tracks']['items']
            if len(tracks) == 0:
                return "No result found"
            else:
                return tracks
        else:
            return "Error: Unexpected response format"
    except json.JSONDecodeError:
        return "Error: Unable to decode response from Spotify API"
    except Exception as e:
        return f"Error: {str(e)}"