import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv('SPOTIPY_ID'),client_secret=os.getenv('SPOTIPY_SEC')))

def search_artist(artist_name):
    results = spotify.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
    return artist    

def top_tracks(artist_id):
    results = spotify.artist_top_tracks(artist_id)
    tracklist = []
    for track in results['tracks'][:10]:
        tracklist.append(track)
    return tracklist