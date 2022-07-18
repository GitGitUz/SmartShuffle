import random
import itertools

#groups songs in a playlist by their artist
def groupPlaylistSongs(playlist):
    grouped_playlist = []
    key_func = lambda song:song['artists'][0]['name']
    for key, group in itertools.groupby(playlist, key_func):
        group_as_list = list(group)
        print(f"ARTIST: {key} - {[s[1]['name'] for s in group_as_list]}")
        grouped_playlist += [[s[1] for s in group_as_list]]
    return grouped_playlist

#testing version of grouping method
def groupPlaylistSongsTEST(playlist):
    print("\n", playlist, "\n")
    grouped_playlist = []
    key_func = lambda song:song[0]
    for key, group in itertools.groupby(playlist, key_func):
        group_as_list = list(group)
        print(f"ARTIST: {key} - {[s[1] for s in group_as_list]}")
        grouped_playlist += [[s[1] for s in group_as_list]]
    print("\nGP: ", grouped_playlist)
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

#shuffles playlist that has already been grouped by songs for each artist
def spotifyShuffle(playlist):
    items = []
    v = []
    for artist_songs in range(len(playlist)):
        items += fyShuffle(playlist[artist_songs])
        n = len(playlist[artist_songs])
        initialOffset = random.uniform(0,1/n)
        randomOffset = [random.uniform(-0.1/n, 0.1/n) for k in range(n)]
        v += [k/n + initialOffset + randomOffset[k] for k in range(n)]
    
    #sort items by positional vector
    shuffled = [s[1] for s in sorted(zip(v,items))]
    # temp = sorted(zip(v,items))
    return shuffled

playlist1 = [["Numb", "In The End", "Crawling", "Papercut"],["The Hills", "Starboy"],["Power", "Runaway", "Jail", "Jesus Walks", "Heartless"], ["Sicko Mode"]]
playlist2 = [["LP1", "LP2", "LP3", "LP4"],["TW1", "TW2"],["KW1", "KW2", "KW3", "KW4", "KW5"], ["TS1"]]
playlist3 = [["Travis Scott", "90210"],["Travis Scott", "Goosebumps"],["Linkin Park", "Numb"],["Linkin Park", "In The End"],["Linkin Park", "Crawling"],["The Weeknd", "Gasoline"],["The Weeknd", "Starboy"],["The Weeknd", "The Hills"]]
groupPlaylistSongsTEST(playlist3)
print()
print(spotifyShuffle(groupPlaylistSongsTEST(playlist3)))