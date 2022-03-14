from brain_games.cli import base_main
from brain_games.games.calc import RULES, question_expression, correct_answer


def main():
    base_main(RULES, question_expression, correct_answer)


if __name__ == '__main__':
    main()
