# API-Review

## Purpose
In this lab, you'll learn how to incorporate an API key into an API request. You'll sign up for ProPublica's Congress API service [here](https://www.propublica.org/datastore/api/propublica-congress-api) to learn how to use a service that uses headers to send the key and you'll sign up for TasteDive's API service [here](https://tastedive.com/)

## Setup
After templating and cloning the lab, you will `touch .env && cloudshell open .env` so you can add your environment variables to include the API key.
```
PROPUBLICA_API_KEY = ''
TASTEDIVE_API_KEY = ''
```

## Directions
You'll work through the steps in `api.py` and practice making calls to the API and writing Python control flow to process the data. Use the API documentation https://projects.propublica.org/api-docs/congress-api/ and https://tastedive.com/read/api
