#Calculating the tip for one person
# food = float(input("How much is your dinner?: "))
# tip = .20
# calc_p = food*tip
# total = calc_p+food
# print(total)
#this program takes in the cost of food as a float.
#multiplies the cost of food and the tip in calc_p
#the total takes in the tip plus the cost of food. 

# *********************
#A Feast to Remeber
# feast takes in the total input
# Tip_calulation divides the tip by 100 plus the cost of the dinner
# Then we print tip_calculation / friends

# feast = float(input("What\'s the total friend?: "))
# tip_calulation = (float(.31 / 100 + feast))

# friends = 3

# print(tip_calulation / friends)

# *********************
#No Tip 
# no_tip_food takes in the food cost
# hard coded the cheap_skates
# no_tip_total takes in the cost of the food and divides it by the cheap_skates


# no_tip_food = float(input("Your food costs: "))
# cheap_skates = 6
# no_tip_total = no_tip_food / cheap_skates
# print(f"total bill {no_tip_total} cheap skate")

#************************
#Sharing the bill with many
big_dinner = float (input("That\'s a big bill: "))
the_folks = int(input("How many of you are splitting the bill?: "))
tip_calulation = (float(.12 / 100))
split_tip = tip_calulation / the_folks
split_dinner = big_dinner / the_folks

print(f"Dinner for each of you is {split_dinner} if you're kind you each give a tip of {split_tip}")
