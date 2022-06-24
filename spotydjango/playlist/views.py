from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse
from .models import userSavedTracks

#we import the spotipy api then get the current user saved tracks
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def index(request):
    return render(request, 'index.html')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="d2734d61db194aec983f37790ccaf643",
                                               client_secret="4aec1ba661014bb29fba8615bd5ebd1e",
                                               redirect_uri="http://localhost:8000/callback",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
trackList = []
counter=0
#this for help us to get the las 20 current user saved tracks
for idx, item in enumerate(results['items']):
    track = item['track']
    tracks = userSavedTracks()
    tracks.id = idx
    tracks.nameAlbum = track['album']['name']
    tracks.nameTrack = track['name']
    tracks.popularity = track['popularity']
    tracks.image = track['album']['images'][0]['url']
    trackList.append(tracks)
    counter += track['popularity']
#print(counter)
#print(counter/len(trackList))


def playlist(request):
    return render(request, 'playlist.html', {'trackList': trackList})

    


