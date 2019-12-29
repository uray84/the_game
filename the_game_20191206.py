#the game!
import random

print("This is me making a game!")

name=input("What is your name? ")
print("Your name is",name)

level=1
max_hp=10+(level*5)
current_hp=15
current_exp=0
req_exp=10*level

print("level:",level)
print("Max HP:", max_hp)
print("Current HP:", current_hp)
print("Current Exp:", current_exp)
print("Exp for level up:", req_exp)



#score=random.randint(0,10)
#print(score)
