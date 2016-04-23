#!/usr/bin/env python3
"""
    First Bank of Matratze

    Program allows the user to enter in a number of different types of
    US Coinage, which are contained in a number of bags.  Each bag is
    stuffed under a mattress.  For undisclosed purposes, one bag is
    labeled as a "Bugout-Bag", ready to go at a moment's notice.  One
    option of the program is to bug out, which quits the program.

"""
import random

class Coin:
    """ Coin Class which represents the following attributes of a coin:
            1) Name - The name used to refer to the coin denomination
            2) Denomination - The monetary value of a single coin
            3) Count - The number of coins
    """
    def __init__(self, name="default", denom=0, count=0):
        self.name = name
        self.denom = denom
        try:
            self.count = int(count)
            if self.count < 0:
                raise print("Error: Can't have bag with a negative" +
                    " number of coins")
        except ValueError as ce:
            print("Error: Could not determine number of coins")
            raise

    def get_name(self):
        return self.name

    def get_denom(self):
        return self.denom

    def get_count(self): 
        return self.count

    def __str__(self):
        coin_str = str(self.name) + " " + str(self.denom) +\
                   " " + str(self.count)
        return coin_str
"""
    Fun fact: a collection of coins of one denomination is a type set
"""
class Bag:
    """ Bag Class which represents the following attributes of a bag:
            1) Name - The unique name
            2) Type Sets - Collections of coins, each set is of a
                particular denomination
            3) Bag Value - The total monetary value of all the coins
                contained within the bag
    """
    def __init__(self, name="default", type_sets="default"):
        self.name = name
        coin_names = ["quarter","dime","nickel","penny"]
        coin_denoms = [25,10,5,1]
        self.type_sets = []
        try:
            coin_counts = type_sets.split()
            if len(coin_counts) != 4:
                raise ValueError("Error: Could not determine number" +
                    " of coins")
            
            for a, b, c in zip(coin_names, coin_denoms, coin_counts):
                self.type_sets.append(Coin(a,b,c))
                
        except ValueError as ce:
            print(ce)
            raise
           
    def get_bag_name(self):
        return self.name

    def get_bag_denoms(self):
        return coin_names
    
    def get_bag_coins(self):
        type_set_strs = []
        type_set_strs_len = 0
        bag_coins_str = ""
        denom_cnt = 0
        for i in self.type_sets:
            if i.count != 0:
                if i.count > 1:
                    noun_type = "s"
                    if i.name == "penny":
                        i.name = "pennie"
                else:
                    noun_type = ""
                    
                type_set_strs.append("{0} {1}{2}".format(str(i.count),
                    str(i.name),noun_type))

        type_set_strs_len = len(type_set_strs)
        if type_set_strs_len == 0:
            bag_coins_str = "nothing"
        if type_set_strs_len > 2:
            comma = ", "
        else:
            comma = ""
        for j in range(type_set_strs_len):
            if (type_set_strs_len - j) == 1 and type_set_strs_len != 1:
                bag_coins_str += " and "
                comma = ""
            bag_coins_str += type_set_strs[j] + "{0}".format(comma)
        
        return bag_coins_str 
    
    def add_coins(self, other):
        x = 0
        for i in self.type_sets:
            new_count = i.get_count() + other.type_sets[x].get_count()
            i.count = new_count
            x += 1
     
    #Calculate the value of all the coins in the bag
    def get_bag_value(self):
        bag_total = 0
        for i in self.type_sets:
            bag_total += i.get_denom() * i.get_count()
        bag_total = float(bag_total)/100
        fmt_bag_total = "{0:.2f}".format(bag_total)
        return fmt_bag_total

    def __str__(self):
        bag_str = str(self.name) + " " + str(self.get_bag_value())
        return bag_str

"""
    Provide the balance of all the bags stored under the mattress along
    with the overal total.  The bags are displayed by value (lowest to 
    highest) with the exception of the bugout-bag which will always 
    appear first.
"""
def balance():
    global running_total
    max_name_length = 10    #Bugout-Bag is 10 in length
    max_value_length = 5    #Total is 5 in length
    bag_dict = {}

    #Determine the max name and value lengths for all bags for the
    #    purpose of formating the display.  In addition, calculate
    #    the running total of all the bags deposited
    for i in mattress:
        bag = mattress.get(i)
        bag_value = bag.get_bag_value()
              
        bag_length = len(bag.name)
        if bag_length > max_name_length:
            max_name_length = bag_length

        #The largest value is the running total
        value_str = str(running_total)   
        value_length = len(value_str)
        if value_length > max_value_length:
            max_value_length = value_length
        max_length = max_name_length + max_value_length   

     
        #Set the bugout-bag to the side before sorting
        if bag.name != "Bugout-Bag":
            bag_dict[bag.name] = bag_value
            
        if bag.name == "Bugout-Bag":
            tmp_tuple = (bag.name, bag_value)
             
    #Used PEP 265, to sort the bags sans bugout-bag
    bags = [(v, k) for k,v in bag_dict.items()]
    bags.sort()
    bags = [(k,v) for v, k in bags]
    bags.insert(0, tmp_tuple)

    #Display the sorted bags with their balances and the overall total
    #    under the mattress - PEP3101
    #line = "{0:{2}} {1:>}"
    line = "{0:<{2}}" + " {1:>{3}}"
    value_line = "${0:>.2f}"
    for i in bags:
        bag_name_str = i[0] + ":"
        value_str = value_line.format(float(i[1]))
        
        fmt_line = line.format(bag_name_str, value_str, max_name_length,
                               max_length)
        if len(i[0]) < max_name_length:
            fmt_line = line.format(bag_name_str, value_str,
                                   max_name_length + 1, max_length)
            
        print(fmt_line)
    total_value_str = value_line.format(float(running_total))    
    print(line.format("Total:", total_value_str, max_name_length+1,
                      max_length))    
    print()

