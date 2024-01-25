import requests

# URL of the API endpoint
url = 'https://napi.arvancloud.ir/vod/2.0/channels'

# Headers including the Authorization with your API key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data: ", response.status_code)
