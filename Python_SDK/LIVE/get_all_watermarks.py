import requests

# URL of the API endpoint
url = 'https://napi.arvancloud.ir/live/2.0/watermarks'

# Headers including the Authorization key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    print(response.json())
else:
    print("Failed to make request: ", response.status_code, response.text)
