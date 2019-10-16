""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
    options = ["Show table","Add","Remove","Update","Year of hightest profit","Average per item profit in a year"]
    table = data_manager.get_table_from_file("accounting/items.csv")
    while True:
        ui.print_menu("Accounting",options,"Back to Main menu")
        inputs = ui.get_inputs("Please enter a number: ","")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option =="3":
            userinput = ui.get_inputs("Enter the ID you want to remove: ", "")
            table = remove(table,userinput)
        elif option == "4":
            userinput_id = ui.get_inputs("Enter the ID you want to update: ", "")
            table = update(table,userinput_id)
        elif option == "5":
            which_year_max(table)
        elif option == "6":
            userinput_year = ui.get_inputs("Enter the year: ", "")
            ui.print_result("The average is: "+str(avg_amount(table,userinput_year)),"")
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
    headers =["ID","Month","Day","Year","Type","Amount"]
    ui.print_table(table,headers)
    ui.get_inputs("Press Enter to to advance!","")

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
    table[-1].append(ui.get_inputs("Type in the month(with number): ", ""))
    table[-1].append(ui.get_inputs("Type in the day: ", ""))
    table[-1].append(ui.get_inputs("Type in the year: ", ""))
    table[-1].append(ui.get_inputs("Type in the type"
                                   "([in] for income or [out] for outflow): ", ""))

    table[-1].append(ui.get_inputs("Type in the amount: ", ""))


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
    userinput_month = ui.get_inputs("Month: ","")
    userinput_day = ui.get_inputs("Day: ", "")
    userinput_year = ui.get_inputs("Year: ", "")
    userinput_type = ui.get_inputs("Type: ", "")
    userinput_amount = ui.get_inputs("Amount: ", "")
    ID = 0
    MONTH=1
    DAY=2
    YEAR=3
    TYPE=4
    AMOUNT=5
      
      
      
      
    for sublist in table:
        if id_ in sublist:
            sublist[ID] = common.generate_random(table)
            sublist[MONTH] = userinput_month
            sublist[DAY] = userinput_day
            sublist[YEAR] = userinput_year
            sublist[TYPE] = userinput_type
            sublist[AMOUNT] = userinput_amount


    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code
    dictionary={}
    year_max=0
    highest_profit=0
    YEAR=3
    TYPE=4
    AMOUNT=5
      
      
    for i in range(len(table)):
        if table[i][YEAR] not in dictionary.keys():
            if table[i][TYPE]=="in":
                dictionary.update({table[i][YEAR]:int(table[i][AMOUNT])})
            if table[i][TYPE]=="out":
                dictionary.update({table[i][YEAR]:(int(table[i][AMOUNT])-(2*int(table[i][AMOUNT])))})
        elif table[i][YEAR] in dictionary.keys():
            if table[i][TYPE]=="in":
                dictionary[table[i][YEAR]]+=int(table[i][AMOUNT])
            if table[i][TYPE]=="out":
                dictionary[table[i][YEAR]]-=int(table[i][AMOUNT])
    for key,value in dictionary.items():
        if value>highest_profit:
            year_max=key
        
    return year_max

    






def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
    listofitems = []

    dic_in={}
    dic_out={}
    counter_in = 1
    counter_out = 1
      
    ID = 0
    MONTH=1
    DAY=2
    YEAR=3
    TYPE=4
    AMOUNT=5
    for sublist in table:
        if sublist[YEAR] == year and sublist[TYPE] == "in":
            counter_in += 1
            dic_in.update({counter_in:sublist[AMOUNT]})

        elif sublist[YEAR] == year and sublist[TYPE] == "out":
            counter_out += 1
            dic_out.update({counter_out:sublist[AMOUNT]})


    for plusz in dic_in.keys():
        for minusz in dic_out.values():
            result = (int(plusz) - int(minusz))
            listofitems.append(result)

    num = 0
    for items in listofitems:
        num += items
    result_new = num / len(dic_in.keys())
    return result_new

