import random

jackpot = random.randint(0,101)
guess = int(input("Guess the number : "))
count = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Guess the number again : "))
    count += 1
    
print(f"Your guess is correct and number is {guess}")
print(f"You have took {count} attempt.")