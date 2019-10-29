""" Sales module
Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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

            ui.print_result(str(get_items_sold_between(table, frommonth, fromday, fromyear, tomonth, today, toyear)),"")
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
    headers = ["ID", "Title", "Price", "Month", "Day", "Year","Customer ID"]
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

    ID = 0
    TITLE = 1
    PRICE = 2
    MONTH = 3
    DAY = 4
    YEAR = 5

    for sublist in table:
        if id_ in sublist:
            sublist[ID] = common.generate_random(table)
            sublist[TITLE] = userinput_title
            sublist[PRICE] = userinput_price
            sublist[MONTH] = userinput_month
            sublist[DAY] = userinput_day
            sublist[YEAR] = userinput_year
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
    ID = 0
    PRICE = 2
    # your code
    listofprices = []
    result = []
    for sublist in table:
        listofprices.append(int(sublist[PRICE]))

    min = 999999999999999999
    for number in listofprices:
        if min > number:
            min = number

    for sublist in table:
        if str(min) == sublist[PRICE]:
            return sublist[ID]


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
    # vH34Ju#&:ID-0   AudioSurf:Title-1  23:Price-2   6:Month-3   2:Day-4   2016:Year-5

    ID = 0
    TITLE = 1
    PRICE = 2
    MONTH = 3
    DAY = 4
    YEAR = 5

    result = []
    day_from = int(day_from)
    month_from = int(month_from) * 30
    year_from = int(year_from) * 365
    result_from = day_from + month_from + year_from
    day_to = int(day_to)
    month_to = int(month_to) * 30
    year_to = int(year_to) * 365
    result_to = day_to + month_to + year_to

    for sublist in table:
        x = int(sublist[DAY]) + (int(sublist[MONTH]) * 30) + (int(sublist[YEAR]) * 365)
        if x > int(result_from) and x < int(result_to):
            sublist[DAY] = int(sublist[DAY])
            sublist[MONTH] = int(sublist[MONTH])
            sublist[YEAR] = int(sublist[YEAR])
            sublist[PRICE] = int(sublist[PRICE])
            result.append(sublist)
    return result

# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code
    ID = 0
    TITLE = 1

    table = data_manager.get_table_from_file("sales.csv")
    for sublist in table:
        if sublist[ID] == id:
            return sublist[TITLE]
    return None


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    ID=0
    TITLE=1

    for i in range(len(table)):
        if table[i][ID]==id:
            return table[i][TITLE]
    return None


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    MONTH = 3
    DAY = 4
    YEAR = 5

    counter = 0
    day_converted = []

    table = data_manager.get_table_from_file("sales.csv")
    DAYS = 0

    for sublist in table:
        counter +=1
        converted = counter, int(sublist[DAY]) + (int(sublist[MONTH]) * 30) + (int(sublist[YEAR]) * 365)
        day_converted.append(converted)

    maxday = (max(day_converted[DAYS]))

    for tuple in day_converted:
        if maxday in tuple:
            id_of_item = tuple[DAYS]
        for sublist in table:
            return sublist[id_of_item-1]


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    MONTH = 3
    DAY = 4
    YEAR = 5

    counter = 0
    day_converted = []

    DAYS = 0

    for sublist in table:
        counter +=1
        converted = counter, int(sublist[DAY]) + (int(sublist[MONTH]) * 30) + (int(sublist[YEAR]) * 365)
        day_converted.append(converted)

    maxday = (max(day_converted[DAYS]))

    for tuple in day_converted:
        if maxday in tuple:
            id_of_item = tuple[DAYS]
        for sublist in table:
            return sublist[id_of_item-1]


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code
    MONTH = 3
    DAY = 4
    YEAR = 5
    TITLE=1

    counter = 0
    day_converted = []

    DAYS = 0

    for sublist in table:
        converted = int(sublist[DAY]) + (int(sublist[MONTH]) * 30) + (int(sublist[YEAR]) * 365)
        day_converted.append(converted)

    maxday = (max(day_converted))
    for i in range(len(day_converted)):
        if day_converted[i]==maxday:
            break
        counter+=1

    return table[counter][TITLE]


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code
    PRICE = 2
    ID = 0
    list_of_prices=[]
    table = data_manager.get_table_from_file("sales.csv")

    for i in range(len(item_ids)):
        for j in range(len(table)):
            if item_ids[i] == table[j][ID]:
                list_of_prices.append(int(table[j][PRICE]))
    sumnum = 0
    for prices in list_of_prices:
        sumnum += prices
    return sumnum

def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code
    PRICE = 2
    ID = 0
    list_of_prices=[]

    for i in range(len(item_ids)):
        for j in range(len(table)):
            if item_ids[i] == table[j][ID]:
                list_of_prices.append(int(table[j][PRICE]))
    sumnum = 0
    for prices in list_of_prices:
        sumnum += prices
    return sumnum


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code
    table = data_manager.get_table_from_file("sales.csv")

    ID = 0
    CUSTOMER_ID = 6

    for sublist in table:
        if sublist[ID] == sale_id:
            return sublist[CUSTOMER_ID]
    return None


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """
    SALEID=0
    CUSTOMERID=6
    # your code
    for i in range(len(table)):
        if table[i][SALEID]==sale_id:
            return table[i][CUSTOMERID]
    return None


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    table = data_manager.get_table_from_file("sales/sales.csv")
    ID = 6
    set1 = set()
    for sublist in table:
        set1.add(sublist[6])
    return set1



def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code
    ID = 6
    set1 = set()
    for sublist in table:
        set1.add(sublist[6])
    return set1

def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code
    SALEID=0
    CUSTOMERID=6
    table = data_manager.get_table_from_file("sales/sales.csv")
    id_dict={}
    for i in range(len(table)):
        if table[i][CUSTOMERID] in id_dict.keys():
            id_dict[table[i][CUSTOMERID]].append(table[i][SALEID])
        else:
            id_dict.update({table[i][CUSTOMERID]:[table[i][SALEID]]})
    return id_dict



def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code
    SALEID=0
    CUSTOMERID=6
    id_dict={}
    for i in range(len(table)):
        if table[i][CUSTOMERID] in id_dict.keys():
            id_dict[table[i][CUSTOMERID]].append(table[i][SALEID])
        else:
            id_dict.update({table[i][CUSTOMERID]:[table[i][SALEID]]})
    return id_dict


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    SALEID=0
    CUSTOMERID=6
    sum_dict={}
    table = data_manager.get_table_from_file("sales/sales.csv")
    for i in range(len(table)):
        if table[i][CUSTOMERID] in sum_dict.keys():
            sum_dict[table[i][CUSTOMERID]]+=1
        else :
            sum_dict.update({table[i][CUSTOMERID]:1})
    return sum_dict



def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    SALEID=0
    CUSTOMERID=6
    sum_dict={}
    for i in range(len(table)):
        if table[i][CUSTOMERID] in sum_dict.keys():
            sum_dict[table[i][CUSTOMERID]]+=1
        else :
            sum_dict.update({table[i][CUSTOMERID]:1})
    return sum_dict
