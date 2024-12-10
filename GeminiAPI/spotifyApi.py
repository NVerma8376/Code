import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pygame
import sys

# Set up Spotify OAuth
scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Initialize Pygame
pygame.init()

# Function to load track
def load_track(track_id):
    return sp.track(track_id)

# Function to play track
def play_track(track):
    pygame.mixer.music.load(track['preview_url'])
    pygame.mixer.music.play()

# Main function
def main():
    print("Welcome to the Spotify Liked Songs Player!")
    print("1. Play a liked song")
    print("2. Quit")

    while True:
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            # Get liked tracks
            liked_tracks = sp.current_user_saved_tracks(limit=20)
            
            # Print options
            print("\nOptions:")
            for i, item in enumerate(liked_tracks['items']):
                print(f"{i}: {item['track']['name']}")

            # Get user input
            choice = input("Enter track number to play, or 'q' to quit: ")

            if choice.lower() == 'q':
                break
            
            try:
                choice = int(choice)
                if 0 <= choice < len(liked_tracks['items']):
                    track_id = liked_tracks['items'][choice]['track']['id']
                    track = load_track(track_id)
                    play_track(track)
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input")

        elif choice == '2':
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
