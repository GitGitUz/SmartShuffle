from website import creds
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# print(json.dumps(results, sort_keys=True, indent=4))

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET))

while True:
    print("------------------------")
    print("WELCOME TO SMARTSHUFFLE")
    print("------------------------")
    print("(SmartShuffle improves on the current Spotify Shuffle algorithm to ensure all songs in a playlist are uniformly played)\n")
    print("0 - Search for a song")
    print("1 - Exit\n")

    choice = input("What do you want to do? ")

    if choice == "0":
        song = input("Song Name: ")
        print()
        searchResults = spotify.search(song,10,0,"track")
        searchResults = searchResults['tracks']
        tracks = searchResults['items']
        pl = {
            "id": "5",
            "tracks": []
        }
        for track in tracks:

            # WILL ONLY DO THIS FOR THE ONE ADDED TO PLAYLIST
            temp = {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "id": track['id'],
                "url": track['external_urls']['spotify']
            }

            pl["tracks"].append(temp)

        print(json.dumps(pl, indent=3))
        print(type(json.dumps(pl)))
        print(json.loads(json.dumps(pl['tracks'], indent=3)))
        # print(json.dumps((pl['tracks'][0]), indent=3))
        # print(type(json.loads((json.dumps(pl)))))


    if choice == "1":
        break