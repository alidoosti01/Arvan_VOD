import requests
import json

# URL of the API endpoint (replace "<CHANNEL-ID>" with the actual channel ID)
channel_id = "<CHANNEL-ID>"
url = f"https://napi.arvancloud.ir/vod/2.0/channels/{channel_id}/videos"

# Headers including Content-Type and Authorization
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Data to be sent in POST request
data = {
    "title": "<FILE-NAME>", # required
    "convert_mode": "auto", # required
    "description": "<DESCRIPTION>",
    "audio_url": "<AUDIO-DOWNOAD-LINK>" # required

    # # If you want to use
    # "profile_id": "<string>",
    # "thumbnail_time": "<integer>",
    # "watermark_id": "<string>",
    # "watermark_area": "<string>",

    # # If you set manaual in convert_mode
    # "convert_info": [
    # {
      # "audio_bitrate": "<integer>",
      # "video_bitrate": "<integer>",
      # "resolution": "<string>"
    # },
    # {
      # "audio_bitrate": "<integer>",
      # "video_bitrate": "<integer>",
      # "resolution": "<string>"
    # }
  # ],


    # # If your VOD plan is professional
    # "parallel_convert": <BOOLEAN>,

}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    print("Request was successful.")
    print(response.json())
else:
    print("Failed to make request: ", response.status_code, response.text)
