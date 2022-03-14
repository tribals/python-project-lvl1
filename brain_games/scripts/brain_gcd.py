from brain_games.cli import base_main
from brain_games.games.gcd import RULES, question_gcd, correct_answer


def main():
    base_main(RULES, question_gcd, correct_answer)
