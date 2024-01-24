import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint


def get_user_sp_id(sp):
    user_data = sp.current_user()
    return user_data['id']


def main():
    load_dotenv()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = 'http://example.com/'
    scope = "playlist-modify-private"

    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        username='Dcomputer23',
        cache_path='token.txt'
    )
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)

    date = input("What year will you like to travel into? 🚀 Type in this format YYYY-MM-DD: ")
    url = "https://www.billboard.com/charts/christian-songs/"
    response = requests.get(url + date)

    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_div = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_div]

    redirect_response = input("Please enter the URL you were redirected to: ")
    token_info = sp_oauth.get_access_token(redirect_response)

    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

    sp = spotipy.Spotify(auth=token_info["access_token"])
    if token_info:
        user_id = get_user_sp_id(sp)
    else:
        print("Error obtaining access token.")

    year = date.split('-')[0]
    songs_uris = []
    for songs in song_names:
        output = sp.search(q=f"track:{songs} year:{year}", type="track")
        try:
            uri = output["tracks"]['items'][0]['uri']
            songs_uris.append(uri)

        except IndexError:
            print(f"'{songs}', does not exist in Spotify. Ignored.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    pprint.pprint(playlist)
    sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)


if __name__ == '__main__':
    main()

