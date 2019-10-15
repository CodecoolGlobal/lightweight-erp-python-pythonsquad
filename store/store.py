""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options = ["Show table", "Add", "Remove", "Update", "Type of games", "Average of games in stock"]
    table = data_manager.get_table_from_file("store/games.csv")
    while True:
        ui.print_menu("Store", options, "Back to Main menu")
        inputs = ui.get_inputs("Please enter a number: ", "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            userinput = ui.get_inputs("Enter the ID you want to remove: ", "")
            table = remove(table, userinput)
        elif option == "4":
            userinput_id = ui.get_inputs("Enter the ID you want to update: ", "")
            table = update(table, userinput_id)
        elif option == "5":
            pass
        elif option == "6":
            userinput_id = ui.get_inputs("Enter the Manufacturer: ", "")
            ui.print_result("The average is: " + str(get_average_by_manufacturer(table, userinput_id)), "")
        elif option == "0":
            break

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    headers = ["ID", "Title", "Manufacturer", "Price", "InStock",]
    ui.print_table(table, headers)
    ui.get_inputs("Press Enter to to advance!", "")

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    table.append([])
    table[-1].append(common.generate_random(table))
    table[-1].append(ui.get_inputs("Type in the Title ", ""))
    table[-1].append(ui.get_inputs("Type in the Manufacturer: ", ""))
    table[-1].append(ui.get_inputs("Type in the Price: ", ""))
    table[-1].append(ui.get_inputs("Type in the InStock: ", ""))
    return table



def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    for sublist in table:
        if id_ in sublist:
            table.remove(sublist)
    ui.get_inputs("Press Enter to to advance!", "")
    return table



def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    userinput_title = ui.get_inputs("Title: ", "")
    userinput_man = ui.get_inputs("Manufacturer: ", "")
    userinput_price = ui.get_inputs("Price: ", "")
    userinput_stock = ui.get_inputs("In Stock: ", "")
    for sublist in table:
        if id_ in sublist:
            sublist[0] = common.generate_random(table)
            sublist[1] = userinput_title
            sublist[2] = userinput_man
            sublist[3] = userinput_price
            sublist[4] = userinput_stock
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
    counter = 0
    listofstock=[]
    for sublist in table:
        if sublist[2] == manufacturer:
            listofstock.append(int(sublist[4]))
    result = common.avg_of_list(listofstock)
    return result

