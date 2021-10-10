import spotipy
import pprint
import scrapeTokboard
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

pp = pprint.PrettyPrinter(indent=4)

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

os.system("SET SPOTIFY_CLIENT_ID="+SPOTIFY_CLIENT_ID)
os.system("SET SPOTIPY_CLIENT_SECRET="+SPOTIFY_CLIENT_SECRET)
os.system("SET SPOTIPY_REDIRECT_URI=' http://example.com'")

scope = "user-library-read playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

final_list = scrapeTokboard.scrapeTokboard()
pp.pprint(final_list)
tracks = []
for key, value in final_list.items():
    try:
        name = key
        track = value
        pp.pprint("Trying to find song " + value + " by " + key)
        results = sp.search(q='artist:' + key + " track:" + value, type='track')
        pp.pprint(results['tracks']['items'][0]['id'])
        tracks.append(results['tracks']['items'][0]['id'])
    except:
        print("No match for artist " + key + " track: " + value)
        continue

pp.pprint(tracks)

track_list = ["spotify:track:" + track for track in tracks]
sp.playlist_replace_items(playlist_id='spotify:playlist:1qTk48mGiRpAhKyionVhEl',items=track_list)

print("Playlist Updated!")
