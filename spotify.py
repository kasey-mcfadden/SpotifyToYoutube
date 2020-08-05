import os
import json
import configparser
import spotipy

config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
redirect_uri = config.get('SPOTIFY', 'REDIRECT_URI')
username = config.get('SPOTIFY', 'USERNAME')

scope = "user-library-read"

# Authenticate and return Spotify object
def auth():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        show_dialog=True,
        username=username
    )
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    return sp

# Grab a list of user's Spotify playlists
def get_playlists(sp):
    results = sp.user_playlists(username)
    for i, item in enumerate(results['items']):
        print("%d %s" % (i, item['name']))
    return results

# Grab track names of all songs within Spotify plist
def get_tracks(sp, playlist_id):
    results = sp.playlist(playlist_id)
    playlist_name = results['name']
    print("\n\n%s:\n" % playlist_name)

    tracks = []

    for item in results['tracks']['items']:
        track = item['track']
        name = track['name']
        artist = track['artists'][0]['name']
        track_string = "%s - %s" % (artist, name)
        print(track_string)
        tracks.append(track_string)

    return tracks, playlist_name

def main():
    sp = auth()
    playlists = get_playlists(sp)
    playlist_number = int(input("Enter the above number \
of the playlist you would like to convert:\n"))
    playlist_id = playlists['items'][playlist_number]['uri']
    tracks, playlist_name = get_tracks(sp, playlist_id)

if __name__ == "__main__":
    main()

