#fortune.py simulates a fortune cookie
#Alec Harmeling

import random
name = input("What is your name")
roll = random.randint(1 , 5)

if  roll == 1 :print(name , "get no lambo")

if roll == 2 :print(name , "spill juice on your electric bugalu")

if roll == 3 :print(name , "Wizardspeelteller steals your soul")

if roll == 4 :print(name , "Jaydon eats your CD")

if roll == 5 :print(name , "get no money")

input("\n/nPress enter to exit")


