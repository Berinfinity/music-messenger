from importlib.resources import path
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

GENRES = {
    "🌙 Dark Academia": [
        "classical",
        "piano",
        "ambient"
    ],

    "✨ Spiritual Awakening": [
        "spiritual",
        "world",
        "meditation"
    ],

    "🌊 Chill & Reflection": [
        "chill",
        "acoustic",
        "ambient"
    ],

    "⚔️ Epic Journey": [
        "classical",
        "orchestral",
        "soundtrack"
    ],

    "🌌 Cosmic Dreams": [
        "ambient",
        "electronic",
        "experimental"
    ],

    "🔥 Energy & Passion": [
        "pop",
        "rock",
        "dance",
        "electronic"
    ],

    "💔 Emotional Heart": [
        "soul",
        "r-n-b",
        "acoustic",
        "indie"
    ],

    "🌿 Nature & Peace": [
        "folk",
        "acoustic",
        "world"
    ],

    "🌃 Midnight Thoughts": [
        "jazz",
        "lo-fi",
        "ambient"
    ],

    "☀️ Happiness & Light": [
        "pop",
        "happy",
        "dance"
    ]
}

class SpotifyClient:

    def __init__(self):

        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                scope=""
            )
        )

    def discover_universe_song(self):

        path = random.choice(list(GENRES.keys()))

        genre = random.choice(GENRES[path])

        results = self.spotify.search(
            q=f"genre:{genre}",
            type="track",
            limit=10
        )

        tracks = results["tracks"]["items"]

        if not tracks:
            return None

        song = random.choice(tracks)

        return {
            "name": song["name"],
            "artist": song["artists"][0]["name"],
            "genre": path
        }