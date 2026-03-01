from game_logic import play_game


def main():
    """Main function to play/replay the snowman game"""
    play_game()
    while True:
        replay = input("Would you like to play the snowman game again (answer 'yes' or 'no')? ")
        if replay.lower() in ['yes', 'y']:
            play_game()
        elif replay.lower() in ['no', 'n']:
            break


if __name__ == "__main__":
    main()