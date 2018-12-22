

user_list = ["XX", "Ht", "As"]  # user input example, need to be a string then converted to a list.
broker_entry = "1"


import math
import random
from trade_class import trade_goods


common_electronics = trade_goods("Common Electronics", ["All"], "2d6*10", 20000, ["In", 2, "Ht", 3, "Ri", 1],
                                 ["Na", 2, "Lt", 1, "Po", 1], "Simple electronics, basic computers.")
common_industrial = trade_goods("Common Industrial", ["All"], "2d6*10", 10000, ["Na", 2, "In", 5], ["Ni", 3, "Ag", 2],
                                "Machine components and common spare parts.")
common_manufactured = trade_goods("Common Manufactured Goods", ["All"], "2d*10", 20000, ["Na", 2, "In", 5],
                                  ["Ni", 3,  "Ag", 2], "Household appliances, clothing, etc.")
common_raw = trade_goods("Common Raw Materials", ["All"], "2d6*20", 5000, ["Na", 3, "Ga", 2], ["In", 2, "Po", 2],
                         "Metals, chemicals, plastics, other basic materials.")
common_consumables = trade_goods("Common Consumables", ["All"], "2d6*20", 500, ["Ag", 3, "Wa", 2, "Ga", 1, "As", -4],
                                 ["As", 1, "Fl", 1, "Ie", 1, "Hi", 1], "Food, drink and other agri products.")
common_ore = trade_goods("Common Ore", ["All"], "2d6*20", 1000, ["As", 4], ["In", 3, "Ni", 1],
                         "Ore bearing common metals.")

advanced_electronics = trade_goods("Advanced Electronics", ["In", "Ht"], "1d6*5", 100000, ["In", 2, "Ht", 3, "Ri", 1],
                                   ["Na", 2, "Lt", 1, "Po", 1], "Advanced sensors and computers up to TL15.")
advanced_machine = trade_goods("Advanced Machine Parts", ["In", "Ht"], "1d6*5", 75000, ["In", 2, "Ht", 1],
                               ["As", 2, "Ni", 1], "Machine components, spare parts up to TL15.")
advanced_manufactured = trade_goods("Advanced Manufacturing Goods", ["In", "Ht"], "1d6*5", 100000, ["In", 1],
                                    ["Hi", 1, "Ri", 2], "Devices and clothing incorporating advanced tech.")
advanced_weapons = trade_goods("Advanced Weapons", ["In", "Ht"], "1d6*5", 150000, ["Ht", 2],
                            ["Po", 1, "Amber", 2, "Red", 4], "Firearms, explosives, ammo, artillery. Military grade.")
advanced_vehicles = trade_goods("Advanced Vehicles", ["In", "Ht"], "1d6*5", 180000, ["Ht", 2],
                                ["As", 2, "Ri", 2], "Air/rafts, spacecraft, grav tanks, vehicles up to TL15.")
biochemicals = trade_goods("Biochemicals", ["Ag", "Wa"], "1d6*5", 50000, ["Ag", 1, "Wa", 2],
                           ["In", 2], "Biofuels, organic chemicals, extracts.")
crystals_gems = trade_goods("Crystals & Gems", ["As", "De", "Ie"], "1d6*5", 20000, ["As", 2, "De", 1, "Ie", 1],
                            ["In", 3, "Ri", 2], "Diamonds, synthetics or natural gemstones.")
cybernetics = trade_goods("Cybernetics", ["Ht"], "1d6", 250000, ["Ht", 1], ["As", 1, "Ie", 1, "Ri", 2],
                          "Cybernetic components, replacement limbs.")
animals = trade_goods("Animals", ["Ag","Ga"], "1d6*10", 10000, ["Ag", 2], ["Lo", 3],
                      "Riding animals, beasts of burden, exotic pets.")
luxury_consumables = trade_goods("Luxury Consumables", ["Ag", "Ga", "Wa"], "1d6*10", 20000,
                                 ["Ag", 2, "Wa", 1], ["Ri", 2, "Hi", 2], "Rare foods, fine liquors.")
luxury_goods = trade_goods("Luxury Goods", ["Hi"], "1d6", 200000, ["Hi", 1], ["Ri", 4],
                           "Rare or extremely high-quality manufactured goods.")
medical_supplies = trade_goods("Medical Supplies", ["Hi","Ht"], "1d6*5", 50000, ["Ht", 2], ["In", 2, "Ri", 1, "Po", 1],
                               "Diagnostic equipment, basic drugs, cloning tech.")
petrochemicals = trade_goods("Petrochemicals", ["De", "Fl", "Ie", "Wa"], "1d*10", 10000, ["De", 2],
                             ["In", 2, "Ag", 1, "Lt", 2], "Oil, liquid fuels.")
pharma = trade_goods("Pharmaceuticals", ["As", "De", "Hi", "Wa"], "1d6", 100000, ["As", 2, "Hi", 1],
                     ["Ri", 2, "Lt", 1], "Drugs, medical supplies, fast/slow drugs, anagathatics.")
