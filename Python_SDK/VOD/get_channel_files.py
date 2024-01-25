import requests

# URL of the API endpoint (replace "<CHANNEL-ID>" with the actual channel ID)
channel_id = "<CHANNEL-ID>"
url = f"https://napi.arvancloud.ir/vod/2.0/channels/{channel_id}/files"

# Headers including the Authorization key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    print(response.json())
else:
    print("Failed to make request: ", response.status_code, response.text)
