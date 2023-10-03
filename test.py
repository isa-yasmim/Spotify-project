import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import load_dotenv, dotenv_values

load_dotenv()

auth_manager = SpotifyClientCredentials(client_id = os.getenv("SPOTIPY_CLIENT_ID"), 
                                        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET"))

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks(5)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    
top_artists = sp.current_user_top_artists(limit=5, time_range='short_term')
for idx, item in enumerate(top_artists['items']):
    print(idx, item['name'])