""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
    options=["show table","add", "remove","Update","Get oldest person","get person closest to average"]
    table = data_manager.get_table_from_file("hr/persons.csv")
    while True:
        ui.print_menu("Human resources",options,"Main menu")
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
            get_oldest_person(table)
        elif option=="6":
            get_persons_closest_to_average(table)
        elif option=="0":
            break
    

    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    headers=["id","name","birth_year"]
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
    table[-1].append(ui.get_inputs("Type in the name",""))
    table[-1].append(ui.get_inputs("Type in the birth year",""))
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
    userinput_name = ui.get_inputs("Name: ","")
    userinput_year = ui.get_inputs("Birth year: ", "")
    
    for sublist in table:
        if id_ in sublist:
            sublist[0] = common.generate_random(table)
            sublist[1] = userinput_name
            sublist[2] = userinput_year
        
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    oldest_list=[]
    oldest_birth_year=int(table[0][2])
    for i in range(len(table)):
        if int(table[i][2])<oldest_birth_year:
            oldest_birth_year=int(table[i][2])
    for j in range(len(table)):
        if int(table[j][2])==oldest_birth_year:
            oldest_list.append(table[j][1])
    ui.print_result(",".join(oldest_list),"")
    ui.get_inputs("Press Enter to to advance!", "")
    return oldest_list
    


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    ages=[]
    avg=0
    list_of_names=[]
    for i in range(len(table)):
        ages.append(2019-int(table[i][2]))
    closest_to_avg=abs(ages[0]-avg)
    avg=common.avg_of_list(ages)
    for j in range(len(ages)):
        if abs(ages[j]-avg)<closest_to_avg:
            closest_to_avg=abs(ages[j]-avg)
    for k in range(len(table)):
        if abs((2019-int(table[k][2]))-avg)==closest_to_avg:
            list_of_names.append(table[k][1])
    ui.print_result(list_of_names,"")
    ui.get_inputs("Press Enter to to advance!", "")        
    return list_of_names



        

