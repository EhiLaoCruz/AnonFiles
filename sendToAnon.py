import requests

files = {
    'file': ('test.txt', open('test.txt', 'rb')),
}

response = requests.post('https://api.anonfiles.com/upload', files=files)

print(response.text)

#https://anonymfiles.com/docs/api