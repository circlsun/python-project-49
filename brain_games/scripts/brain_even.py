#!/usr/bin/env python3
from brain_games.questions import get_answers, welcome_user


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    get_answers(user_name)


if __name__ == "__main__":
    main()
