import requests
import os
from dotenv import load_dotenv
load_dotenv()

## Load API_KEY from .env
TASTEDIVE_API_KEY = os.getenv("TASTEDIVE_API_KEY")

## API Endpoint
API_ENDPOINT = f'https://tastedive.com/api/similar'

Media1="Red Hot Chili Peppers"
Media2="The Beatles"
## The documentation says we make a query by giving a list of Media separated by a comma
API_QUERY = f'q={Media1},+{Media2}'
## To include the key, the documentation tells us to pass it via a GET parameter in the URL
## GET Parameters follow the URL and a ? mark.
## Additional GET parameters are concatenated with a &
API_URL = f"{API_ENDPOINT}?k={TASTEDIVE_API_KEY}&{API_QUERY}"
r = requests.get(API_URL)

# We get the data from the request using .json()
data = r.json()
## Reading the documentation, we see we get back a dictionary
## Inside is another dictionary for our query Info + results
## And finally a list of dictionaries for our results
results = data['Similar']['Results']

for result in results:
    #Each result is a dictionary with keys Name and Type
    print(result)

# Challenge 1: Append the results to a list and count them

# Challenge 2: Update the query to include 'info'
# https://tastedive.com/read/api

# Challenge 3: Update the query to look up two tv shows and print the results

# Challenge 4: USe the info key to find recommended youtube videos and append to a list