"""
    Deposit function which creates a bag and validates the uniqueness
    of the bag name and values of the coins supplied by the user 
    before bag is deposited under the mattress.

    If the user provides the name of a bag already in existence or no 
    name at all, generate a pseudorandom name for the bag.
"""     
def deposit():
    global running_total
    
    #Create a unique bag
    def create_bag():
        bag_name = input("Enter name of deposited bag: ")
        
        #Generate a pseudorandom bag name 
        if len(bag_name) == 0:
            bag_name = "Bag #" + str(random.randint(0,9))
        if bag_name in mattress:   
           rand_str = str(random.randint(0,9))
           bag_name += rand_str
        try:
            coinage = input("Enter number of quarters, dimes, " +\
                            "nickels, and pennies: ")
            new_bag = Bag(bag_name, coinage)
        except ValueError:
            raise   
        return(new_bag)

    #Deposit bag under the mattress
    try:
        deposit_bag = create_bag()
        mattress.update({deposit_bag.get_bag_name() : deposit_bag})
        running_total += float(deposit_bag.get_bag_value())
        print("Bag Deposited.\n")
    except ValueError as name_err:
        print("Bag Not Deposited.\n")
    except TypeError as type_err:
        print("Bag Not Deposited.\n")

"""
    Transfer function which allows the user to transfer the entirity of
    one bag into another and destroy the empty bag.
"""
def transfer():
    try:
        from_bag = input("Enter name of bag to transfer from: ")
        to_bag = input("Enter name of bag to transfer into: ")

        #Ensure bags aren't the same
        if from_bag == to_bag:
            raise ValueError("Error: Unable to transfer bag as" +\
                " transfer from and to are the same.\n")
        #Make sure the transfer from is not Bugout-Bag
        if from_bag == "Bugout-Bag":
            raise ValueError("Error: May not transfer Bugout-Bag" +\
                " into another bag.\n")
        #Transfer coins                            
        mattress[to_bag].add_coins(mattress[from_bag])

        #Display the dollar amount transferred
        bag_value = float(mattress[from_bag].get_bag_value())
        print("${0:.2f} Transferred.\n".format(bag_value))

        #Remove the bag from mattress
        mattress.pop(from_bag)
    except KeyError as ke:
        print("Error: Bag doesn't exist.\n")
    except ValueError as name_err:
        print(name_err)

"""
    Withdrawal function allows the user to completely remove a bag
    from the mattress, except the "Bugout-Bag".  
"""
def withdrawal():
    global running_total    
    try:
        withdrawl_bag = input("Enter name of bag to withdraw: ")

        #Check if bag exists and not the Bugout-Bag
        if withdrawl_bag == "Bugout-Bag":
            raise ValueError("Error: May not withdraw.\n")

        #Display the bag coins withdrawn
        bag_coins_str = ""
        type_sets = mattress[withdrawl_bag].get_bag_coins()
        print(type_sets + " withdrawn\n")
               
        #Remove the bag from mattress
        running_total -= float(mattress[withdrawl_bag].get_bag_value())
        mattress.pop(withdrawl_bag)       
    except KeyError as ke:
        print("Error: Bag doesn't exist.\n")
    except ValueError as name_err:
        print(name_err)

"""
    Flee!!!!!!!!! User had withdrawn their "Bugout-Bag"
"""
def flee():
    global running_total    
    running_total -= float(mattress["Bugout-Bag"].get_bag_value())
    
    #Display the bag coins withdrawn
    bag_coins_str = ""
    type_sets = mattress["Bugout-Bag"].get_bag_coins()

    line = "You have fled the country, leaving ${0:.2f} behind\n" +\
    "You took {1} with you."
    print(line.format(running_total,type_sets))
               
    #Remove the bag from mattress
    mattress.pop("Bugout-Bag")
    
    exit(0)

def menu():
    try:
        print("Choose an option:\n" +\
        "   1) Balance Inquiry\n" +\
        "   2) Deposit\n" +\
        "   3) Transfer\n" +\
        "   4) Withdrawal\n" +\
        "   5) Flee the Country\n")
                       
        #Map the inputs to the functions
        menu_options = {1 : balance,
            2 : deposit,
            3 : transfer,
            4 : withdrawal,
            5 : flee}

        while True:
            option = int(input("> "))
            if option < 1 or option > 5:
                raise ValueError 
            execute = menu_options[option]()
    except ValueError as err:
        menu()

#Main
#Initialize what's under the mattress
running_total = 0.0        
mattress = {}
mattress.update({"Bugout-Bag" : Bag("Bugout-Bag","0 0 0 0")})

#Allow the user to perform an action
print("Welcome to Erste Bank der Matratze\n")
menu()
    
