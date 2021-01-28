import json
import requests
#the module below imports the id for the discover_weekly specifically, feel free to adjust to your own playlist
from secrets import spotify_user_id,  discover_weekly_id
from datetime import date
from refresh import Refresh

#for this example, i used the discover weekly playlist to showcase how to retrieve the playlist id
class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id = discover_weekly_id
        self.tracks = ""
        self.new_playlist_id = ""
#fill in the empty quotations above withthe id of the playlist you want to save

#the playlist id can be found by looking at the url of the page
    def find_songs(self):

        print("Finding songs in discover weekly...")
        # Loop through playlist tracks, add them to list

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)
        #the request pulls the authorization for the application so we can refresh the token in refresh.py
        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        print(response)
    #this adds/ copies the tracks to your new saved playlist
        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]
        #the uri is what the api uses to interepert since it contains the directory and can pass more information
        self.add_to_playlist()

    def create_playlist(self):
        # Create a new playlist
        print("Trying to create playlist...")
        today = date.today()

        todayFormatted = today.strftime("%d/%m/%Y")
        #sets up the playlist in the link provided
        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        #this part is not required, just optional if you would like to addd a description to your playlist for more personalization.
        request_body = json.dumps({
            "name": todayFormatted + " discover weekly", "description": "Discover weekly rescued once again from the brink of destruction by your friendly neighbourhood python script", "public": True
        })

        response = requests.post(query, data=request_body, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

        response_json = response.json()

        return response_json["id"]

    def add_to_playlist(self):
        # add all songs to new playlist
        print("Adding songs...")

        self.new_playlist_id = self.create_playlist()
        # the new playlist gets its own unique playlist id
        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.new_playlist_id, self.tracks)

        response = requests.post(query, headers={"Content-Type": "application/json",
                                                 "Authorization": "Bearer {}".format(self.spotify_token)})

        print(response.json)
    #below is the automation for getting the refresh token per expiration
    def call_refresh(self):

        print("Refreshing token")

        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.find_songs()


a = SaveSongs()
a.call_refresh()
