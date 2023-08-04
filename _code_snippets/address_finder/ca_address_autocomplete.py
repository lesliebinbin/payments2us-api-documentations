import requests, yaml

url = "https://api.addressfinder.io/api/ca/address/v2/autocomplete/"

payload = {}
headers = {}

with open("../../.secrets.yml") as f:
    secrets = yaml.safe_load(f)
    params = {
        "key": secrets["address_finder"]["key"],
        "secret": secrets["address_finder"]["secret"],
        "q": "233 Vancouver St N5W",
        "format": "json",
    }

response = requests.get(url, headers=headers, data=payload, params=params)

print(response.text)
