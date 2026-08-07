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
    
    print()
    print(f"Selected option: {choice}")


if __name__ == "__main__":
    main()