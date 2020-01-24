#!/usr/bin/env python3

import requests
from requests.exceptions import ConnectionError
import json
import argparse
# /api/url/geturls

# /api/url/submit


def shorten_url(url):
  """ Shorten URL """
  try:
    response = requests.post("https://kutt.it/api/url/submit",
                             {"target": url,
                              "reuse": True,
                              "customurl": ""},
                             headers={"X-Api-Key": "u1G0A6H4eemePo_sd1gelQm5s8VSSMjK1sLfwW2q"})

    api_response = json.loads(response.content)
    
    # Pretty print json return data
    pretty = json.dumps(api_response, indent=4)
    print(pretty)
    
    return {"created_at": api_response['created_at'],
            "shortUrl": api_response['shortUrl'],
            "message": "URL shortened successfully"}

  except ConnectionError:
    return {"created_at": "error",
            "shortUrl": None,
            "message": "Please make sure you are connected to the internet"}


# shorten_url("google.com")

# Create a parser
parser = argparse.ArgumentParser(description='Shorten URLs in the terminal')

# Add argument
parser.add_argument('--url', default="google.com",
                    help="The URL to be shortened")
# print(args)

# if args.get('url'):
#   print(shorten_url(args['url']))


def handle_output(result):
  """ Function to format and print the output """
  if result["created_at"] != "ok":
    print(f"{result['message']}. Your shortened URL is:\n"
          f"\t{result['shortUrl']}")
  elif result["created_at"] == "error":
    print(f"{result['message']}")


args = vars(parser.parse_args())

if args.get('url'):
  result = shorten_url(args['url'])
  handle_output(result)


# Get a list of URLs
def get_urls():
  """ Get a list of URLs """
  response = requests.get("https://kutt.it/api/url/geturls",
                          headers={"X-Api-Key": "u1G0A6H4eemePo_sd1gelQm5s8VSSMjK1sLfwW2q"})

  api_response = json.loads(response.content)

  print(api_response)

  return api_response


"""

get_urls()

urllist = get_urls()

pretty = json.dumps(urllist, sort_keys=True, indent=4)

print(pretty)

"""
