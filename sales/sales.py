""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    options = ["Show table", "Add", "Remove", "Update", "Lowest price ID", "Sold between two given dates"]
    table = data_manager.get_table_from_file("sales/sales.csv")
    while True:
        ui.print_menu("Sales", options, "Back to Main menu")
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
            ui.print_result("The ID is: " + str(get_lowest_price_item_id(table)), "")
        elif option == "6":
            frommonth = ui.get_inputs("Enter the first month you want to update: ", "")
            fromday = ui.get_inputs("Enter the first day you want to update: ", "")
            fromyear = ui.get_inputs("Enter the first year you want to update: ", "")

            tomonth = ui.get_inputs("Enter the second month you want to update: ", "")
            today = ui.get_inputs("Enter the second day you want to update: ", "")
            toyear = ui.get_inputs("Enter the second year you want to update: ", "")

            ui.print_result(str(get_items_sold_between(table,frommonth,fromday,fromyear,tomonth,today,toyear)), "")
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
    headers = ["ID", "Title", "Price", "Month", "Day", "Year"]
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
    table[-1].append(ui.get_inputs("Type in the Price: ", ""))
    table[-1].append(ui.get_inputs("Type in the Month: ", ""))
    table[-1].append(ui.get_inputs("Type in the Day: ", ""))
    table[-1].append(ui.get_inputs("Type in the Year: ", ""))
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
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    userinput_title = ui.get_inputs("Title: ", "")
    userinput_price = ui.get_inputs("Price: ", "")
    userinput_month = ui.get_inputs("Month: ", "")
    userinput_day = ui.get_inputs("Day: ", "")
    userinput_year = ui.get_inputs("Year: ", "")
    for sublist in table:
        if id_ in sublist:
            sublist[0] = common.generate_random(table)
            sublist[1] = userinput_title
            sublist[2] = userinput_price
            sublist[3] = userinput_month
            sublist[4] = userinput_day
            sublist[5] = userinput_year
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code
    listofprices=[]
    result =[]
    for sublist in table:
        listofprices.append(int(sublist[2]))

    min=999999999999999999
    for number in listofprices:
        if min > number:
            min = number

    for sublist in table:
        if str(min) == sublist[2]:
            return sublist[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code

    # vH34Ju#&:ID-0   AudioSurf:Title-1  23:Price-2   6:Month-3   2:Day-4   2016:Year-5

    result=[]
    day_from = int(day_from)
    month_from = int(month_from) * 30
    year_from = int(year_from) * 365
    result_from = day_from + month_from + year_from
    day_to = int(day_to)
    month_to = int(month_to) * 30
    year_to = int(year_to) * 365
    result_to = day_to + month_to + year_to
    for sublist in table:

        x = int(sublist[4])+(int(sublist[3])*30)+(int(sublist[5])*365)
        if x >= int(result_from) and x <= int(result_to):
            result.append(sublist[1])
    return result





