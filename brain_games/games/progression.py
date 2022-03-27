import random

from brain_games.game import game


_RULES = 'What number is missing in the progression?'

_PROGRESSION_MAX_START = 99
_PROGRESSION_MAX_INCREMENT = 10
_PROGRESSION_LENGTH = 10


def game_progression(user):
    game(_RULES, question_progression, correct_answer, user)


def question_progression():
    progression = _random_progression()
    missing_element_index = _missing_element(progression)

    text_question = _hide_missing_element(progression, missing_element_index)

    return ((progression, missing_element_index), text_question)


def _random_progression():
    start = random.randint(0, _PROGRESSION_MAX_START)
    step = random.randint(1, _PROGRESSION_MAX_INCREMENT)

    result = ()
    i = 0

    while i < _PROGRESSION_LENGTH:
        result += (start + step * i,)
        i += 1

    return result


def _missing_element(progression):
    return random.randint(0, len(progression) - 1)


def _hide_missing_element(progression, missing_element_index):
    result = ''
    i = 0

    while i < _PROGRESSION_LENGTH:
        if i == missing_element_index:
            result += '.. '
        else:
            result += f'{progression[i]} '

        i += 1

    return result


def correct_answer(question):
    (progression, missing_element_index) = question

    return str(progression[missing_element_index])
