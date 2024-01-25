import requests

# URL of the API endpoint
period = "<CHANGE-ME>" # Requird , Values: 1h,3h,6h,12h,24h,7d,30d
url = f'https://napi.arvancloud.ir/live/2.0/report/visitors?period={period}'

# Headers including the Authorization key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    print(response.json())
else:
    print("Failed to make request: ", response.status_code, response.text)
