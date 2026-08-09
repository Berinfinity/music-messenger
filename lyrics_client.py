import random
import requests


class LyricsClient:

    def get_lyrics(self, artist, title):

        url = "https://lrclib.net/api/get"

        params = {
            "artist_name": artist,
            "track_name": title
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return None

        data = response.json()

        return data.get("plainLyrics")

    def get_random_line(self, artist, title):

        lyrics = self.get_lyrics(artist, title)

        if not lyrics:
            return None

        lines = [
            line.strip()
            for line in lyrics.splitlines()
            if line.strip()
        ]

        if not lines:
            return None

        return random.choice(lines)