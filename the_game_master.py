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
#name=input("What is your adventures name? ")


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
moster_list = {
    1:{"name": "slime", "mon_level": 1, "mon_attack": 1, "mon_health": 2, "exp": 2},
    2:{"name": "skeleton", "mon_level": 2, "mon_attack": 2, "mon_health": 4, "exp": 4},
    3:{"name": "zombie", "mon_level": 5, "mon_attack": 3, "mon_health": 10, "exp": 10},
    4:{"name": "mini dragon", "mon_level": 10, "mon_attack": 5, "mon_health": 20, "exp": 50}
    }

#battle logic here
def battle():
    return

#boss battle logic here
def boss_battle():
    return

#treasure event
def treasure():
    global weapon
    global weapon_damage
    global armour
    global armour_defence
    treas_num=random.randint(0,10)
    if treas_num in (0,1,2,3,4):
        weap_num=random.randint(1,10)
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
        
#gain exp
def gain_exp(exp):
    current_exp+=exp
    if current_exp >= req_exp and level < 10:
        level += 1
        current_exp=0
        current_hp=max_hp
    elif current_exp >= req_exp:
        current_exp=0
        current_hp=max_hp

#main logic
def random_event(ran_num):
    global inn_check
    global boss_count
    global current_hp
    global max_hp
    global level
    global boss_battle_done
    global weapon
    global weapon_damage
    global armour
    global armour_defence
  
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
        print("You find the dragons castle!")
        print("You rest to recover your HP before continuing.")
        current_hp=max_hp
        if level != 10:
            print("The dragon is stronger than you... do you want to come back later?")
            answer=input("yes or no:")
            if answer.lower() == "no":
                #boss_battle
                print("boss fight here")
                boss_battle_done=True
                return boss_battle_done
            else:
                boss_count-=5
                return inn_check, boss_count
        else:
            #boss_battle
            print("boss fight here")
            boss_battle_done=True
    elif ran_num in (1,2,3):
        print("You continue down the road.")
        inn_check += 1
        boss_count+=1
        return inn_check, boss_count
    elif ran_num in (4,5,6):
        print("You run into a monster!")
        #battle
        print("battle here")
        inn_check += 1
        boss_count+=1
        return inn_check, boss_count
    elif ran_num == 7:
        print("You find some treasure!")
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
        #boss_battle
        print("boss battle here")
        boss_battle_done=True
        return inn_check, boss_count, boss_battle_done
    

boss_battle_done=False
inn_check=0
boss_count=0
turn=1

while boss_battle_done == False:
    ran_num=random.randint(1,10)
    print("Turn:",turn)
    print("dice roll:",ran_num)
    random_event(ran_num)
    turn+=1
#    print("inn_check:",inn_check)
#    print("boss_count:",boss_count)
#    print("boss_battle_done",boss_battle_done)
    print("---------------------------")
    input("Continue?")


print ("Congratulations, you completed your adventure in", turn-1, "turns.")
print ("You have a", weapon, "and are wearing", armour)
    
