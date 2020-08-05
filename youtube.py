import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Disable OAuthlib's HTTPS verification when running locally.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "CLIENT_SECRET_FILE.json"

# Get credentials and create an API client
def auth():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    yt = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    return yt

# Create YouTube playlist with title
def createPlaylist(yt, title):
    request = yt.playlists().insert(
        part="snippet",
        body={
          "snippet": {
            "title": title
          }
        }
    )
    response = request.execute()
    playlistId = response['id']
    return playlistId

# Query YouTube for song, grab first video
def search(yt, query):
    request = yt.search().list(
        part="snippet",
        maxResults=1,
        q=query
    )
    response = request.execute()
    videoId = response['items'][0]['id']['videoId']
    return videoId

# Insert video into playlist
def insertIntoPlaylist(yt, playlistId, videoId):
    request = yt.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": playlistId,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": videoId
            }
          }
        }
    )
    response = request.execute()
    return response

def main():
    query = "Bill Withers - Lovely Day"
    yt = auth()
    playlistId = createPlaylist(yt, title)
    videoId = search(yt, query)
    insertIntoPlaylist(yt, playlistId, videoId)

if __name__ == "__main__":
    main()

