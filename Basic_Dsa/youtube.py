import pytube

# Prompt the user to input the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object with the provided URL
instance = pytube.YouTube(url)

# Get the highest resolution stream available
video_stream = instance.streams.get_highest_resolution()

# Download the video
video_stream.download()

print("Video downloaded successfully.")
