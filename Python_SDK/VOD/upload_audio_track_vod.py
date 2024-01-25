import requests

# URL of the API endpoint (replace "<video-id>" with the actual ID)
video_id = "video-id"
url = f'https://napi.arvancloud.ir/vod/2.0/videos/{video_id}/audio-tracks'

# Headers including the Authorization key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# File and data to be uploaded
files = {
    'lang': (None, 'fa'),
    'audio_track': ('filename.mp3', open('path/to/your/filename.mp3', 'rb'), 'audio/mpeg') # Make sure the file is in current directory
}

# Make the POST request
response = requests.post(url, headers=headers, files=files)

# Check if the request was successful
if response.status_code == 201:
    print("File uploaded successfully.")
    print(response.json())
else:
    print("Failed to upload file: ", response.status_code, response.text)

# Close the file (important to prevent resource leakage)
files['audio_track'][1].close()
