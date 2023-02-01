# Share a file with Python and Filestack
from filestack import Client

api_key = ""

client = Client(api_key)
new_link = client.upload(filepath='file.txt')

print(new_link.url)