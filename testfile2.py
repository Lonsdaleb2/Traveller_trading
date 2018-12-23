



import math
import random
from trade_class import trade_goods
import re


common_electronics = trade_goods("Common Electronics", ["All"], "2d6*10", 20000, ["In", 2, "Ht", 3, "Ri", 1],
                                 ["Na", 2, "Lt", 1, "Po", 1], "Simple electronics, basic computers.")
common_industrial = trade_goods("Common Industrial", ["All"], "2d6*10", 10000, ["Na", 2, "In", 5], ["Ni", 3, "Ag", 2],
                                "Machine components and common spare parts.")
common_manufactured = trade_goods("Common Manufactured Goods", ["All"], "2d6*10", 20000, ["Na", 2, "In", 5],
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
petrochemicals = trade_goods("Petrochemicals", ["De", "Fl", "Ie", "Wa"], "1d6*10", 10000, ["De", 2],
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
exotics = trade_goods("Exotics",["Special", 1], "1d6", 10 , ["Special", 1], ["Special", 1], "Special.")
#35 entries





def buying(b_t, broker):

    purchase_list_buying = {
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

    broker_entry = broker

    user_list = ["XX", "Ht", "As"]  # user input example, need to be a string then converted to a list.

    print(b_t)

    if b_t == "no":
        trader_value = 30
    else:
        trader_value = 5

    print(trader_value)

    master_trade_goods_list = []

    if trader_value == 30:
        master_trade_goods_list.append(common_electronics) #0
        master_trade_goods_list.append(common_industrial) #1
        master_trade_goods_list.append(common_manufactured) #2
        master_trade_goods_list.append(common_raw) #3
        master_trade_goods_list.append(common_consumables) #4
        master_trade_goods_list.append(common_ore) #5
        master_trade_goods_list.append(advanced_electronics) #6
        master_trade_goods_list.append(advanced_machine) #7
        master_trade_goods_list.append(advanced_manufactured) #8
        master_trade_goods_list.append(advanced_weapons) #9
        master_trade_goods_list.append(advanced_vehicles) #10
        master_trade_goods_list.append(biochemicals) #11
        master_trade_goods_list.append(crystals_gems) #12
        master_trade_goods_list.append(cybernetics) #13
        master_trade_goods_list.append(animals) #14
        master_trade_goods_list.append(luxury_consumables) #15
        master_trade_goods_list.append(luxury_goods) #16
        master_trade_goods_list.append(medical_supplies) #17
        master_trade_goods_list.append(petrochemicals) #18
        master_trade_goods_list.append(pharma) #19
        master_trade_goods_list.append(polymers) #20
        master_trade_goods_list.append(precious_metals) #21
        master_trade_goods_list.append(radioactives) #22
        master_trade_goods_list.append(robots) #23
        master_trade_goods_list.append(spices) #24
        master_trade_goods_list.append(textiles) #25
        master_trade_goods_list.append(uncommon_ore) #26
        master_trade_goods_list.append(uncommon_raw) #27
        master_trade_goods_list.append(wood) #28
        master_trade_goods_list.append(vehicles) #29
        master_trade_goods_list.append(exotics) #30
    if trader_value == 5:
        master_trade_goods_list.append(illegal_bio) #31
        master_trade_goods_list.append(illegal_cyber) #32
        master_trade_goods_list.append(illegal_drugs) #33
        master_trade_goods_list.append(illegal_luxuries) #34
        master_trade_goods_list.append(illegal_weapons) #35


    print(master_trade_goods_list)

    a = 0
    x = 0
    j = 0
    trade_list_all = []
    while x <= trader_value:
        x += 1

        if "All" in master_trade_goods_list[j].availability:
            temp_all = master_trade_goods_list[j].type
            temp_all_codes = master_trade_goods_list[j].purchase_dm_list
            temp_price = master_trade_goods_list[j].base_price
            temp_quantity = master_trade_goods_list[j].tons
            temp_sale = master_trade_goods_list[j].sale_dm_list

            trade_list_all.append(temp_all)
            trade_list_all.append(temp_price)
            trade_list_all.append(temp_quantity)
            trade_list_all.append(temp_all_codes)
            trade_list_all.append(temp_sale)
            j += 1
    print("All list complete")



    a = 0
    j = 0
    k = 0
    x = 0
    while j < trader_value:
        #print(master_trade_goods_list[j].type)
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
            temp_any_quantity = master_trade_goods_list[j].tons
            temp_sale_codes = master_trade_goods_list[j].sale_dm_list

            trade_list_all.append(temp_any)
            trade_list_all.append(temp_any_price)
            trade_list_all.append(temp_any_quantity)
            trade_list_all.append(temp_any_codes)
            trade_list_all.append(temp_sale_codes)
            a += 0
            j += 1
            print("Match has been found. Moving to next J")
        elif user_list[a] not in master_trade_goods_list[j].availability:
            print(user_list[a] + " is not in ")
            print(master_trade_goods_list[j].availability)
            a += 1

    random_goods_list = []
    random_roll = random.randint(1, 6)
    a = 1
    print(random_roll)
    while a <= random_roll:
        random_goods_roll = random.randint(0, (trader_value-1))
        print(random_goods_roll)
        random_goods_name = master_trade_goods_list[random_goods_roll].type
        random_goods_price = master_trade_goods_list[random_goods_roll].base_price
        random_goods_quan = master_trade_goods_list[random_goods_roll].tons
        random_goods_codes = master_trade_goods_list[random_goods_roll].purchase_dm_list
        random_sale_codes = master_trade_goods_list[random_goods_roll].sale_dm_list

        random_goods_list.append(random_goods_name)
        random_goods_list.append(random_goods_price)
        random_goods_list.append(random_goods_quan)
        random_goods_list.append(random_goods_codes)
        random_goods_list.append(random_sale_codes)
        a += 1
        print(random_goods_list)

    trade_list_all.extend(random_goods_list)

    # elif user_list

    print("Starting trade list")
    print(trade_list_all)






    new_list = [] # this sees which purchase trade code modifiers need to be added
    maths_list = []
    a = 0
    y = 3
    z = 0
    print(trade_list_all[2][0])
    while y <= len(trade_list_all):
        if a >= len(user_list):
            print("A is not in XY and is greater than user length")
            y += 5
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
    print("This is the proper list")
    print(maths_list)

    new_list = []
    maths_list_2 = []
    a = 0
    y = 4
    z = 0
    print(trade_list_all[2][0])
    while y <= len(trade_list_all):
        if a >= len(user_list):
            print("A is not in XY and is greater than user length")
            y += 5
            z = 0
            a = 0
            if len(new_list) >= 1:
                modifier_number_string = "+".join(new_list)
                print(modifier_number_string)
                price_temp = eval(modifier_number_string)
                maths_list_2.append(price_temp)
                new_list.clear()
                print(maths_list_2)
            else:
                maths_list_2.append(0)
        elif user_list[a] == trade_list_all[y][z]:
            new_list.append(str(trade_list_all[y][z + 1]))
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
    print("This is the sales modifier list")
    print(maths_list_2)
    print(maths_list)




    a = 0
    while a < len(maths_list):
        dice_roll = eval(str(random.randint(1, 6))+"+"+str(random.randint(1, 6))+"+"+str(random.randint(1, 6)))
        dice_plus_mod = str(dice_roll)+"+"+str(broker_entry)+"-"+str(maths_list_2[a])
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
            b = purchase_list_buying.get(replacement)
        maths_list[a] = b
        a += 1
    print(maths_list) # this gives us the %-based modifiers to tweak the goods base cost. 0.5/1.15 etc

    a = 0
    c = 1
    while a < len(maths_list):
        replacement = float((maths_list[a]))
        trade_list_all[c] = "- Cr "+str(round(replacement*int(trade_list_all[c]))) + "/ton,"
        a += 1
        c += 5
    print(trade_list_all) # this puts the modified prices into the original list.

    b = 3
    while b <= len(trade_list_all):
        trade_list_all.remove(trade_list_all[b])
        b += 4
    print(trade_list_all) # this removes the trade codes

    b = 3
    while b <= len(trade_list_all):
        trade_list_all.remove(trade_list_all[b])
        b += 3
    print(trade_list_all) # this removes the 2nd set of trade codes, giving us just item and its cost.


    h = 2
    dice_holding_pen = []
    while h <= len(trade_list_all):
        temp_dice = trade_list_all[h]
        dice_holding_pen.append(temp_dice)
        dice_holding_pen.append(h)
        print(dice_holding_pen)
        h += 3


    #########start of dice maths
    dice_holding_pen_2 = []
    AA = 0
    BB = 0
    while AA <= len(dice_holding_pen):
        AA += 2
        if AA <= len(dice_holding_pen):
            dice = str(dice_holding_pen[BB])
            dice = dice.replace("*", " multiply ")
            dicelist = re.sub("[^\w]", " ", dice).split()
            print("The input. Splitting each piece to be worked on separately. ")
            print(dicelist)


            dice_coords = []  # this shows where the dice belong in the original dicelist
            space = " "
            a = 1
            b = 0
            letters = set("d")
            while a <= len(dicelist):
                a += 1
                for w in dicelist:
                    if letters & set(w):
                        dice_location = dicelist.index(w)
                        print(w + " " + str(dice_location))
                        dicelist[dice_location] = space
                        dice_coords.append(w)
                        dice_coords.append(dice_location)
                        b += 1
                        print(dice_coords)

            the_dice_var = dice_coords[0::2]
            the_location_var = dice_coords[1::2]
            print("Location of dice and what dice need to be rolled:")
            print(the_location_var)
            print(the_dice_var)

            quantity_1 = 0
            dice_post_while = []
            while quantity_1 < len(the_dice_var):
                the_dice_var_while = the_dice_var[quantity_1].split("d")
                quantity_1 += 1
                dice_post_while.append(the_dice_var_while)
            print(dice_post_while)

            quantity_2 = 0
            times_to_roll = []
            dice_type = []
            while quantity_2 < len(dice_post_while):
                times_to_roll_while = dice_post_while[quantity_2][0]
                dice_type_while = dice_post_while[quantity_2][1]
                quantity_2 += 1
                times_to_roll.append(times_to_roll_while)
                dice_type.append(dice_type_while)
            print("Number of times the dice need to rolled and what type they are.")
            print(times_to_roll)
            print(dice_type)
            print("The generated dice:")

            roll_entry = 0
            master_dice_numbers = []
            j = 1
            a = len(times_to_roll)
            while j <= a:
                j += 1
                x = 1
                dice_numbers = []
                master_dice_numbers.append(dice_numbers)
                t = times_to_roll[roll_entry]
                d = dice_type[roll_entry]
                roll_entry += 1

                while x <= int(t):
                    roll = random.randint(1, int((d)))
                    dice_total = 0
                    dice_total += roll
                    x += 1
                    dice_numbers.append(dice_total)
                print(dice_numbers)
            print("Master list for the now generated dice numbers. These will use the above location_var to put them back into"
                  " their original place")
            print(master_dice_numbers)

            x = 1
            e = 0
            d = 0
            while x <= len(the_location_var):
                c = int(the_location_var[e])
                b = (master_dice_numbers[d])
                dicelist[c] = b  # insert location, then thing you want to insert
                x += 1
                e += 1
                d += 1


            x = 1
            a = 0
            while x <= len(the_location_var):
                Q = the_location_var[a]
                dice_string = "+".join(str(e) for e in (dicelist[Q]))  # - to turn a list into a string
                dicelist[Q] = ("(" + dice_string + ")")
                x += 1
                a += 1
            print("The original entry list, now with all of the generated numbers. Just needs to be put back together.")
            print(dicelist)

            dicelist = "".join(dicelist)

            sum_of_dice = dicelist.replace("multiply", "*")
            print("The finished article.")
            print(sum_of_dice)
            dicelist = str(eval(sum_of_dice))
            print("The sum.")
            print(dicelist)
            dice_holding_pen_2.append(dicelist + " tons.\n") #Eg: " + "**" + special +"**")
            print(dice_holding_pen_2)
            BB += 2

    print("does this work")
    g = 0
    h = 0
    while g < len(dice_holding_pen_2):

        dice_holding_pen[h] = (dice_holding_pen_2[g])
        g += 1
        h += 2

    print(dice_holding_pen)

    p = 2
    m = 0
    while p <= len(trade_list_all):
        trade_list_all[p] = dice_holding_pen[m]
        p += 3
        m += 2

    print(trade_list_all) # now we have the goods, their adjusted costs, and generated tons that are available to buy

    trade_list_string = " ".join(trade_list_all)
    print(trade_list_string)



#A merchant will buy X-goods for Y-price
def selling(*arg):

    user_list = ["XX", "Wa", "Ht"]
    broker_entry = "1"

    master_trade_goods_list = []
    master_trade_goods_list.append(common_electronics)  # 0
    master_trade_goods_list.append(common_industrial)  # 1
    master_trade_goods_list.append(common_manufactured)  # 2
    master_trade_goods_list.append(common_raw)  # 3
    master_trade_goods_list.append(common_consumables)  # 4
    master_trade_goods_list.append(common_ore)  # 5
    master_trade_goods_list.append(advanced_electronics)  # 6
    master_trade_goods_list.append(advanced_machine)  # 7
    master_trade_goods_list.append(advanced_manufactured)  # 8
    master_trade_goods_list.append(advanced_weapons)  # 9
    master_trade_goods_list.append(advanced_vehicles)  # 10
    master_trade_goods_list.append(biochemicals)  # 11
    master_trade_goods_list.append(crystals_gems)  # 12
    master_trade_goods_list.append(cybernetics)  # 13
    master_trade_goods_list.append(animals)  # 14
    master_trade_goods_list.append(luxury_consumables)  # 15
    master_trade_goods_list.append(luxury_goods)  # 16
    master_trade_goods_list.append(medical_supplies)  # 17
    master_trade_goods_list.append(petrochemicals)  # 18
    master_trade_goods_list.append(pharma)  # 19
    master_trade_goods_list.append(polymers)  # 20
    master_trade_goods_list.append(precious_metals)  # 21
    master_trade_goods_list.append(radioactives)  # 22
    master_trade_goods_list.append(robots)  # 23
    master_trade_goods_list.append(spices)  # 24
    master_trade_goods_list.append(textiles)  # 25
    master_trade_goods_list.append(uncommon_ore)  # 26
    master_trade_goods_list.append(uncommon_raw)  # 27
    master_trade_goods_list.append(wood)  # 28
    master_trade_goods_list.append(vehicles)  # 29
    master_trade_goods_list.append(exotics)  # 30
    master_trade_goods_list.append(illegal_bio)  # 31
    master_trade_goods_list.append(illegal_cyber)  # 32
    master_trade_goods_list.append(illegal_drugs)  # 33
    master_trade_goods_list.append(illegal_luxuries)  # 34
    master_trade_goods_list.append(illegal_weapons)  # 35

    print(master_trade_goods_list)

    arg = list(arg)
    print("Is this a list now?")
    print(arg) #arg is a list of items the players wish to sell.

    purchase_list_buying = {
        0: 0.4,
        1: 0.45,
        2: 0.5,
        3: 0.55,
        4: 0.6,
        5: 0.65,
        6: 0.7,
        7: 0.75,
        8: 0.8,
        9: 0.85,
        10: 0.9,
        11: 1,
        12: 1.05,
        13: 1.1,
        14: 1.15,
        15: 1.2,
        16: 1.25,
        17: 1.3,
        18: 1.35,
        19: 1.4,
        20: 1.45,
        21: 1.5,
        22: 1.55,
        23: 1.6,
    }


    selling_list = []
    j = 0
    a = 0

    while j < len(master_trade_goods_list):
        if a >= len(arg):

            j = len(master_trade_goods_list)
        elif arg[a].lower() == (master_trade_goods_list[j].type).lower():
            temp_all_codes = master_trade_goods_list[j].sale_dm_list
            temp_price = master_trade_goods_list[j].base_price
            temp_sale_codes = master_trade_goods_list[j].purchase_dm_list

            selling_list.append(arg[a])
            selling_list.append(temp_price)
            selling_list.append(temp_all_codes)
            selling_list.append(temp_sale_codes)
            j += 0
            a += 1

        elif arg[a] != master_trade_goods_list[j].type:
            print("No")
            j += 1
    print(selling_list)

    new_list = []  # this sees which purchase trade code modifiers need to be added
    maths_list = []
    a = 0
    y = 2
    z = 0

    while y <= len(selling_list):
        if a >= len(user_list):
            print("A is not in XY and is greater than user length")
            y += 4
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
                maths_list.append(11)
        elif user_list[a] == selling_list[y][z]:
            new_list.append(str(selling_list[y][z + 1]))
            a += 1
            z = 0
            print("A is in Y,Z")
            print(new_list)
        elif user_list[a] != selling_list[y][z]:
            z += 2
            print("A is not in Y,Z")
            if z >= len(selling_list[y]):
                a += 1
                z = 0
                print("Resetting Z")
    print("This is the selling list")
    print(maths_list)

    new_list = []
    maths_list_2 = []
    a = 0
    y = 3
    z = 0

    while y <= len(selling_list):
        if a >= len(user_list):
            print("A is not in XY and is greater than user length")
            y += 4
            z = 0
            a = 0
            if len(new_list) >= 1:
                modifier_number_string = "+".join(new_list)
                print(modifier_number_string)
                price_temp = eval(modifier_number_string)
                maths_list_2.append(price_temp)
                new_list.clear()
                print(maths_list_2)
            else:
                maths_list_2.append(0)
        elif user_list[a] == selling_list[y][z]:
            new_list.append(str((selling_list[y][z + 1])))
            a += 1
            z = 0
            print("A is in Y,Z")
            print(new_list)
        elif user_list[a] != selling_list[y][z]:
            z += 2
            print("A is not in Y,Z")
            if z >= len(selling_list[y]):
                a += 1
                z = 0
                print("Resetting Z")
    print("This is the purchase modifier list")
    print(maths_list_2)
    print(maths_list)

    a = 0
    while a < len(maths_list):
        dice_roll = eval(str(random.randint(1, 6)) + "+" + str(random.randint(1, 6)) + "+" + str(random.randint(1, 6)))
        dice_plus_mod = str(dice_roll) + "+" + str(broker_entry) + "-" + str(maths_list_2[a])
        dice_plus_mod = eval(dice_plus_mod)
        temp_number = str(maths_list[a])
        maths_list[a] = (eval((temp_number) + "+" + str(dice_plus_mod)))
        a += 1
        print(maths_list)  # this takes the maths_list and adds the players own modifiers, then runns it through the modifier dict (dice roll and broker skill)

    a = 0
    x = 1
    while x <= len(maths_list):
        x += 1
        replacement = maths_list[a]
        if replacement >= 23:
            b = 1.6
        elif replacement <= 0:
            b = 0.3
        else:
            b = purchase_list_buying.get(replacement)
        maths_list[a] = b
        a += 1
    print(maths_list)  # this gives us the %-based modifiers to tweak the goods base cost. 0.5/1.15 etc

    a = 0
    c = 1
    while a < len(maths_list):
        replacement = float((maths_list[a]))
        selling_list[c] = "- Cr " + str(round(replacement * int(selling_list[c]))) + "/ton.\n"
        a += 1
        c += 4
    print(selling_list)  # this puts the modified prices into the original list.

    b = 2
    while b < len(selling_list):
        selling_list.remove(selling_list[b])
        b += 3
        print("del pls")
    print(selling_list)  # this removes the trade codes

    b = 2
    while b <= len(selling_list):
        selling_list.remove(selling_list[b])
        b += 2
    print(selling_list)  # this removes the 2nd set of trade codes, giving us just item and its cost.

    selling_list_string = " ".join(selling_list)
    print(selling_list_string)


#un-comment one of the lines below to run either the selling or buying functions

#selling("common ore", "wood", "illegal weapons")
#buying("no", 1) 
