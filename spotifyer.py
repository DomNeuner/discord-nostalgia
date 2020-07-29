import spotipy
import spotipy.util as util
import os
from dotenv import load_dotenv

load_dotenv() # specifying the custom .env location as we're in a sub folder here

username = os.environ['SPOTIFY_USERNAME']
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIFY_CALLBACK_URL']
scope = 'user-read-recently-played user-read-playback-state user-modify-playback-state user-read-currently-playing'


# noinspection PyDeprecation
def check():
    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    spotify_fetcher = spotipy.Spotify(auth=token)
    current_playback = spotify_fetcher.current_playback('DE')
    current_title = current_playback['item']['name']
    current_artist = current_playback['item']['artists'][0]['name']
    current_song_URL = current_playback['item']['external_urls']['spotify']

    return current_title, current_artist, current_song_URL
