""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
    options=["show table","add", "remove","Update","Get the id connected to the longest name","Get subscribed customers"]
    table = data_manager.get_table_from_file("crm/customers.csv")
    while True:
        ui.print_menu("Customer Relationship Management",options,"Main menu")
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
            ui.print_result(get_longest_name_id(table),"")
        elif option=="6":
            ui.print_result(get_subscribed_emails(table),"")
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
    headers=["id","name","email","subscribed"]
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
    table[-1].append(ui.get_inputs("Type in the email address: ",""))
    table[-1].append(ui.get_inputs("Is he/she subscribed?(0/1): ",""))
    
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
    userinput_email = ui.get_inputs("Email:  ","")
    userinput_subbed = ui.get_inputs("Subscribed? (0/1): ","")
    for sublist in table:
        if id_ in sublist:
            sublist[0] = common.generate_random(table)
            sublist[1] = userinput_name
            sublist[2] = userinput_email
            sublist[3] = userinput_subbed

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code
    Longest_id=""
    longest_length=0
    dictionary={}
    for i in range(len(table)):
        if len(table[i][1])>longest_length:
            longest_length=len(table[i][1])
    for j in range(len(table)):
        if len(table[j][1])==longest_length:
            dictionary.update({table[j][0]:table[j][1]})
    longest_name=""
    temp=0
    for key,value in dictionary.items():
        if temp==0:
            longest_name=value
            temp+=1
        elif value>longest_name:
            longest_name=value
            longest_id=key
    ui.get_inputs("Press Enter to to advance!", "")
    return longest_id


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
    subscribed_str=""
    subscribed_list=[]
    for i in range(len(table)):
        if table[i][3]=="1" and i!=(len(table)-1):
            subscribed_str=subscribed_str+table[i][2]+";"+table[i][1]+","
        elif table[i][3]=="1" and i==(len(table)-1):
            subscribed_str=subscribed_str+table[i][2]+";"+table[i][1]
    subscribed_list=subscribed_str.split(",")
    subscribed_list.remove('')
    ui.get_inputs("Press Enter to to advance!", "")
    return subscribed_list