polymers = trade_goods("Polymers", ["In"], "1d6*10", 7000, ["In", 1], ["Ri", 2, "Ni", 1],
                       "Plastics and other synthetics.")
precious_metals = trade_goods("Precious Metals", ["As", "De", "Ie", "Fl"], "1d6", 50000,
                              ["As", 3, "De", 1, "Ie", 2], ["Ri", 3, "In", 2, "Ht", 1],
                              "Gold, silver, platinum, rare elements.")
radioactives = trade_goods("Radioactives", ["As", "De", "Lo"], "1d6", 1000000, ["As", 2, "Lo", 2],
                           ["In", 3, "Ht", 1, "Ni", -2, "Ag", -3], "Uranium, plutonium, unobtanium, rare elements.")
robots = trade_goods("Robots", ["All"], "1d6*5", 400000, ["In", 1], ["Ag", 2, "Ht", 1],
                     "Industrial and personal robots and drones.")
spices = trade_goods("Spices", ["Ga", "De", "Wa"], "1d6*10", 6000, ["De", 2], ["Hi", 2, "Ri", 3, "Po", 3],
                     "Preservatives, luxury food additives, natural drugs.")
textiles = trade_goods("Textiles", ["Ag", "Ni"], "1d6*20", 3000, ["Ag", 7], ["Hi", 3, "Na", 2], "Clothing and fabrics.")
uncommon_ore = trade_goods("Uncommon Ore", ["As", "Ie"], "1d6*10", 5000, ["As", 4], ["In", 3, "Ni", 1],
                           "Ore containing precious or valuable metals.")
uncommon_raw = trade_goods("Uncommon Raw Materials", ["Ag", "De", "Wa"], "1d6*10", 20000, ["Ag", 2, "Wa", 1], [
    "In", 2, "Ht", 1], "Valuable metals, rare elements.")
wood = trade_goods("Wood", ["Ag", "Ga"], "1d6*20", 1000, ["Ag", 6], ["Ri", 2, "In", 1],
                   "Hard or beautiful woods and plant extracts.")
vehicles = trade_goods("Vehicles", ["In", "Ht"], "1d6*10", 15000, ["In", 2, "Ht", 1], ["Ni", 2, "Hi", 1],
                       "Wheeled, tracked and other vehicles from TL10 or lower.")
illegal_bio = trade_goods("Illegal Biochemicals", ["Ag", "Wa"], "1d6*5", 50000, ["Wa", 2], ["In", 6],
                          "Dangerous chemicals, extracts from endangered species.")
illegal_cyber = trade_goods("Illegal Cybernetics", ["Ht"], "1d6", 250000, ["Ht", 1],
                        ["As", 4, "Ie", 4, "Ri", 8, "Amber", 6, "Red", 6], "Combat cybernetics, illegal enhancements.")
illegal_drugs = trade_goods("Illegal Drugs", ["As", "Hi", "De", "Wa"], "1d6", 100000,
                            ["As", 1, "De", 1, "Ga", 1, "Wa", 1], ["Ri", 6, "Hi", 6], "Addictive drugs, combat drugs.")
illegal_luxuries = trade_goods("Illegal Luxuries", ["Ag", "Ga", "Wa"], "1d6", 50000,
                               ["Ag", 2, "Wa", 1], ["Ri", 6, "Hi", 4], "Debauched or addictive luxuries.")
illegal_weapons = trade_goods("Illegal Weapons", ["In", "Ht"], "1d6*5", 150000, ["Ht", 2],
                              ["Po", 6, "Amber", 8, "Red", 10], "Weapons of mass destruction, naval weapons.")
exotics = trade_goods("Exotics", "Special", "Special", 1, ["Special", 1], ["Special", 1], "Special.")
#35 entries

master_trade_goods_list = []
master_trade_goods_list.append(common_electronics)
master_trade_goods_list.append(common_industrial)
master_trade_goods_list.append(common_manufactured)
master_trade_goods_list.append(common_raw)
master_trade_goods_list.append(common_consumables)
master_trade_goods_list.append(common_ore)
master_trade_goods_list.append(advanced_electronics)
master_trade_goods_list.append(advanced_machine)
master_trade_goods_list.append(advanced_manufactured)
master_trade_goods_list.append(advanced_weapons)
master_trade_goods_list.append(advanced_vehicles)
master_trade_goods_list.append(biochemicals)
master_trade_goods_list.append(crystals_gems)
master_trade_goods_list.append(cybernetics)
master_trade_goods_list.append(animals)
master_trade_goods_list.append(luxury_consumables)
master_trade_goods_list.append(luxury_goods)
master_trade_goods_list.append(medical_supplies)
master_trade_goods_list.append(petrochemicals)
master_trade_goods_list.append(pharma)
master_trade_goods_list.append(polymers)
master_trade_goods_list.append(precious_metals)
master_trade_goods_list.append(radioactives)
master_trade_goods_list.append(robots)
master_trade_goods_list.append(spices)
master_trade_goods_list.append(textiles)
master_trade_goods_list.append(uncommon_ore)
master_trade_goods_list.append(uncommon_raw)
master_trade_goods_list.append(wood)
master_trade_goods_list.append(vehicles)
master_trade_goods_list.append(illegal_bio)
master_trade_goods_list.append(illegal_cyber)
master_trade_goods_list.append(illegal_drugs)
master_trade_goods_list.append(illegal_luxuries)
master_trade_goods_list.append(illegal_weapons)
master_trade_goods_list.append(exotics)

