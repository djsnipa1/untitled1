from urllib.parse import urlparse

import requests
import json
import urllib
from dictor import dictor

main_api = "https://api.song.link/v1-alpha.1/links?"

address = "https://open.spotify.com/album/2SlS6cdEVoFjkpTUdBbpij?si=somT0Zg0S7yoVBy1rm6gpg"

url = main_api + urllib.parse.urlencode({"url": address})

json_data = requests.get(url).json()

# pretty = json.dumps(json_data, indent=4, sort_keys=False)

# print(pretty)

with open('json.json') as f:
  data = json.load(f)

pretty = json.dumps(data, indent=2, sort_keys=True)

# print(pretty)
final_data = []
# spotify = data['entitiesByUniqueId']
# entities = data['entitiesByUniqueId'].values()
entities = data['linksByPlatform']

# for services in entities:
#   print(services)
print(entities)

for key in entities:
  # entities[value]['apiProvider']
  list_platforms = key
  # print(entities[value]['apiProvider'])
  # print(value)
  # final_data.update(list_platforms)
  print(list_platforms)

spotify_url = dictor(data, 'linksByPlatform.spotify.url')
applemusic_url = dictor(data, 'linksByPlatform.appleMusic.url')
pandora_url = dictor(data, 'linksByPlatform.pandora.url')
deezer_url = dictor(data, 'linksByPlatform.deezer.url')
amazonmusic_url = dictor(data, 'linksByPlatform.amazonMusic.url')
tidal_url = dictor(data, 'linksByPlatform.tidal.url')
yandex_url = dictor(data, 'linksByPlatform.yandex.url')
itunes_url = dictor(data, 'linksByPlatform.itunes.url')
amazonstore_url = dictor(data, 'linksByPlatform.amazonStore.url')


print('spotify_url = ' + spotify_url)
print('appleMusic_url = ' + applemusic_url)
print('pandora_url = ' + pandora_url)
print('deezer_url = ' + deezer_url)
print('amazonmusic_url = ' + amazonmusic_url)
print('tidal_url = ' + tidal_url)
print('yandex_url = ' + yandex_url)
print('itunes_url = ' + itunes_url)
print('amazonstore_url - ' + amazonstore_url)

# print("Your API provider: " + final_data)

links = data['linksByPlatform']
