#the game!
import random

print("This is a game to practise python!")


#character_stats():
name=""
level=1
max_hp=10+(level*5)
current_hp=15
current_exp=0
req_exp=10*level
max_level=10
#name=input("What is your name? ")


#equipment_stats():
weapon="fist"
weapon_damage=1
armour="clothes"
armour_defence=0


print("Your name is",name)
print("level:",level)
print("Max HP:", max_hp)
print("Current HP:", current_hp)
print("Current Exp:", current_exp)
print("Exp for level up:", req_exp)
print("Weapon:", weapon, ", Damage:", weapon_damage)
print("Armour:", armour, ", Defence:", armour_defence)

print("======================")



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

#monster dict
monster_list = {
    1:{"name": "slime", "mon_level": 1, "mon_attack": 1, "mon_health": 2, "exp": 2},
    2:{"name": "skeleton", "mon_level": 2, "mon_attack": 2, "mon_health": 4, "exp": 4},
    3:{"name": "zombie", "mon_level": 5, "mon_attack": 3, "mon_health": 10, "exp": 10},
    4:{"name": "mini dragon", "mon_level": 10, "mon_attack": 5, "mon_health": 20, "exp": 50}
    }

#battle logic here
def battle():
    global weapon_damage
    global armour_defence
    global current_hp
    global level
    mon_numb=random.randint(1,10)
    if level in (1,2,3):
        if mon_numb in (1,2,3,4,5,6):
            mon_id=1
        else:
            mon_id=2
    elif level in (4,5,6,7,8):
        if mon_numb in (1,4):
            mon_id=1
        elif mon_numb in (5,6,7,8):
            mon_id=2
        else:
            mon_id=3
    else:
        if mon_numb in (1,2,3,4):
            mon_id=1
        elif mon_numb in (5,6,7):
            mon_id=2
        elif mon_numb in (8,9):
            mon_id=3
        else:
            mon_id=4

#   attack
    mon_name=monster_list[mon_id]["name"]
    mon_hp=monster_list[mon_id]["mon_health"]
    mon_attack=monster_list[mon_id]["mon_attack"]
    print("You encounter a",mon_name)

    while current_hp>0 and mon_hp>0:
        your_damage=weapon_damage + int(level/2) + random.randint(0,3)
        mon_damage=mon_attack-armour_defence
        if mon_damage <=0:
            mon_damage=1
        mon_hp=mon_hp-your_damage
        current_hp=current_hp - (mon_attack-armour_defence)
        print("You attack the",mon_name, "for", your_damage, "damage")
        print("The", mon_name, "attacks you for", mon_damage, "damage")
        print("Current HP:", current_hp)
        print("Monster HP:", mon_hp)

    if current_hp > 0 and mon_hp <= 0:
        print("You beat the", mon_name)
        print("Your earn",monster_list[mon_id]["exp"], "exp")
        gain_exp(monster_list[mon_id]["exp"])

    else:
        print("You were beaten by the", mon_name)
    return current_hp

#boss battle logic here
def boss_battle():
    return

#gain exp
def gain_exp(exp):
    global current_exp
    global req_exp
    global level
    global current_hp
    global max_hp
    current_exp+=exp
    if current_exp >= req_exp and level < 10:
        level += 1
        current_exp=0
        current_hp=max_hp
        print("Level up! You are now level", level)
        print("HP Refreshed")
    elif current_exp >= req_exp:
        current_exp=0
        current_hp=max_hp
        print("HP Refreshed")
    print(req_exp-current_exp, "exp until next level.")
    return current_exp, current_hp, level



boss_battle_done=False
inn_check=0
boss_count=0
turn=1

while boss_battle_done == False:
    ran_num=random.randint(1,10)
    print("Turn:",turn)
    print("dice roll:",ran_num)
    battle()
    turn+=1
#    print("inn_check:",inn_check)
#    print("boss_count:",boss_count)
#    print("boss_battle_done",boss_battle_done)
    print("---------------------------")
    input("Continue?")


print ("Congratulations, you completed your adventure in", turn-1, "turns.")
print ("You have a", weapon, "and are wearing", armour)
    
