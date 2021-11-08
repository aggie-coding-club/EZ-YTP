import requests

params = (
    ('async', 'false'),
)

files = {
    'audio': ('words.mp3', open('test_files/words.mp3', 'rb')),
    'transcript': ('words.txt', open('test_files/words.txt', 'rb')),
}

response = requests.post('http://localhost:49153/transcriptions', params=params, files=files)

body = response.json()

print(body)
