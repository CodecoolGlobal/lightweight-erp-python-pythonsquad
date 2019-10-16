""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
    options=["show table","add", "remove","Update","Get available items","Get average durability times"]
    table = data_manager.get_table_from_file("inventory/inventory.csv")
    while True:
        ui.print_menu("Inventory",options,"Main menu")
        inputs=ui.get_inputs("Please enter a number:","")
        option = inputs[0]
        if option=="1":
            show_table(table)
        elif option=="2":
            table = add(table)
            #data_manager.write_table_to_file(table, "hr/persons.csv")
        elif option=="3":
            userinput = ui.get_inputs("Enter the ID you want to remove: ", "")
            table =remove(table,userinput)
        elif option=="4":
            userinput_id = ui.get_inputs("Enter the ID you want to update: ", "")
            update(table,userinput_id)
        elif option=="5":
            userinput_id = ui.get_inputs("Enter the year: ", "")
            ui.print_result(get_available_items(table, userinput_id),"")
        elif option=="6":
            ui.print_result(get_average_durability_by_manufacturers(table),"")
        elif option=="0":
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
    headers=["id","name","manufacturer","purchase year", "durability"]
    ui.print_table(table,headers)
    ui.get_inputs("Press a button to advance!","")


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
    table[-1].append(ui.get_inputs("Type in the name: ",""))
    table[-1].append(ui.get_inputs("Type in the manufacturer: ",""))
    table[-1].append(ui.get_inputs("Type in the purchase year: ",""))
    table[-1].append(ui.get_inputs("Type in the durability",""))
    
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
    userinput_name = ui.get_inputs("Type in the name: ","")
    userinput_manufacturer = ui.get_inputs("Type in the manufacturer:  ", "")
    userinput_purchase = ui.get_inputs("Type in the purchase year:  ", "")
    userinput_durability = ui.get_inputs("Type in the durability","")

    
    for sublist in table:
        if id_ in sublist:
            sublist[0] = common.generate_random(table)
            sublist[1] = userinput_name
            sublist[2] = userinput_manufacturer
            sublist[3] = userinput_purchase
            sublist[4] = userinput_durability

    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code
    available_items=[]
    DURABILITY_COL=4
    YEAR_COL=3
    ITEM_COL=1
    for i in range(len(table)):
        if int(table[i][DURABILITY_COL])+int(table[i][YEAR_COL])>=int(year) and int(year)>=int(table[i][YEAR_COL]):
            available_items.append(table[i])

    return available_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
    avg_durability={}
    DURABILITY_COL=4
    MANUFACTURER_COL=2
    temp=0
    
    for i in range(len(table)):
        if table[i][MANUFACTURER_COL]not in avg_durability.keys():
            sum_dur=0
            counter=0
            avg=0
            for j in range(len(table)):
                if table[i][MANUFACTURER_COL]==table[j][MANUFACTURER_COL]:
                    sum_dur+=int(table[j][DURABILITY_COL])
                    counter+=1
            avg=sum_dur/counter
            avg_durability.update({table[i][MANUFACTURER_COL]:avg})
    return avg_durability


