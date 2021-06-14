import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

victories = {
    Action.Scissors: [Action.Paper],
    Action.Paper: [Action.Rock],
    Action.Rock: [Action.Scissors]
}


"""
This function is responsible for getting selection from user,
basically it asks user if he wants to pick rock, paper or scissors.
"""
def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}):"))
    action = Action(selection)
    return action


"""
This function is responsible for getting selection from computer,
using random.randit function it's randomizing one of the three possible actions.
"""
def get_computer_selection():
    selection = random.randint(1, len(Action) - 1)
    action = Action(selection)
    return action

"""
This function is responsible for determining the winner.
Basically if the user pick is the same as the computer pick, it's draw.
If computer action is in defeats action, then user win.
If none of the above requirements is satisfied then user lose.
"""
def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")
