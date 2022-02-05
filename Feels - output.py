import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id='d732ba776cb54bf681ec10673a7dfe5f', client_secret='af80ba1c481f48d69ffbebb817dfcdcc')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def make_lists(s):
    out = []
    tmp = sp.category_playlists(s,'GB',5,0)
    links = tmp['playlists']['items']
    for link in links:
        out.append(link['external_urls']['spotify'])
    return out

def get_playlist(s):
    tmp = emotions[s]
    return tmp[random.randint(0,len(tmp)-1)]

pop_l = make_lists('pop')
blues_l = make_lists('blues')
chill_l = make_lists('chill')
rnb_l = make_lists('rnb')
funk_l = make_lists('funk')

emotions = {"happy":pop_l,
            "sad":blues_l,
            "angry":chill_l,
            "fear":rnb_l,
            "surprise":funk_l,
            }

s = "surprise"

print(get_playlist(s))


