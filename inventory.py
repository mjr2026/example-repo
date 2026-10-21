#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (
            f"Item: {self.product}. Quantity: {self.quantity}."
            f" Cost: {self.cost}. Country: {self.country}. Code: {self.code}."
        )


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt") as file:
            lines = file.readlines()
            for line in lines[1:]:
                if line.strip() == "":
                    continue
                shoe_specs = line.split(",")
                shoe = Shoe(shoe_specs[0], shoe_specs[1], shoe_specs[2], float(shoe_specs[3]), int(shoe_specs[4]))
                shoe_list.append(shoe) 
    except FileNotFoundError:
        print("This file cannot be found. Please try again.")


def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product information: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)


def view_all():
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Here is the shoe with the lowest quantity: {lowest_shoe}.")
    user_question = input("Do you want to restock this shoe? yes/no: ")
    if user_question.lower() == "yes":
        number_to_add = int(input("Enter how many more to add: "))
        lowest_shoe.quantity += number_to_add
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n") 
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


def search_shoe():
    shoe_search = input("Please enter the shoe code you want to find: ")
    for shoe in shoe_list:
        if shoe.code == shoe_search:
            return(shoe) 
    print("This code has not been found.") 


def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} and total value {value}.") 


def highest_qty():
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"This shoe is for sale: {highest_shoe}.")


read_shoes_data()

#==========Main Menu=============
while True:
    try:
        user_choice = int(
        input(
            """\nWould you like to:
    1. Enter a new shoe into the database
    2. View all the shoes currently in the database
    3. Find the shoe with the lowest quantity
    4. Find a shoe based on its code 
    5. Find the value of each shoe
    6. Find the shoe with the highest quantity 
    7. Quit 

    Enter selection: """
        )
    )

    except ValueError:
        print("Please try again.")
        continue 

    if user_choice == 1:
        capture_shoes()
        
    elif user_choice == 2:
        view_all()
    
    elif user_choice == 3:
        re_stock()
        
    elif user_choice == 4:
        discovered_shoe = search_shoe()
        if discovered_shoe is not None:
            print(discovered_shoe)
        
    elif user_choice == 5:
        value_per_item()
        
    elif user_choice == 6:
        highest_qty()

    elif user_choice == 7:
        break

    else:
        print("Please try again: ")