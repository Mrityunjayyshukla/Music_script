from dotenv import load_dotenv
import os, base64, json
from requests import post, get, put

# TODO: Use Spotify API to get the name of the song then
# use the name of the song to get the information and lyrics of the song

# Load the environment variables
load_dotenv()   
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
scope = os.getenv('SCOPE')

# Get the token
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
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Search the song
def search_song(token, song_name, no_of_result):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={song_name}&type=track&limit={no_of_result}"

    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']['items']
    return "No result found" if len(json_result) == 0 else json_result


token = get_token()
song_name = input("Enter the name of the song: ")
no_of_result = 3
result = search_song(token, song_name, no_of_result)

for i in range(no_of_result):
    print(f"Song Name: {result[i]['name']}")
    print(f"Album Name: {result[i]['album']['name']}")
    print(f"Artist Name: {result[i]['artists'][0]['name']}")
    print(f"Song ID: {result[i]['external_urls']['spotify']}")
    print()