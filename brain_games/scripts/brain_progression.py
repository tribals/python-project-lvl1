from brain_games.cli import base_main
from brain_games.games.progression import RULES, question_progression, correct_answer


def main():
    base_main(RULES, question_progression, correct_answer)


if __name__ == '__main__':
    main()
