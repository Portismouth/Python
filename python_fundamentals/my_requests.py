import requests

# raw_input("Enter your search: ")

url = 'https://api.spotify.com/v1/search'
token = "Bearer BQC-9jkJ2s51ckuropIJ_-lol6SGB3yBjYvCsjlf4D7Iv7MJAWyRFYRaQfSb7aG-PvYnnF1JA-3pJa2UnTXSAW4Mp-Jf0LV4tSdZ-YECqtVxhYpj1jESX5q79AeIpiRdWXzulQaRkWxz4r78VQ"

r = requests.get(url, headers={"Accept": "application/json", "Authorization": token})

print r.json()
