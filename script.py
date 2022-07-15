
#import statements
import requests, json

url = "https://api.apollo.io/api/v1/people/bulk_match"

data = {
    "api_key": "z2FzoyGx4LCYPSz9g5iscw",
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

with open("output.json", 'w+') as outfile:
    json.dump(response.json(), outfile)

print(response.text)
