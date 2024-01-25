import requests

# URL of the API endpoint (replace "<video-ID>" with the actual video ID)
video_id = "<video-ID>"
url = f"https://napi.arvancloud.ir/vod/2.0/videos/{video_id}/thumbnail"

# Headers including the Authorization key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    print(response.json())
else:
    print("Failed to make request: ", response.status_code, response.text)