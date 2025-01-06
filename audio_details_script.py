from mutagen.easyid3 import EasyID3
import mutagen
import requests, os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
import streamlit as st

# Save the image
@st.cache_data
def save_image_from_url(url, file_name):
    # Send a GET request to the URL to retrieve the image
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the image
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {file_name}")
    else:
        print(f"Failed to retrieve the image. Status code: {response.status_code}")

# Changing the metadata
@st.cache_data
def change_metadata(file_path, title = None,artist = None,album = None,genre = None,album_artist = None,year = None):
    try:
        audio = EasyID3(file_path)
    except mutagen.id3.ID3NoHeaderError:
        audio = mutagen.File(file_path, easy=True)
        audio.add_tags()

    # Update text metadata
    if title:
        audio['title'] = title
    if artist:
        audio['artist'] = artist
    if album:
        audio['album'] = album
    if genre:
        audio['genre'] = genre
    if album_artist:
        audio['albumartist'] = album_artist
    if year:
        audio['date'] = year
    print("Metadata changed successfully")

    audio.save()

# Change cover image
@st.cache_data
def cover_image(audio_file, image_file):
    audio = MP3(audio_file, ID3 = ID3)
    with open(image_file, "rb") as img_file:
        img_data = img_file.read()

    audio.tags.add(APIC(
        encoding=3,  # 3 = UTF-8
        mime='image/jpg',  # MIME type of the image
        type=3,  # Type 3 = album art
        desc='Cover',
        data=img_data
    ))
    print("Changed value")
    audio.save()

# Delete the image file
@st.cache_data
def delete_image(file_name):
    # Check if the file exists before attempting to delete
    if os.path.exists(file_name):
        os.remove(file_name)  # Delete the file
        print(f"File {file_name} has been deleted.")
    else:
        print(f"The file {file_name} does not exist.")
