import random
import json
import itertools
from operator import itemgetter

#groups songs in a playlist by their artist
def groupPlaylistSongs(playlist):
    playlist = sorted(playlist, key=itemgetter('artist'))
    grouped_playlist = []
    for key, group in itertools.groupby(playlist, key=itemgetter('artist')):
        group_as_list = list(group)
        print(f"ARTIST:[{key}] - {[s['name'] for s in group_as_list]}")
        print("--------------------")
        grouped_playlist += [[s for s in group_as_list]]
    return grouped_playlist

#a simple Fisher-Yates shuffle algorithm to be used within each category
def fyShuffle(arr):
    last_idx = len(arr)-1
    while last_idx > 0:
        rand_idx = random.randint(0, last_idx)
        temp = arr[last_idx]
        arr[last_idx] = arr[rand_idx]
        arr[rand_idx] = temp
        last_idx -=1
    return arr

#shuffles playlist that has already been grouped by artist for each song
def spotifyShuffle(playlist):
    playlist = groupPlaylistSongs(playlist)
    items = []
    v = []
    for artist_songs in range(len(playlist)):
        # print("Group: ", artist_songs)
        # print("-----------------------")
        # print(json.dumps(playlist[artist_songs], indent=3))
        items += fyShuffle(playlist[artist_songs])
        n = len(playlist[artist_songs])
        initialOffset = random.uniform(0,1/n)
        randomOffset = [random.uniform(-0.1/n, 0.1/n) for k in range(n)]
        playsOffset= [random.uniform(-1/(playlist[artist_songs][k]['plays'] if playlist[artist_songs][k]['plays'] > 0 else 1), 0) for k in range(n)]
        print(playsOffset)
        v += [k/n + initialOffset + randomOffset[k] + playsOffset[k] for k in range(n)]
    
    #sort items by positional vector
    shuffled = [s[1] for s in sorted(zip(v,items))]
    return shuffled    

# playlist4 = [{"artist": "Travis Scott", "name": "90210"},{"artist": "Linkin Park", "name": "In The End"},{"artist": "The Weeknd", "name": "Gasoline"},{"artist": "Linkin Park", "name": "Crawling"},{"artist": "The Weeknd", "name": "Starboy"},{"artist": "Linkin Park", "name":  "Numb"},{"artist": "The Weeknd", "name": "The Hills"}]