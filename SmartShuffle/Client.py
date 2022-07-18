from operator import indexOf
import creds
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# print(json.dumps(results, sort_keys=True, indent=4))

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=creds.client_id, client_secret=creds.client_secret))

while True:
    print("------------------------")
    print("WELCOME TO SMARTSHUFFLE")
    print("------------------------")
    print("(SmartShuffle improves on the current Spotify Shuffle algorithm to ensure all songs in a playlist are uniformly played)\n")
    print("0 - Search for a song")
    print("1 - Exit\n")
    choice = input("What do you want to do? ")

    if choice == "0":
        song = input("Search for a song: ")
        print()
        searchResults = spotify.search(song,10,0,"track")
        searchResults = searchResults['tracks']
        tracks = searchResults['items']

        for track in tracks:
            print(f"[{indexOf(tracks,track)+1}] SONG: {track['name']}")
            print(f"\tARTIST: {track['artists'][0]['name']}")
            print(f"\tALBUM: {track['album']['name']}\n")

    if choice == "1":
        break