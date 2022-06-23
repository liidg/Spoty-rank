from django.db import models
from django.forms import ImageField

# Create your models here.
# class for userplaylist still in progress
class userSavedTracks:
    id: int
    nameAlbum: str
    nameTrack: str
    popularity: int
    image: ImageField
