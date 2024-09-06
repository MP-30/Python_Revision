import pytube
from pytube.cli import on_progress
from urllib.parse import urlparse, parse_qs

def clean_youtube_url(url):
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id[0]}"
    return url.split('&')[0]

def download_youtube_video(url):
    try:
        # Clean the YouTube URL
        clean_url = clean_youtube_url(url)
        
        # Create a YouTube object with the provided URL
        instance = pytube.YouTube(clean_url, on_progress_callback=on_progress)

        # Get the highest resolution stream available
        video_stream = instance.streams.get_highest_resolution()

        # Download the video
        video_stream.download()

        print("Video downloaded successfully.")
    except pytube.exceptions.PytubeError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompt the user to input the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Download the video
download_youtube_video(url)
