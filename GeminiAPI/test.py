import os
import google.generativeai as genai
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_video_link(response):
    lines = response.split('\n')
    video_link = None
    
    # Look for a line that starts with "Video Link:"
    for line in lines:
        if line.startswith("Video Link:"):
            video_link = line.split(':', 1)[1].strip()
            break
    
    # If no link found, try to find a URL at the end of the response
    if video_link is None:
        url_pattern = r'https?://\S+'
        matches = re.findall(url_pattern, response)
        if matches:
            video_link = matches[-1]
    
    return video_link

def chat_with_youtube():
    api_key = "AIzaSyAMXbP_qGecWXVLkq4K0nMhKPZxfOOFAkw"
    if not api_key:
        logger.error("API key not found. Please set GEMINI_API_KEY environment variable.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat()

    def get_chat_response(prompt):
        try:
            response = chat.send_message(prompt)
            logger.info(f"Response received: {response.text}")
            return response.text
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            return f"An error occurred while processing your request."

    # Start the chat loop
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "quit":
            break
        
        # Generate the response
        response = get_chat_response(user_input)
        
        # Extract the answer and video link
        lines = response.split('\n')
        answer = '\n'.join(lines[:-1])
        video_link = extract_video_link(response)
        
        # Print the response
        print(f"AI: {answer}")
        print(f"Video Link: {video_link}")
        print("---")

if __name__ == "__main__":
    chat_with_youtube()
