
#import statements
import os, requests, json
from dotenv import load_dotenv
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APOLLO_API_KEY = os.environ.get("APOLLO_API_KEY")

url = "https://api.apollo.io/api/v1/people/bulk_match"

#----Sample data
data = {
    "api_key": APOLLO_API_KEY,
    "details": [
        {
            "first_name": "Tim",
            "last_name": "Zheng",
            "domain": "apollo.io",
            "email": "tim@apollo.io",
            "organization_name": "Apollo"
        },
        {
            "first_name": "Roy",
            "last_name": "Chung",
            "email": "roy@apollo.io",
            "organization_name": "Apollo"
        }
    ]
}

headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=data)


# Dump output for testing
with open("output.json", 'w+') as outfile:
    json.dump(response.json(), outfile)

#print(response.text)
