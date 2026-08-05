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


def main():
    show_welcome()

    print()
    print("Listening to the echoes of the universe...")
    sleep(2)

    print()
    print("A melody is searching for you...")
    sleep(1.5)


if __name__ == "__main__":
    main()