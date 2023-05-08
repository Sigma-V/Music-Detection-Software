import requests
api_key='fae375fabd85c09a46c4405b106b88dd'

def suggest(app):
    link = f"http://ws.audioscrobbler.com/2.0/?method=album.search&album={app}&api_key={api_key}&format=json"
    data = requests.get(link)
    data = data.json()
    for i in data["results"]["albummatches"]["album"]:
        print(i["name"],i["url"])