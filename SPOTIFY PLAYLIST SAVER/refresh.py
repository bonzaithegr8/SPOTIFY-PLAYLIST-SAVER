from secrets import refresh_token, base_64
import requests
import json
#importing spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Refresh:

    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):
        #the link which spotify api provides for the refresh token
        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refresh_token},
                                 headers={"Authorization": "Basic " + base_64})

        response_json = response.json()
        print(response_json)

        return response_json["access_token"]

#theis will simply run the code and refresh the token
a = Refresh()
a.refresh()
