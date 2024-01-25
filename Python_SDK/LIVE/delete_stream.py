import requests

# URL of the API endpoint (replace "<stream-ID>" with the actual stream ID)
stream_id = "<stream-ID>"
url = f"https://napi.arvancloud.ir/live/2.0/streams/{stream_id}"

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
