import requests

response = requests.get('https://api.anonfiles.com/v2/file/vfycn301p8/info')
print(response.text)