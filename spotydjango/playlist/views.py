from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="d2734d61db194aec983f37790ccaf643",
                                               client_secret="4aec1ba661014bb29fba8615bd5ebd1e",
                                               redirect_uri="http://localhost:8000/callback",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
track_dict = {}
for idx, item in enumerate(results['items']):
    track = item['track']
    track_dict[track['artists'][0]['name']] = track['name']
print (track_dict)

def index(request):
    return render(request, 'index.html', track_dict = track_dict)

