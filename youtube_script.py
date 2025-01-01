from googleapiclient.discovery import build
from dotenv import load_dotenv
import os, base64, json

# setup API key
api_key = os.getenv('YOUTUBE_API_KEY')

# Initialize the Youtube API
youtube = build('youtube', 'v3', developerKey=api_key)

# Check example
# Checking top5 popular videos
request = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    chart="mostPopular",
    regionCode="US",
    maxResults=5
)
response = request.execute()

# Response 
for item in response['items']:
    print(f"title: {item['snippet']['title']}")
    print(f"Views: {item['statistics']['viewCount']}")
    print()