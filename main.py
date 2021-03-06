#!/usr/bin/env Python

from logic import logic


while True:
    try:
        user_action = logic.get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(logic.Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue


    computer_action = logic.get_computer_selection()
    logic.determine_winner(user_action, computer_action)


    play_again = input("Do you want to play again? (y/n):")
    if play_again.lower() != "y":
        break
