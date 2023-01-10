import prompt
from random import randint, choice


def welcome_user():
    name = prompt.string("May I have your name? ")
    return name


def is_even(x):
    if x % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_random_num():
    return randint(1, 20)


def get_random_expression():
    return f"{get_random_num()} {choice(['+', '-', '*'])} {get_random_num()}"


def get_answer(name, game, question):
    answer = prompt.string('Your answer: ').lower()
    return answer == game, answer   


def start_game(name, game, question, tries):
    for user_try in range(tries):
        print(f"Question: {question}")
        user_answer = get_answer(name, game, question)
        if user_answer[0] == True:
            print('Correct!')
        else:
            print(f"'{user_answer[1]}' is wrong answer ;(. Correct answer was '{game}'")
            print(f"Let's try again, {name}!")
        if user_try >= tries - 1:
            print(f"Congratulations, {name}!")
