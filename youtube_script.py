from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import streamlit as st

# setup API key
load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')

# Initialize the Youtube API
youtube = build('youtube', 'v3', developerKey=api_key)

# Search song video
@st.cache_data
def search_video(query, max_results = 5):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )
    response = request.execute()
    return response

# Get the video link
@st.cache_data
def video_link(video_id):
    return f"https://www.youtube.com/watch?v={video_id}"
