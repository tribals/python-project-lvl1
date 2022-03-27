from brain_games.cli import base_main
from brain_games.games.even import game_even


def main():
    base_main(game_even)


if __name__ == '__main__':
    main()
