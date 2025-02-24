import requests, pprint

params = {
    "rocket_name" : "starship"
}

response = requests.get("https://api.spacexdata.com/v3/rockets", params=params)
print(response)
pprint.pprint(response.json())
pprint.pprint(response.request)

