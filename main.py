import streamlit as st
from spotify_script import get_token, search_song
from youtube_script import search_video, video_link
from youtube_download_script import download_audio_from_youtube
from audio_details_script import change_metadata, save_image_from_url, cover_image, delete_image

st.markdown("# Welcome to Music Script 🌐")

# Spotify Authorization and fetching the details
token = get_token()
no_of_res = 5
song_name = st.text_input("Search song: ")
if song_name:
    song_result = search_song(token, song_name, no_of_res)
    if song_result == "No result found":
        st.write(song_result)
    elif isinstance(song_result, list) and len(song_result) > 0:
        selected_song = None
        # Create a variable to store the checkbox key
        checkbox_key = st.radio("Select one song", options=[f"{song['name']} by {', '.join([artist['name'] for artist in song['artists']])}" for song in song_result], index=None)
        
        
        if checkbox_key:
            selected_song = song_result[[f"{song['name']} by {', '.join([artist['name'] for artist in song['artists']])}" for song in song_result].index(checkbox_key)]
        if selected_song:
            track_name = selected_song['name']
            track_album = selected_song['album']['name']
            artists = ", ".join([artist['name'] for artist in selected_song['artists']])
            song_url = selected_song['external_urls']['spotify']
            release_year = selected_song['album']['release_date'][0:4]
            album_type = selected_song['album']['album_type']
            cover_image_url = selected_song['album']['images'][0]['url']

            left_column, right_column = st.columns([0.25, 0.75])
            left_column.image(cover_image_url, caption=f"Album cover for {track_name}", )
            right_column.write(f"**Song:** {track_name}")
            right_column.write(f"**Album** {track_album}")
            right_column.write(f"**Artists:** {artists}")
            right_column.write(f"**Released in:** {release_year}")
            right_column.write(f"[Listen on Spotify]({song_url})")

            st.write(f"You chose **{track_name}** by ***{artists}***")


            # Getting the youtube URL from the youtube API
            youtube_response = search_video(f"{track_name} - {artists} Official Audio")
            video_id = youtube_response['items'][0]['id']['videoId']

            youtube_link = video_link(video_id)
            st.write(f"Here's your link to the song: [Play on YouTube]({youtube_link})")
            # # Downloading the song from Youtube
            if st.button("Download the song"):
                if song_name[-1] == ".":
                    song_name = song_name[0:len(song_name)-1]
                file_path = download_audio_from_youtube(youtube_link, f'downloads/{track_name}')

                # # Changing the text metadata of the audio
                change_metadata(f"{file_path}.mp3", title=track_name, artist=artists, album=track_album, genre=album_type, album_artist=artists[0], year=release_year)
                music_data = [
                    ["Song", "Album", "Artist", "Release year"],
                    [track_name, track_album, artists, release_year]
                ]
                st.dataframe(music_data, hide_index=True)


                # Downloading cover_image and changing it in audio metadata
                local_file_name = "downloaded_cover.jpg"
                save_image_from_url(cover_image_url, local_file_name)
                cover_image(f"{file_path}.mp3", local_file_name)

                # Delete the image
                delete_image(local_file_name)

                # Return the song path
                st.write(f"**{track_name}** downloaded at ***{file_path}***")
                st.markdown("### Listen Here")
                st.audio(f"{file_path}.mp3", format="audio/mp3")