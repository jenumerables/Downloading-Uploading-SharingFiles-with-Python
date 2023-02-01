# Download a File with Python
import requests

# download mp3 from url
url = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"
req = requests.get(url)
content = req.content

# write binary file content to download.mp3
with open('download.mp3', 'wb') as file:
  file.write(content)
  print("File successfully downloaded")