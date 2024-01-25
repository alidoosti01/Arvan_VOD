import requests

# URL of the API endpoint (replace "<video-ID>" with the actual ID)
video_id = "<video-ID>"
url = f'https://napi.arvancloud.ir/vod/2.0/videos/{video_id}/thumbnail'

# Headers including the Authorization key
headers = {
    'Authorization': 'apikey xxxxxxxxxxxxxxxxxxxx'
}

# File to be uploaded
files = {
    'thumbnail': ('filename.jpg', open('path/to/your/filename.jpg', 'rb'), 'image/jpeg')
}

# Make the POST request
response = requests.post(url, headers=headers, files=files)

# Check if the request was successful
if response.status_code == 201:
    print("File uploaded successfully.")
    print(response.json())
else:
    print("Failed to upload file: ", response.status_code, response.text)

# Close the file (important to prevent resource leakage)
files['thumbnail'][1].close()
