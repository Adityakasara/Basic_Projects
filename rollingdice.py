import random
def roll_dice():
    return random.randint(1,6)

print("welcome to dice game")

while True:
    input("press Enter to start")
    result = roll_dice()
    print(f"you rolled a {result}!")

choice = input("Do you wish to roll dice again? (y?/n):").lower()
if choice!=y:
    print("thanks for playing , goodbye")
    break