import requests
from bs4 import BeautifulSoup
import re

def get_video_title(url):
    try:
        # Send a GET request to the YouTube page
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the title element
            title_element = soup.find('title')
            
            if title_element:
                # Extract the title text
                title = title_element.text.strip()
                
                # Remove any extra characters like "(Official)" or " - YouTube"
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

def get_video_views(url):
    try:
        # Send a GET request to the YouTube page
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the view count element using a more flexible selector
            view_count_element = soup.find('meta', attrs={'itemprop': 'interactionCount'})
            
            if view_count_element:
                # Extract the view count text
                views_text = view_count_element.get('content')
                
                # Remove any extra characters like "views"
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
    
