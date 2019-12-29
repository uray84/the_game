#the game!
import random

print("This is a game to practise python!")


#character_stats():
name=""
level=1
max_hp=15
current_hp=15
current_exp=0
req_exp=10
max_level=10
#name=input("What is your name? ")


#equipment_stats():
weapon="dagger"
weapon_damage=1
armour="clothes"
armour_defence=0


#print("Your name is",name)
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
    1:{"name": "sword", "damage":2},
    2:{"name": "axe", "damage":3},
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
    4:{"name": "mini dragon", "mon_level": 10, "mon_attack": 5, "mon_health": 20, "exp": 50},
    5:{"name": "Boss dragon", "mon_level": 10, "mon_attack": 7, "mon_health": 50, "exp": 50}
    }

#battle logic here
def battle():
    global weapon_damage
    global armour_defence
    global current_hp
    global level

    #choose monster
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

    #attack
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
        print("-----")

    if current_hp > 0 and mon_hp <= 0:
        print("You beat the", mon_name)
        print("Your earn",monster_list[mon_id]["exp"], "exp")
        gain_exp(monster_list[mon_id]["exp"])

    else:
        print("You were beaten by the", mon_name)
    return current_hp


#boss battle logic here
def boss_battle():
    global weapon_damage
    global armour_defence
    global current_hp
    global level
    global boss_count
    global boss_battle_done

    #check if ready
    print("boss count:", boss_count)
    print("You find the dragons castle!")
    if level != 10:
        print("You are currently level",level)
        print("The dragon is stronger than you... maybe you should come back later.")
        answer=input("If you want to attack anyway, type 'attack': ")
        if answer.lower() != "attack":
            boss_count-=10
            print("You wisely choose to come back later.")
            return boss_count
    print("You rest to recover your HP before continuing.")
    current_hp=max_hp

    #attack
    mon_id=5
    mon_name=monster_list[mon_id]["name"]
    mon_hp=monster_list[mon_id]["mon_health"]
    mon_attack=monster_list[mon_id]["mon_attack"]
    print("You encounter the",mon_name)

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
        print("Boss HP:", mon_hp)
        print("-----")
    if current_hp > 0 and mon_hp <= 0:
        print("You beat the", mon_name)
        print("Your earn",monster_list[mon_id]["exp"], "exp")
        gain_exp(monster_list[mon_id]["exp"])
        boss_battle_done=True
        return current_hp, boss_battle_done
    else:
        print("You were beaten by the", mon_name)
        return current_hp, boss_battle_done
    return current_hp, boss_battle_done
    

#gain exp
def gain_exp(exp):
    global current_exp
    global req_exp
    global level
    global current_hp
    global max_hp
    global inn_check
    current_exp+=exp
    if current_exp >= req_exp and level < 10:
        level += 1
        max_hp += 5
        current_hp=max_hp
        req_exp += 2
        current_exp=0
        inn_check=0
        print("Level up! You are now level", level)
        print("HP Refreshed. Max HP now", max_hp)
    elif current_exp >= req_exp:
        current_exp=0
        current_hp=max_hp
        print("HP Refreshed")
        inn_check=0
    print(req_exp-current_exp, "exp until next level.")
    return current_exp, current_hp, level, inn_check, max_hp

#treasure event
def treasure():
    global weapon
    global weapon_damage
    global armour
    global armour_defence
    treas_num=random.randint(0,10)

    #get weapon
    if treas_num in (0,1,2,3,4):
        weap_num=random.randint(0,10)
        if weap_num in (0,1,2,3,4):
            weap_choice=1
        elif weap_num in (5,6,7,8):
            weap_choice=2
        elif weap_num == 9:
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
            print("but it's not better than your current weapon.")
            return
    #get armour
    elif treas_num in (5,6,7,8,9):
        arm_num=random.randint(0,10)
        if arm_num in (0,1,2,3,4):
            arm_choice=1
        elif arm_num in (5,6,7,8):
            arm_choice=2
        elif arm_num == 9:
            arm_choice=3
        else:
            print("You found some broken armour.")
            return
        print("You found some", armour_list[arm_choice]["name"])
        if armour_list[arm_choice]["defence"] > armour_defence:
            armour = armour_list[arm_choice]["name"]
            armour_defence = armour_list[arm_choice]["defence"]
            print("and equipped it.")
            return armour, armour_defence
        else:
            print("but it's not better than your current armour.")
            return
    else:
        print("You didn't find anything special")
        

#turn logic
def random_event(ran_num):
    global inn_check
    global boss_count
    global current_hp
    global max_hp
    global boss_battle_done
    
    if boss_count < 0:
        boss_count = 0
    
    if inn_check >= 6:
        if current_hp<max_hp:
            print("You find an inn and stop to rest.\n Your HP has been restored.")
            current_hp=max_hp
            print("Current HP:", current_hp)
        else:
            print("You find an inn, but are not tired so continue on.")
        inn_check=0
        boss_count+=1
        return inn_check, boss_count
    elif boss_count==20:
        boss_battle()
        return boss_count, current_hp, boss_battle_done
    elif ran_num in (1,2):
        print("You continue down the road.")
        inn_check += 1
        boss_count+=1
        return inn_check, boss_count
    elif ran_num in (3,4,5,6):
        battle()
        inn_check += 1
        boss_count += 1
        return inn_check, boss_count
    elif ran_num == 7:
        print("You find a treasure chest!")
        treasure()
        print("Weapon:", weapon, ", Damage:", weapon_damage)
        print("Armour:", armour, ", Defence:", armour_defence)
        inn_check += 1
        boss_count+=1
        return inn_check, boss_count
    elif ran_num in (8,9):
        if current_hp<max_hp:
            print("You find an inn and stop to rest.\n Your HP has been restored.")
            current_hp=max_hp
            print("Current HP:", current_hp)
        else:
            print("You find an inn, but are not tired so continue on.")
        inn_check=0
        boss_count+=1
        return inn_check, boss_count
    else:
        boss_battle()
        return boss_count, current_hp, boss_battle_done


boss_battle_done=False
inn_check=0
boss_count=0
turn=1

while boss_battle_done == False and current_hp > 0:
    ran_num=random.randint(1,10)
    print("Turn:",turn)
    print("dice roll:",ran_num)
    random_event(ran_num)
    turn+=1
    print("---------------------------")
    input("Continue:")
if current_hp <= 0:
    print("Sorry, you died. Please try again")
elif boss_battle_done==True:
    print ("Congratulations, you completed your adventure in", turn-1, "turns.")
else:
    print("something went weird")
print ("You had a", weapon, "and were wearing", armour)
    
