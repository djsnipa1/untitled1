from urllib.parse import urlparse

import requests
import json
import urllib
from dictor import dictor

main_api = "https://api.song.link/v1-alpha.1/links?" 

address = "https://open.spotify.com/album/2SlS6cdEVoFjkpTUdBbpij?si=somT0Zg0S7yoVBy1rm6gpg"

# url = main_api + urllib.parse.urlencode({"url": address})

# json_data = requests.get(url).json()


def get_songlink(address):
  # try:
  url = main_api + urllib.parse.urlencode({"url": address})

  json_data = requests.get(url).json()

  # return json_data


  print(json_data)


get_songlink('https://open.spotify.com/album/2SlS6cdEVoFjkpTUdBbpij')