#rock_paper_scissors.py Plays rock paper scissors
#ALec Harmeling

import random
chi = input("Rock, paper, or scissors?")
roll = random.randint(1 , 3)


print("rock...")

print("paper...")

print("scissors...")

print("Shoot!")

print(chi)

if roll == 1 :print("rock!")

elif roll == 2 :print("paper!")

elif roll == 3 :print("scissors")

if chi == "rock" and roll == 1 or chi == "paper" and roll == 2 or chi == "scissors" and roll == 3:
    print("Its a tie")

if chi == "paper" and roll == 3 or chi == "rock" and roll == 2 or chi == "scissors" and roll == 1:
    print("You lost against the computer")

if chi == "scissors" and roll == 2 or chi == "paper" and roll == 1 or chi == "rock" and roll == 3:
    print("You won!")

input("\n\nPress enter to exit")
