from brain_games.cli import base_main
from brain_games.games.prime import RULES, question_number, correct_answer


def main():
    base_main(RULES, question_number, correct_answer)


if __name__ == '__main__':
    main()
