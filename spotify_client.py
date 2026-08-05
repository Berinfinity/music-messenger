import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


class SpotifyClient:

    def __init__(self):

        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                scope="user-library-read"
            )
        )