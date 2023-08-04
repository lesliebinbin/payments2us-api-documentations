import requests, yaml

url = "https://api.addressfinder.io/api/nz/address/autocomplete/"

payload = {}
headers = {}

with open("../../.secrets.yml") as f:
    secrets = yaml.safe_load(f)
    params = {
        "key": secrets["address_finder"]["key"],
        "secret": secrets["address_finder"]["secret"],
        "q": "184 will",
        "format": "json",
    }

response = requests.get(url, headers=headers, data=payload, params=params)

print(response.text)
