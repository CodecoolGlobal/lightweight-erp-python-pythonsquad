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


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # your code
    prices = []

    all_IDs = sales.get_all_sales_ids_for_customer_ids()
    
    ID=1
    FIRST=0
    
    for customer, sale in all_IDs.items():
        prices.append((crm.get_name_by_id(customer), sales.get_the_sum_of_prices(sale)))

    biggest_spent = prices[FIRST][ID]

    for price in prices:
        if price[ID] > biggest_spent:
            biggest_spent = price[ID]
            
    for customer in prices:
        if customer[ID] == biggest_spent:
            return customer

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
    prices = []
    
    FIRST = 0
    PRICE = 1

    customer_sales = sales.get_all_sales_ids_for_customer_ids()

    for customer, sale in customer_sales.items():
        prices.append((customer, sales.get_the_sum_of_prices(sale)))

    biggest_spent = prices[FIRST][PRICE]

    SECOND=1

    for price in prices:
        if price[SECOND] > biggest_spent:
            biggest_spent = price[SECOND]

    for customer in prices:
        if customer[SECOND] == biggest_spent:
            return customer

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
