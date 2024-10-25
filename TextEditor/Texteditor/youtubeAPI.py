import requests
import json
import VideoSearch
import ViewCount as test2
# Base URL for YouTube API search
def get_video(input1):
    baseUrl = VideoSearch.genURL(input1)
    print(baseUrl)
    viewList = []
    highestView = 0
    currentView = 0
    highestViewVideo = ""

    #baseUrl = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=python_bubble_sort&key=AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8"

    # Make GET request to the API endpoint
    response = requests.get(baseUrl)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()
        
        # Extract the first title
        items = json_data['items']
        if items:
            i = 0
            for item in items:


                try:
                    first_item = items[i]
                    snippet = first_item['snippet']
                    first_title = snippet['title']
                    videoID1 = first_item['id']
                    
                    if 'videoId' not in videoID1:
                        i+=1
                        continue

                    if 'videoId' in videoID1:
                        video_url = videoID1['videoId']
                    
                    else:
                        i+=1
                    
                except:
                    print("Error extracting data from the JSON response.")
                    break

                i+=1

                try:
                    video = f"https://www.youtube.com/watch?v={video_url}"
                except:
                    print("Error extracting video URL.")
                    break

                view = test2.get_video_views(video)
                
                if view > highestView:
                    highestView = view
                    highestViewVideo = video

                viewList.append(view)

                
            else:
                print("No items found in the JSON response.")

            print("")
            print("Highest view video: ", highestViewVideo)
            print("Highest view count: ", highestView)
            print("")
            
            return highestViewVideo
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
