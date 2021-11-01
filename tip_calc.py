#Calculating the tip for one person
food = float(input("How much is your dinner?: "))
tip = int(input("what's the tip?: "))
tip_percent = tip/100
tax = food*.1
total_tip=food*tip_percent
total_bill = food+tax+total_tip
print(f"this is your total bill {total_bill}")
calc_p = food
tip = 2/100
tax = food*.1
total = calc_p+food
total_bill = total+tip+tax
print(f"this is your total bill {total_bill}")
#this program takes in the cost of food as a float.
#multiplies the cost of food and the tip in calc_p
#the total takes in the tip plus the cost of food. 

# *********************
#A Feast to Remeber
# feast takes in the total input
# Tip_calulation divides the tip by 100 plus the cost of the dinner
# Then we print tip_calculation / friends


food = float(input("How much is your dinner?: "))
tip = int(input("what's the tip?: "))
num_of_ppl = int(input("How many folks splitting the tab?\n"))
tip_percent = tip/100
tax = food*.1
total_tip=food*tip_percent
total_bill = food+tax+total_tip
bill_split1 = total_bill/num_of_ppl
final_bill = round(bill_split1, 2)

print(f"this is your total bill {total_bill}")
print(f"each person pays{final_bill}")
# *********************
#No Tip 

food = 5000
tax = food*.1
print(tax)
tip = .12*food
print(tip)
num_of_ppl = 876
tip_percent = tip/100
total_tip=food*tip_percent
print(total_tip)
total_bill = food+tax
print(total_bill)
bill_split1 = total_bill/num_of_ppl
final_bill = (bill_split1)

print(f"this is your total bill {total_bill}")
print(f"each person pays{final_bill}")

# food variable takes in the amount of the bill. 
# the tax is multiplied and added in line 48. The 
# bill is totaled and divided by the number of people.
# However, I can't seem to get the same amount provded in 
# the instructions.  




#************************
#Sharing the bill with many
# 
