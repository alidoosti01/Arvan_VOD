import requests
import json

# API endpoint URL
url = 'https://napi.arvancloud.ir/vod/2.0/channels'

# Headers including Content-Type and Authorization
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Data to be sent in POST request
data = {
    "title": "<string>",  # required
    "description": "<string>"

    # # If you want
    # "secure_link_enabled": "<boolean>",
    # "secure_link_key": "<string>",
    # "secure_link_with_ip": "<boolean>" ,

    # # If your VOD plan is growth
    # "ads_enabled": "<boolean>",
    # "present_type": "<string>",
    # "campaign_id": "<string>"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    # Parse and print JSON response
    print(response.json())
else:
    print("Failed to post data: ", response.status_code, response.text)
