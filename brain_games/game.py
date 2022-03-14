import prompt


_MESSAGE_QUESTION = 'Question:'
_MESSAGE_PROMPT_ANSWER = 'Your answer:'
_MESSAGE_WIN = 'Correct!'
_MESSAGE_LOSE = 'is wrong answer ;(. Correct answer was'
_MESSAGE_TRY_AGAIN = "Let's try again,"
_MESSAGE_CONGRATULATIONS = 'Congratulations,'

_REQUIRED_TURNS_TO_WIN = 3


def game(rules, game_question, game_correct_answer, user):
    correct_answers = 0

    _display_rules(rules)

    while correct_answers < _REQUIRED_TURNS_TO_WIN:
        user_is_correct = _turn(game_question, game_correct_answer, user)

        if user_is_correct:
            correct_answers += 1
        else:
            return

    _display_congratulations(user)


def _turn(game_question, game_correct_answer, user):
    (question, text_question) = game_question()
    _display_question(text_question)

    answer = _prompt_answer()
    correct_answer = game_correct_answer(question)

    user_is_correct = answer == correct_answer

    if user_is_correct:
        _display_win()
    else:
        _display_lose(answer, correct_answer, user)

    return user_is_correct


def _display_rules(rules):
    print(rules)


def _display_question(text_question):
    print(f'{_MESSAGE_QUESTION} {text_question}')


def _prompt_answer():
    return prompt.string(f'{_MESSAGE_PROMPT_ANSWER} ')


def _display_win():
    print(_MESSAGE_WIN)


def _display_lose(answer, correct_answer, user):
    print(f'{answer!r} {_MESSAGE_LOSE} {correct_answer!r}.')
    print(f'{_MESSAGE_TRY_AGAIN} {user}!')


def _display_congratulations(user):
    print(f'{_MESSAGE_CONGRATULATIONS} {user}!')
