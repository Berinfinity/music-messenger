from lyrics_client import LyricsClient


client = LyricsClient()

message = client.get_random_line(
    "Ian Asher",
    "Take Me (To The Moon)"
)

if message:
    print("The universe whispers:")
    print()
    print(f'🎶 "{message}"')
else:
    print("The melody remains silent.")