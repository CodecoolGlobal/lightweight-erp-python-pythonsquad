"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options=["Last buyer's name","Last buyer's ID","The most money spent with name","The most money spent with ID","The most frequent buyer's name","The most frequent buyer's ID"]
    while True:
        ui.print_menu("Data analyser",options,"Main menu")
        inputs=ui.get_inputs("Please enter a number:","")
        option = inputs[0]
        if option=="1":
            ui.print_result(get_the_last_buyer_name(),"")
        elif option=="2":
            ui.print_result(get_the_last_buyer_id(),"")
        elif option=="3":
            ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(),"")
        elif option=="4":
            ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(),"")
        elif option=="5":
            ui.print_result(get_the_most_frequent_buyers_names(num=1),"")
        elif option=="6":
            ui.print_result(get_the_most_frequent_buyers_ids(num=1),"")
        elif option=="0":
            break


    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # your code
    last_sold_item_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(last_sold_item_id)
    name = crm.get_name_by_id(customer_id)
    return name


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # your code
    last_sold_item_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(last_sold_item_id)
    return customer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # your code
    FIRST = 0
    ID = 1
    cmr_price = []
    list_of_prices=[]
    all_IDs = sales.get_all_sales_ids_for_customer_ids()
    
    for key, value in all_IDs.items():
        cmr_price.append((crm.get_name_by_id(key), sales.get_the_sum_of_prices(value)))

    maxnum = cmr_price[FIRST][ID]

    for tuple in cmr_price:
        list_of_prices.append(tuple[ID])
    maxnum = max(list_of_prices)

    for cmr in cmr_price:
        if cmr[ID] == maxnum:
            return cmr

def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code
    FIRST = 0
    PRICE = 1
    cmr_price = []
    list_of_prices = []
    customer_sales = sales.get_all_sales_ids_for_customer_ids()

    for key, value in customer_sales.items():
        cmr_price.append((key, sales.get_the_sum_of_prices(value)))

    maxnum = cmr_price[FIRST][PRICE]

    
    for tuple in cmr_price:
        list_of_prices.append(tuple[PRICE])
        
    maxnum = max(list_of_prices)
    
    for cmr in cmr_price:
        if cmr[PRICE] == maxnum:
            return cmr



def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code
    sales_dict=sales.get_all_sales_ids_for_customer_ids()
    sales_keys=[]
    sales_names=[]
    for keys in sales_dict.keys():
        sales_keys.append(keys)
    for key in sales_keys:
        sales_names.append(crm.get_name_by_id(key))
    buyer_names=[]
    #for i in range (len(sales_dict.values())):
    for i in range(num):
        buyer_names.append((sales_names[i],len(sales_dict[sales_keys[i]])))
    return buyer_names
    



def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
    sales_dict=sales.get_all_sales_ids_for_customer_ids()
    sales_keys=[]
    for keys in sales_dict.keys():
        sales_keys.append(keys)
    buyer_ids=[]
    #for i in range (len(sales_dict.values())):
    for i in range(num):
        buyer_ids.append((sales_keys[i],len(sales_dict[sales_keys[i]])))
    return buyer_ids
