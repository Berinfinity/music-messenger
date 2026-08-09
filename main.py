from lyrics_client import LyricsClient
from spotify_client import SpotifyClient
from time import sleep


def show_welcome():
    print("=" * 48)
    print("               ✨MUSIC MESSENGER✨")
    print("=" * 48)
    print()

    sleep(2)
    print("Everything moves in harmony")
    print("with the rhythm of the universe.")
    print()

    sleep(3)
    print("Every melody carries a story.")
    print("Perhaps one of them")
    print("is meant for you today.")
    print()

    sleep(4)

    print("The universe speaks in many ways.")
    sleep(2)
    print("Sometimes through stars.")
    sleep(1)
    print("Sometimes through silence.")
    sleep(1)
    print("And sometimes...")
    sleep(1.5)
    print("through music.")
    print()
    sleep(2)
    input("Press ENTER to begin your journey...")

def choose_music_path():

    options = {
        "1": "universe",
        "2": "genre",
        "3": "artist",
        "4": "album",
        "5": "exit"
    }

    while True:

        print("=" * 48)
        print("How would you like to receive")
        print("your musical message?")
        print("=" * 48)
        print()

        print("1. Let the Universe Choose")
        print("2. Choose a Genre")
        print("3. Choose an Artist")
        print("4. Choose an Album")
        print("5. End the Journey")
        print()

        choice = input("Enter your choice (1-5): ").strip()

        if choice in options:
            return options[choice]

        print()
        print("The universe couldn't understand your choice.")
        print("Please enter a number between 1 and 5.\n")


def main():
    show_welcome()

    while True:
        print()
        print("Listening to the echoes of the universe...")
        sleep(2)

        choice = choose_music_path()

        if choice == "exit":
            print()
            print("May the universe guide your next journey.")
            return

        print()
        print("The universe is listening...")
        sleep(2)

        print("Searching beyond the harmony...")
        sleep(2)

        try:
            spotify = SpotifyClient()

            if choice == "universe":
                song = spotify.discover_universe_song()
            elif choice == "genre":
                genre = input("Which genre speaks to you today? ").strip()
                song = spotify.discover_by_genre(genre)
            elif choice == "artist":
                artist = input("Which artist's universe would you like to explore? ").strip()
                song = spotify.discover_by_artist(artist)
            elif choice == "album":
                album = input("Which album holds your message? ").strip()
                song = spotify.discover_by_album(album)

        except Exception as e:
            print("The universe could not connect with Spotify.")
            print(e)
            return

        if song:
            print()
            print("✨ Your musical message has arrived ✨")
            print()
            sleep(2)

            print("The universe has chosen a frequency aligned with you:")
            print()
            print(f"🌌 Path: {song['genre']}\n")
            print(f"🎵 Song: {song['name']}")
            print(f"🎤 Artist: {song['artist']}")

            print()

            wants_lyrics = input(
                "Would you like a deeper message from this melody? (yes/no): "
            ).strip().lower()

            if wants_lyrics in ("yes", "y"):

                lyrics_client = LyricsClient()

                message = lyrics_client.get_random_line(
                    song["artist"],
                    song["name"]
                )

                print()

                if message:
                    print("The universe whispers:")
                    print()
                    print(f'🎶 "{message}"')
                else:
                    print("The melody keeps its message hidden for now.")

            print()
            another = input(
                "Would you like to receive another musical message? (y/n): "
            ).strip().lower()

            if another not in ("yes", "y"):
                print()
                print("May the universe guide your next journey.")
                return

        else:
            print("The universe could not find a melody for this path.")


if __name__ == "__main__":
    main()