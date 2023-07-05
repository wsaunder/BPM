import requests

"""
steps:
1. Start server.
2. Post for bearer token
3. Input Username
4. Get playlist ids and pick playlist
5. Get playlist total number of tracks then get tracks using limit offset 
6. Get track tempos
7. Set tempo range, filter step 6.
"""
#get token
'''
url = 'https://accounts.spotify.com/api/token'
 
headers = {"Content-Type": "application/x-www-form-urlencoded"}
params = {"Scope": "playlist-read-collaborative playlist-read-private"} 
data = "grant_type=client_credentials&client_id=CLIENTID&client_secret=CLIENTSECRET"

response = requests.post(url, headers=headers, data=data, params=params)
 
print("Status Code", response.status_code)
data = response.json()
print("access token: " + data["access_token"])
token = data["access_token"]
'''
token = "TOKEN"
#get playlist
user = "USER"
playlist_url = "https://api.spotify.com/v1/users/%s/playlists" % user
playlist_headers = {"Authorization": "Bearer " + token}
playlist = requests.get(playlist_url, headers=playlist_headers)
playlist_data = playlist.json()
print("Status Code ", playlist.status_code)
for items in playlist_data["items"]:
    print(items["id"] + " " + items["name"])
selected_playlist_id = "4gyoE77tvoFXtvMPwIBbjK"
track_requests_url = "https://api.spotify.com/v1/playlists/%s/tracks" % selected_playlist_id
tracks_request = requests.get(track_requests_url, headers=playlist_headers).json()
tracks = []
for items in tracks_request["items"]:
    print(items["track"]["name"])