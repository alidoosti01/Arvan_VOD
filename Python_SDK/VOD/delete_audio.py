import requests

# URL of the API endpoint (replace "<AUDIO-ID>" with the actual audio ID)
audio_id = "<AUDIO-ID>"
url = f"https://napi.arvancloud.ir/vod/2.0/audios/{audio_id}"

# Headers including the Authorization
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxx'
}

# Make the DELETE request
response = requests.delete(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully deleted.")
else:
    print("Failed to delete: ", response.status_code, response.text)
