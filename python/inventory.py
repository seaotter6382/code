# imports
import time
import random
from colorama import Fore, Style

# vars
slot_1 = "no_item"
slot_2 = "no_item"
slot_3 = "no_item"
slot_4 = "no_item"
slot_5 = "no_item"
var = 0
slot1 = 1
slot2 = 2
slot3 = 3
slot4 = 4
slot5 = 5
slot_1_full = "empty"
slot_2_full = "empty"
slot_3_full = "empty"
slot_4_full = "empty"
slot_5_full = "empty"

# functions
def items():
    print(slot_1, slot_2, slot_3, slot_4, slot_5)

# game
# rarity key
# 1-60 common (white)
# 61-80 uncoomon (green)
# 81-90 rare (purple)
# 91-99 lengentary (yellow)
# 100 mythic (pink)
for i in range(5):
    random_1 = random.randint(1, 100)
    if random_1 >= 0 and random_1 <= 60:
        #print('you got a common item!')
        random_2 = random.randint(1, 2)
        if random_2 == 1:
            item_name = "wooden_sword"
        if random_2 == 2:
            item_name = "rusty_spellbook"
    if random_1 >= 61 and random_1 <= 80:
        #print('you got a ' + Fore.GREEN + 'uncommon item!' + Style.RESET_ALL)
        random_2 = random.randint(1, 2)
        if random_2 == 1:
            item_name = "\033[32miron_sword\033[0m"
        if random_2 == 2:
            arrows = random.randint(10, 25)
            item_name = "\033[32mbow_arrow x" + str(arrows) + "\033[0m"
    if random_1 >= 81 and random_1 <= 90:
        #print('you got a ' + Fore.MAGENTA + 'rare item!' + Style.RESET_ALL)
        random_2 = random.randint(1, 2)
        if random_2 == 1:
            item_name = "\033[35mdiamond sword\033[0m"
        if random_2 == 2:
            crossbow_arrows = random.randint(5, 15)
            item_name = "\033[35mcrossbow x" + str(crossbow_arrows) + "\033[0m"
    if random_1 >= 91 and random_1 <= 99:
        #print('you got a ' + Fore.YELLOW + 'lengdary item!' + Style.RESET_ALL)
        random_2 = random.randint(1, 2)
        if random_2 == 1:
            item_name = Fore.YELLOW + "dammage_potion" + Style.RESET_ALL
        if random_2 == 2:
            item_name = Fore.YELLOW + "rocket_launcher" + Style.RESET_ALL
    if random_1 == 100:
        #print('you got a ' + Fore.CYAN + 'MYTHIC ITEM!!!!!!' + Style.RESET_ALL)
        random_2 = random.randint(1, 2)
        if random_2 == 1:
            item_name = Fore.CYAN + "mini_fridge" + Style.RESET_ALL
        if random_2 == 2:
            item_name = Fore.CYAN + "magic_sword" + Style.RESET_ALL
    
    print("you found a " + item_name)
    time.sleep(0.5)
    print('what slot do you want to put this on?')
    var = 0
    if slot_1 == "no_item":
        var = var + 1
        print('slot ' + str(slot1) + ' (' + str(var) + ')')
        time.sleep(0.1)
    if slot_2 == "no_item":
        var = var + 1
        print('slot ' + str(slot2) + ' (' + str(var) + ')')
        time.sleep(0.1)
    if slot_3 == "no_item":
        var = var + 1
        print('slot ' + str(slot3) + ' (' + str(var) + ')')
        time.sleep(0.1)
    if slot_4 == "no_item":
        var = var + 1
        print('slot ' + str(slot4) + ' (' + str(var) + ')')
        time.sleep(0.1)
    if slot_5 == "no_item":
        var = var + 1
        print('slot ' + str(slot5) + ' (' + str(var) + ')')
        time.sleep(0.1)
    
    
    while True:
        secret = 0
        try:
            word = int(input())
        except ValueError as e:
            print('please enter a number not a letter')
            continue
        if word < var + 1:
            if word == slot1:
                if slot_1 == "no_item":
                    secret = secret + 1
                    slot_1 = item_name
                    print('\033[31msuccesfully put the item into the slot!\033[0m')
                    break
                if not slot_1 == "no_item":
                    print('this slot already has a item')
                    time.sleep(0.5)
                    print('please select another slot from the list above')
            if word == slot2:
                if slot_2 == "no_item":
                    secret = secret + 1
                    slot_2 = item_name
                    print('\033[31msuccesfully put the item into the slot\033[0m!')
                    break
                if not slot_2 == "no_item":
                    print('this slot already has a item')
                    time.sleep(0.5)
                    print('please select another slot from the list above')
            if word == slot3:
                if slot_3 == "no_item":
                    secret = secret + 1
                    slot_3 = item_name
                    print('\033[31msuccesfully put the item into the slot!\033[0m!')
                    break
                if not slot_3 == "no_item":
                    print('this slot already has a item')
                    time.sleep(0.5)
                    print('please select another slot from the list above')
            if word == slot4:
                if slot_4 == "no_item":
                    secret = secret + 1
                    slot_4 = item_name
                    print('\033[31msuccesfully put the item into the slot!\033[0m')
                    break
                if not slot_4 == "no_item":
                    print('this slot already has a item')
                    time.sleep(0.5)
                    print('please select another slot from the list above')
            if word == slot5:
                if slot_5 == "no_item":
                    secret = secret + 1
                    slot_5 = item_name
                    print('\033[31msuccesfully put the item into the slot!\033[0m')
                    break
                if not slot_5 == "no_item":
                    print('this slot already has a item')
                    time.sleep(0.5)
                    print('please select another slot from the list above')
        if word > secret:
            print('uh thats not a real slot')
            time.sleep(0.25)
            print('please enter a real slot from the list above')
    time.sleep(0.5)
    print('your current inventory is:')
    items()
    print("\n")
    time.sleep(1)

