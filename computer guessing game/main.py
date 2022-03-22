import random;



def computer_guess(x):

    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low
        guess = random.randint(low , high)
        feedback = input(f"{guess} too high (H) too low (l) or correct(c)").lower()
        if feedback == "h":
            high == guess - 1
        elif feedback == "l":
            low == + 1

        else:
            print(f"the computer has guessed it correct  {guess}")

computer_guess(20) ## enter value of your choice