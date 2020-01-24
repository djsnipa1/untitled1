import requests
from requests.exceptions import ConnectionError
import json
import argparse


def shorten_url(url):
    try:
        response = requests.put("https://api.shorte.st/v1/data/url",
                                {"urlToShorten": url},
                                headers={"public-api-token": "651a15a69f687d5f878c2146e4be19b1"})

        api_response = json.loads(response.content)

        return {"status": api_response['status'],
                "shortenedUrl": api_response['shortenedUrl'],
                "message": "URL shortened successfully"}

    except ConnectionError:
        return {"status": "error",
                "shortenedUrl": None,
                "message": "Please ensure you are connected to the internet and shit"}


# Create a parser
parser = argparse.ArgumentParser(description='Shorten URLs in the terminal')

# Add argument
parser.add_argument('--url', default="google.com",
                    help="The URL to be shortened")
args = vars(parser.parse_args())
print(args)

if args.get('url'):
	print(shorten_url(args['url']))
