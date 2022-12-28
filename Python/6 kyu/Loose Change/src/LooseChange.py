import math

def loose_change(cents):
    
    coins = { "Pennies" : 1, "Nickels": 5, "Dimes": 10, "Quarters": 25 }
    
    Nickels = 0
    Pennies = 0
    Dimes = 0
    Quarters = 0
    
    change = {"Nickels": Nickels, "Pennies": Pennies, "Dimes": Dimes, "Quarters": Quarters}
    
    if cents <= 0:

        return  change 

    for i in range(math.ceil(cents)):

        if cents >= coins["Quarters"]:
        
            cents = cents - coins["Quarters"]
            change["Quarters"] += 1
        
        elif cents >= coins["Dimes"]:

            cents = cents - coins["Dimes"]
            change["Dimes"] += 1

        elif cents >= coins["Nickels"]:

            cents = cents - coins["Nickels"]
            change["Nickels"] += 1

        elif cents >= coins["Pennies"]:
            
            cents = cents - coins["Pennies"]
            change["Pennies"] += 1

        else:

            return change