print(master_trade_goods_list)

purchase_list = {
    0: 1.75,
    1: 1.5,
    2: 1.35,
    3: 1.25,
    4: 1.2,
    5: 1.15,
    6: 1.1,
    7: 1.05,
    8: 1,
    9: 0.95,
    10: 0.9,
    11: 0.85,
    12: 0.8,
    13: 0.75,
    14: 0.7,
    15: 0.65,
    16: 0.6,
    17: 0.55,
    18: 0.5,
    19: 0.45,
    20: 0.4,
    21: 0.35,
    22: 0.3,
    23: 0.25
}

a = 0
x = 0
j = 0
trade_list_all = []
while x <= 35:
    x += 1
    if "All" in master_trade_goods_list[j].availability:
        temp_all = master_trade_goods_list[j].type
        temp_all_codes = master_trade_goods_list[j].purchase_dm_list
        temp_price = master_trade_goods_list[j].base_price

        trade_list_all.append(temp_all)
        trade_list_all.append(temp_price)
        trade_list_all.append(temp_all_codes)
        j += 1
print("All list complete")

a = 0
j = 0
k = 0
x = 0
while j <= 35:
    print(master_trade_goods_list[j].type)
    if a >= len(user_list):
        print("A limit has been reached, moving onto next J")
        a = 0
        j += 1
    elif user_list[a] in master_trade_goods_list[j].availability:
        print(user_list[a] + " is in ")
        print(master_trade_goods_list[j].availability)
        temp_any = master_trade_goods_list[j].type
        temp_any_codes = master_trade_goods_list[j].purchase_dm_list
        temp_any_price = master_trade_goods_list[j].base_price

        trade_list_all.append(temp_any)
        trade_list_all.append(temp_any_price)
        trade_list_all.append(temp_any_codes)
        a += 0
        j += 1
        print("Match has been found. Moving to next J")
    elif user_list[a] not in master_trade_goods_list[j].availability:
        print(user_list[a] + " is not in ")
        print(master_trade_goods_list[j].availability)
        a += 1

    #elif user_list


print(trade_list_all)


def start_check():
    new_list = []
    maths_list = []
    a = 0
    y = 2
    z = 0
    print(trade_list_all[2][0])
    while y <= len(trade_list_all):
        if a >= len(user_list):
            print("A is not in XY and is greater than user length")
            y += 3
            z = 0
            a = 0
            if len(new_list) >= 1:
                modifier_number_string = "+".join(new_list)
                print(modifier_number_string)
                price_temp = eval(modifier_number_string)
                maths_list.append(price_temp)
                new_list.clear()
                print(maths_list)
            else:
                maths_list.append(8)
        elif user_list[a] == trade_list_all[y][z]:
            new_list.append(str(trade_list_all[y][z+1]))
            a += 1
            z = 0
            print("A is in Y,Z")
            print(new_list)
        elif user_list[a] != trade_list_all[y][z]:
            z += 2
            print("A is not in Y,Z")
            if z >= len(trade_list_all[y]):
                a += 1
                z = 0
                print("Resetting Z")
    print(maths_list)



    a = 0
    while a < len(maths_list):
        dice_roll = eval(str(random.randint(1, 6))+"+"+str(random.randint(1, 6))+"+"+str(random.randint(1, 6)))
        dice_plus_mod = str(dice_roll)+"+"+str(broker_entry)
        dice_plus_mod = eval(dice_plus_mod)
        temp_number = str(maths_list[a])
        maths_list[a] = (eval((temp_number)+"+"+str(dice_plus_mod)))
        a += 1
        print(maths_list) # this takes the maths_list and adds the players own modifiers, then runns it through the modifier dict (dice roll and broker skill)

    a = 0
    x = 1
    while x <= len(maths_list):
        x += 1
        replacement = maths_list[a]
        if replacement >= 23:
            b = 0.25
        elif replacement <= 0:
            b = 0.25
        else:
            b = purchase_list.get(replacement)
        maths_list[a] = b
        a += 1
    print(maths_list) # this gives us the %-based modifiers to tweak the goods base cost. 0.5/1.15 etc

    a = 0
    c = 1
    while a < len(maths_list):
        replacement = float((maths_list[a]))
        trade_list_all[c] = (replacement*float(trade_list_all[c]))
        a += 1
        c += 3
    print(trade_list_all) # this puts the modified prices into the original list.

    b = 2
    while b <= len(trade_list_all):
        trade_list_all.remove(trade_list_all[b])
        b += 2
    print(trade_list_all) # this removes the trade codes, giving us just item and its cost.

start_check()
