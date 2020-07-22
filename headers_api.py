import requests
import os
from dotenv import load_dotenv
load_dotenv()

## Load API_KEY from .env
PROPUBLICA_API_KEY = os.getenv("PROPUBLICA_API_KEY")

## API Endpoint
version = 'v1'
API_ENDPOINT = f'https://api.propublica.org/congress/{version}/'
API_AUTH = {'X-API-Key':PROPUBLICA_API_KEY}

## Sample API Request to get all of the members of the 116th House of Representatives
congress = 116
chamber = 'house'
API_URL = f"{API_ENDPOINT}/{congress}/{chamber}/members.json"

## The documentation for this API says to include the authentication key in the headers.
## To do that, we make a dictionary and use the headers keyword
r = requests.get(API_URL,headers=API_AUTH)
# We get the data from the request using .json()
data = r.json()
# Here, we're getting a list of members using the documentation
# WE need to access a dictionary, then a list, then another dictionary
# This gives us a list of all members of the house
members = data['results'][0]['members']
for member in members:
    print(member['twitter_account'])
