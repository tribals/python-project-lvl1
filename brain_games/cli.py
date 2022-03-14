import prompt

from brain_games.game import game

_MESSAGE_WELCOME = 'Welcome to the Brain Games!'
_MESSAGE_PROMPT_NAME = 'May I have your name?'
_MESSAGE_HELLO = 'Hello,'


def base_main(rules, game_question, game_correct_answer):
    display_welcome()

    user = meet_user()

    game(rules, game_question, game_correct_answer, user)


def display_welcome():
    print(_MESSAGE_WELCOME)


def meet_user():
    name = _prompt_name()
    _display_hello(name)

    return name


def _prompt_name():
    return prompt.string(f'{_MESSAGE_PROMPT_NAME} ')


def _display_hello(user):
    print(f'{_MESSAGE_HELLO} {user}!')
