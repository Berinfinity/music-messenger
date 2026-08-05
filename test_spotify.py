from spotify_client import SpotifyClient


def main():

    spotify = SpotifyClient()

    user = spotify.spotify.current_user()

    print(user["display_name"])


if __name__ == "__main__":
    main()