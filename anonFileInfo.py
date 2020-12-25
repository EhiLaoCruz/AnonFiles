import requests

response = requests.get('https://api.anonfiles.com/v2/file/xxxxxx/info')
print(response.text)
#https://anonymfiles.com/docs/api