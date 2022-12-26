import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    return name


def is_even(x):
    if x % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_answers(name):
    for tries in range(3):
        num = randint(1, 20)
        print(f"Question: {num}")
        answer = prompt.string('Your answer: ').lower()
        if answer == is_even(num):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{is_even(num)}'")
            print(f"Let's try again, {name}!")
            break
        if tries >= 2:
            print(f"Congratulations, {name}!")
