# SpotifyToYoutube
Convert Spotify Playlists to YouTube Playlists

## Dependencies

```
pip install configparser
pip install google-api-python-client
pip install google-auth-oauthlib
pip install spotipy
```

## Authentication

Create and modify a `config.cfg` file in the same directory:
```
[SPOTIFY]
CLIENT_ID = YOUR_CLIENT_ID
CLIENT_SECRET = YOUR_CLIENT_SECRET
REDIRECT_URI = http://localhost/
USERNAME = YOUR_USERNAME
```

Have your `CLIENT_SECRET_FILE.json` file saved in the same directory. You can download this OAuth Client ID file from the [Google Developer Console](https://console.developers.google.com/apis/credentials). Make sure to select Desktop App as the Application Type.

## Usage

`python main.py`
