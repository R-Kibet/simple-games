import random;


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the nuber between  1 and {x}:"))
        if guess < random_number:
            print("Ur to low")

        elif guess > random_number:
            print("Too high")
    else:
     print(f"congrats u got the correct number{random_number}")


guess(15)
