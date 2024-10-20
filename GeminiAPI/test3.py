import json
import requests

# setting the base URL value
baseUrl = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=network_chuck_wifi_hacking&key=AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8"

json_data = requests.get(baseUrl).json()


# Open the JSON file for reading
with open('json.json', 'r') as file:
    # Parse JSON data
    data = json.load(file)



file = data['items']

# Loop through the array and print each city name
for items in file:
    print(items['items'])