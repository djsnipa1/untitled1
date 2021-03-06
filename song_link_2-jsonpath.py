from urllib.parse import urlparse

import requests
import json
import urllib
from jsonpath_ng import jsonpath_ng, parse


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

# spotify = data['entitiesByUniqueId']
spotify = data['linksByPlatform']

# print(spotify)

for item in spotify:
  print(item)
  # for thing in item:
  #   print(thing)

for thing in item:
  print(thing)

jsonpath_expr = parse('linksByPlatform[*]')

print(jsonpath_expr)