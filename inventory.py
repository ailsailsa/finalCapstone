# importing tabulate
from tabulate import tabulate


# ========The beginning of the class==========
# defining Shoe class
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
        return [str(self.country), str(self.code), str(self.product), str(self.cost), str(self.quantity)]


# =============Shoe list===========
# empty list to store shoe objects
shoe_list = []


# ==========Functions outside the class==============
# function to read data from txt file and save shoe objects in shoe_list
def read_shoes_data():
    # opening file, reading contents and splitting contents into lists to use to create shoe objects
    with open("inventory.txt", "r") as file:
        inventory_list = file.read()
        inventory_list = inventory_list.split("\n")

    for index in range(0, len(inventory_list)):
        inventory_list[index] = inventory_list[index].split(",")

    # creating shoe objects using each list in inventory_list
    for i in range(1, len(inventory_list)):
        shoe_list.append(Shoe(inventory_list[i][0], inventory_list[i][1], inventory_list[i][2],
                              int(inventory_list[i][3]), int(inventory_list[i][4])))


# function to update the contents of the inventory txt file
def update_txt_file():
    with open("inventory.txt", "r+") as file:
        updated_shoe_list = []
        for shoe in shoe_list:
            shoe = shoe.__str__()
            shoe = ",".join(shoe)

            updated_shoe_list.append(shoe)
        updated_shoe_list = "\n".join(updated_shoe_list)
        file.write("Country,Code,Product,Cost,Quantity\n" + updated_shoe_list)


# function to add a new stock item
def capture_shoes():
    while True:
        input_country = input("Enter country: ")
        input_code = input("Enter product code: ")
        input_product = input("Enter product name: ")
        try:
            input_cost = int((input("Enter cost: ")))
        except ValueError:
            print("You have not entered a valid price. Please try again.")
        try:
            input_quantity = int(input("Enter quantity: "))
        except ValueError:
            print("You have not entered a valid number for the quantity. Please try again.\n")
        if type(input_cost) == int and type(input_quantity) == int:
            break

    shoe_list.append(Shoe(input_country, input_code, input_product, input_cost, input_quantity))
    print("\nYour data has been saved to the inventory list.")

    # writing new data to the text file
    with open("inventory.txt", "a") as file:
        new_stock = f"\n{shoe_list[-1].country},{shoe_list[-1].code},{shoe_list[-1].product}," \
                    f"{shoe_list[-1].cost},{shoe_list[-1].quantity}"
        file.write(new_stock)


# function to view all shoe data in a table
def view_all():
    list_to_tabulate = []
    for item in shoe_list:
        item = item.__str__()
        list_to_tabulate.append(item)
    print(tabulate(list_to_tabulate, headers=["Country", "Code", "Product", "Cost", "Quantity"]))


# function to find low stock
def find_lowest_stock():
    lowest_stock = shoe_list[0].quantity

    for index in range(1, len(shoe_list)):
        if lowest_stock <= shoe_list[index].quantity:
            continue
        elif lowest_stock > shoe_list[index].quantity:
            lowest_stock = shoe_list[index].quantity

        else:
            print("There is an error.")
    return lowest_stock


# function to find high stock
def find_highest_stock():
    highest_stock = shoe_list[0].quantity

    for index in range(1, len(shoe_list)):
        if highest_stock >= shoe_list[index].quantity:
            continue
        elif highest_stock < shoe_list[index].quantity:
            highest_stock = shoe_list[index].quantity

        else:
            print("There is an error.")
    return highest_stock


# function to identify and re-order low stock
def re_stock():
    lowest_stock_num = find_lowest_stock()
    print(f"The lowest quantity found for any shoe in stock is: {lowest_stock_num}\n"
          f"Low stock items:\n")

    for stock in shoe_list:
        if stock.quantity == lowest_stock_num:
            print(stock.__str__())

            while True:
                re_order = input("Would you like to order more of this item (y/n)?")
                re_order = re_order.strip()

                if not re_order == "n" and not re_order == "y":
                    print("You have not entered a valid option. Please try again.")
                    continue
                else:
                    break

            if re_order == "n":
                print(f"No re-stock for {stock.product}.\n")
                break

            elif re_order == "y":
                while True:
                    try:
                        re_stock_qty = int(input("Enter quantity for re-stock: "))
                        break
                    except ValueError:
                        print("You have not entered a valid number. Please try again.")

                stock.quantity = stock.quantity + re_stock_qty
                update_txt_file()
                print(f"You have ordered {re_stock_qty} additional pairs of {stock.product}.\n"
                      f"The total quantity of {stock.product} is now {stock.quantity}.\n\n")
            else:
                print("Returning to main menu.\n\n")


# function to search for a shoe with a product code and print associated data, as well as returning shoe object
def search_shoe():
    while True:
        user_code = input("Enter product code: ")
        shoe_found = False
        for shoe in shoe_list:
            if user_code.strip() == shoe.code:
                shoe_found = True
        if shoe_found:
            break
        else:
            print("You have not entered a valid code. Please try again.")
    shoe_data_list = [["Country", "Code", "Product", "Cost", "Quantity"],
                      [shoe_data.country, shoe_data.code, shoe_data.product, str(shoe_data.cost),
                       str(shoe_data.quantity)]]
    print(tabulate(shoe_data_list, headers="firstrow"))
    print("")
    return shoe


# calculating overall value of stock items
def value_per_item():
    value_list_for_tab = []
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        data_to_print = [shoe.code, shoe.product, value]
        value_list_for_tab.append(data_to_print)
    print(tabulate(value_list_for_tab, headers=["Code", "Product", "Value"]))

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


# function to decide which stock to put on sale
def highest_qty():
    highest_stock = find_highest_stock()
    for shoe in shoe_list:
        if shoe.get_quantity() == highest_stock:
            print(f"The {shoe.product} ({shoe.code}) has the highest stock quantity of {highest_stock}."
                  f" We advise you put this item on sale.\n")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


# ==========Main Menu=============
# main menu for the user
print("Welcome to the Nike Inventory Program")
while True:
    menu = input("Please enter your menu choice:\n"
                 "view all stock data - va\n"
                 "add stock - as\n"
                 "re_stock - rs\n"
                 "search shoe - ss\n"
                 "see value = sv\n"
                 "view highest stock - vhs\n"
                 "exit - e \n")
    menu = menu.strip()
    menu = menu.lower()
    read_shoes_data()

    if menu == "va":
        view_all()

    elif menu == "as":
        capture_shoes()

    elif menu == "rs":
        re_stock()

    elif menu == "ss":
        shoe_data = search_shoe()

    elif menu == "sa":
        value_per_item()

    elif menu == "vhs":
        highest_qty()

    elif menu == "e":
        print("Thank you for using the Nike Inventory Program. Goodbye!")

    else:
        print("You have not entered a valid option. Please try again.")
