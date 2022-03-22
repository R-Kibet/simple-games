import random


def game():
    user = input(" whats ur choice 'r' for rock , 's' for scissors and 'p' for paper ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "its a tie"

    elif is_win(user, computer):  ##user beats computer
        return "you won"
    else:
        return "you lost"


def is_win(player, opponent):
    # return true if player wins
    # logic r>s s>p p>r

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (
            player == "p" and opponent == "r"):
        return True

print(game())