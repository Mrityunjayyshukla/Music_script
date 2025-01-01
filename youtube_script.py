from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# setup API key
load_dotenv()
api_key = os.getenv('YOUTUBE_API_KEY')

# Initialize the Youtube API
youtube = build('youtube', 'v3', developerKey=api_key)


# Search song video
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
def video_link(video_id):
    return f"https://www.youtube.com/watch?v={video_id}"

response = search_video("music name - artist name")
video_id = response['items'][0]['id']['videoId']

print(video_link(video_id))