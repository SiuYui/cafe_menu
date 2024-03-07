# If the input from the user is invalid, prompt error and request for input again
def get_valid_input(answer, data_type):
    while True:
        try:
            response = data_type(input(answer))
            return response
        except ValueError:
            print("Invalid Entry.")

# If the input value from the user is negative, prompt error and request for input again
def positive_input(answer, data_type):
    while True:
        response = get_valid_input(answer, data_type)
        try:
            if response < 0:
                raise ValueError("Input cannot be negative.")
        except ValueError as return_statement:
            print(return_statement)
        else:
            return response
# Check if the input from user are not in list, prompt error and request for input again
def item_in_list(answer, item_type):
    while True:
        response = input(answer).strip().capitalize()
        if response not in item_type:
            print("Item not found.")
            continue
        else:
            return response

'''
This is the program to record items sell in the cafe and its' stocks, prices and total values
Defined Functions are used when running the programme.
'''
def add_item(menu, stock, price):
    '''
    This defined function is used for adding new items sell in the cafe
    Requesting the user to input a new item and check the validity of the input
        Using While Loop to ask for the input of its stock and price
            prompt the error if input is invalid and 
            continue 
        until the input is a valid 
            then stop
    '''
    new_item = input("\nPlease enter an item sold in the cafe: ").strip().capitalize()

# Add the item to list if it is not in the existing menu and the item's name is valid:
    if new_item not in menu and len(new_item) > 0 and new_item.isdigit() is False:
        menu.append(new_item)

# Add "new_item" as a key, "item_stock" and "item_price" as a value to dictionary
        item_stock = positive_input(f"Please enter the number of stock of {new_item}: ", int)
        stock[new_item] = item_stock
        item_price = positive_input(f"Please enter the price of {new_item}: ", float)
        price[new_item] = item_price
        
# Output a message to user if error occurred
    elif len(new_item) == 0 or new_item.isdigit() is True:
        print("Please input a valid entry.")
    else:
        print("Item already exist. Please choose 2 for updating the stock.")
        
def updating_menu(stock):
    '''
    This defined function is to update the number of items' stock
    Using While Loops for requesting the user to input an item that the stock need to be added and 
        If the input not match with item in menu,
            return an error message to user and continue
        until the input is valid
        then stop
    Using While Loop to ask for the input of the number of stocks is added 
        prompt the error if input is invalid and 
        continue 
    until the input is a valid 
        then stop
    '''
    revised_item = item_in_list("Please enter the item in menu you have to update: ", stock)
                                
# If the input from the user is invalid, prompt error and request for input again
    revised_stock = positive_input(
                f"Please enter the number of stock of {revised_item} you would like to add: ", int)                      

# Find the "revised_item" in dictionary and add the "revised_stock" to the particular value
    if revised_item in stock:
        stock[revised_item] += revised_stock


def updating_price(price):
    '''
    This defined functions for updating the item's price
    Using While Loop to ask for input of the item in menu that need to be updated
    if item not in menu
        prompt the message and continue
    until the inputted item is in menu then stop
    
    Using While Loop to ask for input of the number of stock need to be add
    if the input is not in number or positive
        prompt error and continue
    until the input is a positive number then stop
    add the number to relevant item
    '''
    revised_item = item_in_list("Please enter the item you have to update: ", price)
                                
# If the input from the user is invalid, prompt error and request for input again
    revised_price = positive_input(f"Please enter the updated price of {revised_item}: ", float)

# Find the "revised_item" in dictionary and replace the "revised_price" to the particular value
    if revised_item in price:
        price[revised_item] = revised_price

def stock_value(menu, stock, price):
    '''
    This is a function to display stock, price and total value of the items sell in the cafe
    Using For Loops to go through all values in the dictionary "stock" 
        with reference to the value in "stock" to get the name of item, number of stock and price
        and using f-string to output the information
    Using For Loops to calculate the total value of stock:
        Number of stock multiply by the item's price and then sum together
    Output the result
    '''
    item_list = ""
    count = -1
    print(f"\n{'Menu' : <25}{'Stock' :<10}{'Price' :<10}")
    for item in stock.values():
        count += 1
        for element in range(count, count +1):
            item_list += f"{menu[element] : <25}"
        item_list += f"{str(item) : <10}{str(price.get(menu[element])):<10}\n"
    print(item_list)
    total_stock = sum(stock[value] * price[value] 
                      for value in price)
    print(f"The total stock value is {total_stock}.")
    
def main():
    '''
    To ask for input item to menu and display item, stock and price to user
        by calling an appropriate defined function
    Display an option menu for user to add item to menu or stop the programme
    '''
# Create empty list and dictionaries for later execution
# Calling the defined function until there are 4 items in "menu"
    menu = []
    stock = {}
    price = {}
    while len(menu) < 4:
        add_item(menu, stock, price)

# Calling the defined function to display detailed information
# Using While Loop to check the validity of input and
# Output the result depending on the input entered by the user
    while True:
        stock_value(menu, stock, price)
        option_menu = input(
            "\nDo you want to updating the menu?  Please select an option below:\n\
            1: Add menu\n\
            2: Updating stock\n\
            3: Updating price \n\
            0: Exit\n"
            "Your choice: ")
        if option_menu == "1":
            add_item(menu, stock, price)
        elif option_menu == "2":
            updating_menu(stock)
        elif option_menu == "3":
            updating_price(price)
        elif option_menu == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid Entry")        

if __name__ == "__main__":
    main()