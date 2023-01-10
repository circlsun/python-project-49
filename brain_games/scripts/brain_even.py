#!/usr/bin/env python3
from brain_games.questions import welcome_user, get_random_num, is_even, start_game


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(user_name, is_even(get_random_num()), get_random_num(), 3)

if __name__ == "__main__":
    main()
