from customtkinter import *
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
import os

# Function to get the video title from the YouTube page
def get_video_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_element = soup.find('title')
            if title_element:
                title = title_element.text.strip()
                cleaned_title = re.sub(r'\(.*?\)', '', title).strip()
                cleaned_title = re.sub(r' - YouTube$', '', cleaned_title).strip()
                return cleaned_title
            else:
                print("No title found on the page.")
                return None
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Function to get the video views
def get_video_views(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            view_count_element = soup.find('meta', attrs={'itemprop': 'interactionCount'})
            if view_count_element:
                views_text = view_count_element.get('content')
                cleaned_views = re.sub(r'\D', '', views_text).strip()
                return int(cleaned_views)
            else:
                print("No view count found on the page.")
                return None
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Function to check if a video is a YouTube Short
def is_short(video_id, api_key):
    try:
        video_details_url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={api_key}"
        response = requests.get(video_details_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            if items:
                content_details = items[0].get('contentDetails', {})
                duration = content_details.get('duration', '')

                # Convert ISO 8601 duration to seconds
                match = re.match(r'PT((\d+)M)?((\d+)S)?', duration)
                minutes = int(match.group(2)) if match.group(2) else 0
                seconds = int(match.group(4)) if match.group(4) else 0
                total_duration = minutes * 60 + seconds

                # Shorts are under 60 seconds
                return total_duration < 60
        return False
    except Exception as e:
        print(f"An error occurred while checking if video is a short: {str(e)}")
        return True  # Assume it's a Short if an error occurs

# Function to get the highest-viewed video
# Function to get the highest-viewed video
def get_video(input_query):
    api_key = 'AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8'  # Replace with your API key
    baseUrl = genURL(input_query)
    print(f"Generated URL: {baseUrl}")
    highestView = 0
    bestVideo = None

    response = requests.get(baseUrl)

    if response.status_code == 200:
        json_data = response.json()
        items = json_data.get('items', [])
        if items:
            for item in items:
                try:
                    videoID = item.get('id', {}).get('videoId')
                    if not videoID:
                        continue

                    # Check if the video is a Short
                    if is_short(videoID, api_key):
                        print(f"Skipping Shorts video: {videoID}")
                        continue

                    # Construct the embed URL
                    video_url = f"https://www.youtube.com/embed/{videoID}"
                    view_count = get_video_views(f"https://www.youtube.com/watch?v={videoID}")

                    # Print video details for debugging
                    print(f"Checking video: {video_url}, Views: {view_count}")

                    # Select video if it has more than 10,000 views and is most relevant so far
                    if view_count and view_count >= 10000:
                        bestVideo = video_url
                        break  # Stop at the first eligible video
                except Exception as e:
                    print(f"Error processing item: {str(e)}")
                    continue

            if bestVideo:
                print("\nSelected video: ", bestVideo)
                return bestVideo
        else:
            print("No items found in the JSON response.")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

    print("No eligible videos found.")
    return None

# Function to generate the YouTube API search URL
def genURL(input_query):
    # Generate a more concise query
    query = input_query.strip().replace(' ', '+')

    # Use the query directly without overly complicated transformations
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={encoded_query}&type=video&key=AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8"
    return url

# if __name__ == "__main__":
#     print("Enter the search query for the YouTube video:")
#     input_query = input("> ").strip()
#     if input_query:
#         print(f"Searching for videos related to: '{input_query}'")
#         highest_viewed_video = get_video(input_query)
#         if highest_viewed_video:
#             print(f"Selected video: {highest_viewed_video}")
#         else:
#             print("No videos found.")
#     else:
#         print("No query entered. Exiting.")
















app = CTk()
app.geometry('500x400')
app.title("Watch Selection")

def click():
    vid = input.get()
    input.delete(0, 'end')
    video = get_video(vid)

    comm = f"mpv {video}"

    os.system(comm)


input = CTkEntry(master=app, width=350, corner_radius=20)
text = CTkLabel(master=app, text="What do you want to watch?", font=('Helvetica', 30, 'bold'))
btn = CTkButton(master=app, text="click me", corner_radius=20, hover_color="#4682b4", command=click)



btn.place(relx=0.5, rely=0.75, anchor='center')
input.place(relx=0.5, rely=0.5, anchor='center')
text.place(relx=0.5, rely=0.3, anchor='center')




app.mainloop()