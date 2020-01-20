from urllib.parse import urlparse

import requests
import json
import urllib

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


# print("Your API provider: " + final_data)

links = data['linksByPlatform']
