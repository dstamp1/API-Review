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
# print(data['results'])
# members = data['results'][0]['members']
# for member in members:
#     for key in member:
#         print(f"{key}: {member[key]}")


# Challenge 1: Print all democrats and all republicans in two separate lists

# Challenge 2: Print all members of Congress with a twitter and facebook account


# Challenge 3: Identify all members from NY and print the one with the highest and lower dw_nominate score
### The dw_nominate scores have been used widely to describe the political ideology of political actors, political parties and political institutions.
### So, a score closer to 1 is described as conservative whereas a score closer to −1 can be described as liberal. Finally, a score at zero or close to zero is described as moderate


# Challenge 4: Print all members of Congress with an office in the Rayburn House Office Building

### Query a different endpoint
# https://projects.propublica.org/api-docs/congress-api/members/#get-recent-privately-funded-trips

API_ENDPOINT = f'https://api.propublica.org/congress/v1/{congress}/private-trips.json'
API_URL = API_ENDPOINT
r = requests.get(API_URL,headers=API_AUTH)
data = r.json()

# Challenge 6: Use the documentation to define a variable, trips, by parsing the data variable
# trips = data

# Challenge 7: Print the trips of all democrats and all republicans as two lists

# Challenge 8: Determine which member oof congress has taken the most trips

# Challenge 9: Determine the destination with the most number of visis

# Challenge 10: Determine the sponsor with the most number of trips to destinations in New York
