import json
import requests
# Assuming the JSON string is stored in a variable called 'json_data'
json_string = '''
{
    "kind": "youtube#searchListResponse",
    "etag": "fF_FEnPurc32qw0-vrB9S0PlSfE",
    "nextPageToken": "CAUQAA",
    "regionCode": "IN",
    "pageInfo": {
        "totalResults": 23,
        "resultsPerPage": 5
    },
    "items": [
        {
            "kind": "youtube#searchResult",
            "etag": "zqFwbY1Ztoe8BGFZ_7GcN-QWmXo",
            "id": {
                "kind": "youtube#video",
                "videoId": "dZwbb42pdtg"
            },
            "snippet": {
                "publishedAt": "2024-01-08T16:03:11Z",
                "channelId": "UC9x0AN7BWHpCDHSm9NiJFJQ",
                "title": "3 Levels of WiFi Hacking",
                "description": "Get NordVPN 2Y plan + 4 months free here ➼ https://nordvpn.com/networkchuck It's risk-free with Nord's 30-day money-back...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/dZwbb42pdtg/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/dZwbb42pdtg/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/dZwbb42pdtg/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "NetworkChuck",
                "liveBroadcastContent": "none",
                "publishTime": "2024-01-08T16:03:11Z"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "oVxfeIayepPOOeSKa75jBnGhxA0",
            "id": {
                "kind": "youtube#playlist",
                "playlistId": "PLIhvC56v63IIJZRa3lzK6IeBQOH_VFjUQ"
            },
            "snippet": {
                "publishedAt": "2020-06-20T21:57:59Z",
                "channelId": "UC9x0AN7BWHpCDHSm9NiJFJQ",
                "title": "Learn Ethical Hacking (CEH Journey)",
                "description": "In this video series, I am learning to become a HACKER!! My first step is to earn the CEH certification (Certified Ethical Hacker)",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/yFC8pb2TPdc/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/yFC8pb2TPdc/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/yFC8pb2TPdc/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "NetworkChuck",
                "liveBroadcastContent": "none",
                "publishTime": "2020-06-20T21:57:59Z"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "-B8A5BLanJ2i7wAjRIbab4kTNzw",
            "id": {
                "kind": "youtube#video",
                "videoId": "80vIin4xGp8"
            },
            "snippet": {
                "publishedAt": "2020-12-06T02:46:46Z",
                "channelId": "UC9x0AN7BWHpCDHSm9NiJFJQ",
                "title": "let&#39;s hack your home network // FREE CCNA // EP 9",
                "description": "your home network can be HACKED!! Let's try. Ready to get your CCNA? Boson xmas sale (25% off) https://bit.ly/bosonccna2020...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/80vIin4xGp8/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/80vIin4xGp8/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/80vIin4xGp8/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "NetworkChuck",
                "liveBroadcastContent": "none",
                "publishTime": "2020-12-06T02:46:46Z"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "dZYbIKxB1aCToRCpb6ME_rmoo_I",
            "id": {
                "kind": "youtube#video",
                "videoId": "aOWr6rWhsIs"
            },
            "snippet": {
                "publishedAt": "2020-10-16T10:06:56Z",
                "channelId": "UCg08SXtXlfADk4yAODpShfQ",
                "title": "Hacking into Android in 32 seconds | HID attack | Metasploit | PIN brute force PoC",
                "description": "Samsung S7 is connected to Pixel as HID device (keyboard) that tries to brute force lock screen PIN (PoC) and then download,...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/aOWr6rWhsIs/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/aOWr6rWhsIs/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/aOWr6rWhsIs/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "Android Infosec",
                "liveBroadcastContent": "none",
                "publishTime": "2020-10-16T10:06:56Z"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "bUL8tC3vOoBkfx9gtnDNmD_0NiI",
            "id": {
                "kind": "youtube#video",
                "videoId": "t7Xib8kpcJ0"
            },
            "snippet": {
                "publishedAt": "2024-10-14T00:26:52Z",
                "channelId": "UCwhnuPCUapU3KHKb_Bfb4cg",
                "title": "Earn 0.2 HOT || Hot Wallet New Mission || What is BNB Chain || Hot Wallet New Video Code",
                "description": "Earn 0.2 HOT || Hot Wallet New Mission || What is BNB Chain || Hot Wallet New Video Code About video:- What is BNB Chain?",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/t7Xib8kpcJ0/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/t7Xib8kpcJ0/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/t7Xib8kpcJ0/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "Crypto kailash ",
                "liveBroadcastContent": "none",
                "publishTime": "2024-10-14T00:26:52Z"
            }
        }
    ]
}
'''
baseUrl = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=network_chuck_wifi_hacking&key=AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8"
jsonthing = str(requests.get(baseUrl).json())

json_data = json.loads(jsonthing)

# Extract the first title
first_title = json_data['items'][0]['snippet']['title']
channel = json_data['items'][0]['id']['videoId']

print(first_title, "https://www.youtube.com/watch?v="+channel)