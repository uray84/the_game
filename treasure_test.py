#the game!
import random

print("This is me making a game!")


#character_stats():
name=""
level=1
max_hp=10+(level*5)
current_hp=15
current_exp=0
req_exp=10*level
max_level=10
#name=input("What is your name? ")

print("Your name is",name)
print("level:",level)
print("Max HP:", max_hp)
print("Current HP:", current_hp)
print("Current Exp:", current_exp)
print("Exp for level up:", req_exp)

print("======================")

#equipment_stats():
weapon="fist"
weapon_damage=1
armour="none"
armour_defence=0


#weapon dict
weapon_list = {
    1:{"name": "dagger", "damage":2},
    2:{"name": "sword", "damage":3},
    3:{"name": "dragon mace", "damage":5}
    }

#armour dict
armour_list = {
    1:{"name": "leather armour", "defence": 1},
    2:{"name": "platemale armour", "defence": 2},
    3:{"name": "dragon armour", "defence": 3}
    }


#treasure event
def treasure(treas_num):
    global weapon
    global weapon_damage
    global armour
    global armour_defence
    if treas_num in (0,1,2,3,4):
        weap_num=random.randint(1,10)
        print("weap_num",weap_num)
        if weap_num in (1,2,3,4):
            weap_choice=1
        elif weap_num in (5,6,7):
            weap_choice=2
        elif weap_num in (8,9):
            weap_choice=3
        else:
            print("You found a broken weapon.")
            return
        print("You found a", weapon_list[weap_choice]["name"])
        if weapon_list[weap_choice]["damage"] > weapon_damage:
            weapon = weapon_list[weap_choice]["name"]
            weapon_damage = weapon_list[weap_choice]["damage"]
            print("and equipped it.")
            return weapon, weapon_damage
        else:
            print("but your current weapon is better.")
            return

    elif treas_num in (5,6,7,8,9):
        print("You found some armour.")
        arm_num=random.randint(1,10)
        print("arm_num",arm_num)
        if arm_num in (1,2,3,4):
            arm_choice=1
        elif arm_num in (5,6,7):
            arm_choice=2
        elif arm_num in (8,9):
            arm_choice=3
        else:
            print("You found some broken armour.")            
        print("You found some", armour_list[arm_choice]["name"])
        if armour_list[arm_choice]["defence"] > armour_defence:
            armour = armour_list[arm_choice]["name"]
            armour_defence = armour_list[arm_choice]["defence"]
            print("and equipped it.")
            return armour, armour_defence
        else:
            print("but your current armour is better.")
            return
    else:
        print("You didn't find anything special")


turn=1
while turn <=10:
    print("turn",turn)
    treas_num=random.randint(0,10)
    print("treas_num",treas_num)
    treasure(treas_num)
    turn+=1
    print("---------------")

