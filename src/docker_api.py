import requests

params = (
    ('async', 'false'),
)

files = {
    'audio': ('words.mp4', open('test_files/words.mp4', 'rb')),
    'transcript': ('words.txt', open('test_files/words.txt', 'rb')),
}

response = requests.post('http://localhost:8765/transcriptions', params=params, files=files)

body = response.json()

print(body)
