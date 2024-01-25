import requests
import json

# URL of the API endpoint
url = 'https://napi.arvancloud.ir/live/2.0/streams'

# Headers including Content-Type and Authorization
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Data to be sent in POST request
data = {
    "title": "<strin>", # Required
    "slug": "<strin>", # Required
    "fps": 30, # Required
    "convert_info": [ # Required
        {
            "audio_bitrate": 320,
            "video_bitrate": 2000,
            "resolution_width": 1080,
            "resolution_height": 980
            # # If you want to use
            # "watermark_id": "eu cupidatat Ut tempor",
            # "watermark_area": "ANIMATE_LEFT_TO_RIGHT"
        } #,
        # {
        #     "audio_bitrate": 320,
        #     "video_bitrate": 2000,
        #     "resolution_width": 1080,
        #     "resolution_height": 980
            # # If you want to use
            # "watermark_id": "eu cupidatat Ut tempor",
            # "watermark_area": "ANIMATE_LEFT_TO_RIGHT"
        # },
    ],
    "mode": "push", # Required
    "type": "normal", # Required
    "description": "<strin>"

    # # If you choose the pull mode for stream
    # "input_url": "<Pull-URL>",

    # # If your LIVE plan is growth
    # "timeshift": -6421919,
    # "fps_mode": "auto",
    # "archive_enabled": false,
    # "archive_mode": "manual",
    # "channel_id": "ut sed tempor occaecat officia",
    # "watermark_id": "deserunt Duis cillum molli",
    # "watermark_area": "FIX_TOP_LEFT",

    # # If your LIVE plan is profissional
    # "secure_link_enabled": false,
    # "secure_link_key": "incididunt",
    # "secure_link_with_ip": true,
    # "ads_enabled": false,
    # "campaign_id": "irure o"

    # # If your LIVE plan is interprise
    # "catchup_enabled": false,
    # "catchup_period": 0,
    # "present_type": "manual",
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    print("Request was successful.")
    print(response.json())
else:
    print("Failed to make request: ", response.status_code, response.text)
