from random import randint

import prompt


_MESSAGE_WELCOME = 'Welcome to the Brain Games!'
_MESSAGE_PROMPT_NAME = 'May I have your name? '  # NOTE: mandatory trailing space
_MESSAGE_HELLO = 'Hello,'
_MESSAGE_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
_MESSAGE_QUESTION_NUMBER = 'Question:'
_MESSAGE_PROMPT_ANSWER = 'Your answer: '  # NOTE: mandatory trailing space
_MESSAGE_WIN_TURN = 'Correct!'
_MESSAGE_LOSE = "is wrong answer ;(. Correct answer was"
_MESSAGE_TRY_AGAIN = "Let's try again,"
_MESSAGE_CONGRATULATIONS = 'Congratulations,'

_REQUIRED_TURNS_TO_WIN = 3
_MAX_QUESTION_NUMBER = 9999

_ANSWER_YES = 'yes'
_ANSWER_NO = 'no'


def main():
    display_welcome()

    user = meet_user()

    game(user)


def meet_user():
    name = prompt_name()
    display_hello(name)

    return name


def prompt_name():
    return prompt.string(f'{_MESSAGE_PROMPT_NAME}')


def game(user):
    correct_answers = 0

    display_rules()

    while correct_answers < _REQUIRED_TURNS_TO_WIN:
        (number, answer) = turn()

        if player_wins(number, answer):
            display_win_turn_message()
            correct_answers += 1
        else:
            display_lose_message(number, answer, user)

            return

    display_congratulations(user)


def player_wins(number, answer):
    if answer == correct_answer(number):
        return True

    return False


def correct_answer(number):
    if is_even(number):
        return _ANSWER_YES

    return _ANSWER_NO


def is_even(n):
    return n % 2 == 0


def turn():
    number = question_number()
    display_question(number)
    answer = prompt_answer()

    return (number, answer)


def question_number():
    return randint(1, _MAX_QUESTION_NUMBER)


def prompt_answer():
    return prompt.string(_MESSAGE_PROMPT_ANSWER)


def display_welcome():
    print(_MESSAGE_WELCOME)


def display_hello(user):
    print(f'{_MESSAGE_HELLO} {user}!')


def display_rules():
    print(_MESSAGE_RULES)


def display_win_turn_message():
    print(_MESSAGE_WIN_TURN)


def display_lose_message(number, answer, player):
    print(f'{answer!r} {_MESSAGE_LOSE} {correct_answer(number)!r}.')
    print(f'{_MESSAGE_TRY_AGAIN} {player}!')


def display_congratulations(player):
    print(f'{_MESSAGE_CONGRATULATIONS} {player}!')


def display_question(number):
    print(f'{_MESSAGE_QUESTION_NUMBER} {number}')
