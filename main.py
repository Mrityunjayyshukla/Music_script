import streamlit as st
from spotify_script import get_token, search_song
from youtube_script import search_video, video_link
from youtube_download_script import download_audio_from_youtube
from audio_details_script import change_metadata, save_image_from_url, cover_image, delete_image

# Spotify Authorization and fetching the details
token = get_token()
no_of_res = 3
song_name = input("Enter the name of the song: ")
result = search_song(token, song_name, no_of_res)
song_result = []

# Format: [title, album, artist, songID, SongYear, AlbumType, cover_Image]
for i in range(no_of_res):
    song_result.append([
        result[i]['name'], 
        result[i]['album']['name'], 
        result[i]['artists'][0]['name'], 
        result[i]['external_urls']['spotify'], 
        result[i]['album']['release_date'][0:4],
        result[i]['album']['album_type'],
        result[i]['album']['images'][0]['url']
    ])

# Choosing the option
for i in range(len(song_result)):
    print(f"Song Name: {song_result[i][0]} and artist name: {song_result[i][2]}")

choice = int(input("Which song to choose: "))
if choice > no_of_res:
    print("Error: Choice invalid")
song_name, song_album, song_artist, song_ID, songYear, albumType, coverImage = song_result[choice-1]


# Getting the youtube URL from the youtube API
youtube_response = search_video(f"{song_name} - {song_artist} Official Audio")
video_id = youtube_response['items'][0]['id']['videoId']

youtube_link = video_link(video_id)

# Downloading the song from Youtube
if song_name[-1] == ".":
    song_name = song_name[0:len(song_name)-1]
file_path = download_audio_from_youtube(youtube_link, f'downloads/{song_name}')

# Changing the text metadata of the audio
change_metadata(f"{file_path}.mp3", title=song_name, artist=song_artist, album=song_album, genre=albumType, album_artist=song_artist, year=songYear)

# Downloading cover_image and changing it in audio metadata
local_file_name = "downloaded_cover.jpg"
save_image_from_url(coverImage, local_file_name)
cover_image(f"{file_path}.mp3", local_file_name)

# Delete the image
delete_image(local_file_name)

# Return the song path
print(f"{song_name} by {song_artist} is saved as {file_path}.mp3")