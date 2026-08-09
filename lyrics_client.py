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

        # Remove duplicate lines.
        lines = list(dict.fromkeys(lines))

        # Remove very short lines.
        lines = [
            line for line in lines
            if len(line.split()) >= 5
        ]

        # Remove common background-vocal lines.
        lines = [
            line for line in lines
            if not (
                line.startswith("(")
                and line.endswith(")")
            )
        ]

        if not lines:
            return None

        return random.choice(lines)