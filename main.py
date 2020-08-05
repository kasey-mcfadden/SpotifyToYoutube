import spotify
import youtube

def main():
    sp = spotify.auth()
    yt = youtube.auth()

    playlists = spotify.get_playlists(sp)
    playlist_number = int(input("Enter the above number \
of the playlist you would like to convert:\n"))
    playlist_id = playlists['items'][playlist_number]['uri']
    tracks, playlist_name = spotify.get_tracks(sp, playlist_id)

    playlistId = youtube.createPlaylist(yt, playlist_name)
    print("\n\n\n\nAdding songs...")
    for track in tracks:
        videoId = youtube.search(yt, track)
        response = youtube.insertIntoPlaylist(yt, playlistId, videoId)
        vid_title = response['snippet']['title']
        print("%s added to playlist ✓" % vid_title)

    print('Playlist "%s" created!' % playlist_name)
    link = "https://www.youtube.com/playlist?list=" + playlistId
    print("Link:\n%s" % link)

if __name__ == "__main__":
    main()

