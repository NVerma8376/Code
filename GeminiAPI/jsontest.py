import urllib.parse
import requests

# setting the base URL value
baseUrl = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=network_chuck_wifi_hacking&key=AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8"

json_data = requests.get(baseUrl).json()
Final_result = json_data['kind']

print(Final_result)