""" Common module
implement commonly used functions here
"""

import random

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """


    # your code
    char = [
            ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
            ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
            [1,2,3,4,5,6,7,8,9,0],
            ["+","#","!","%","/","=","(",")","?",".","-","_","@",],
            ]
    l = []

    # j H 3 4 J u # &  <---  ID example for myself
    while True:
        special_one = random.randint(0, 11)
        special_two = random.randint(0, 11)

        lower_one = random.randint(0,25)
        lower_two = random.randint(0,25)

        upper_one = random.randint(0,25)
        upper_two = random.randint(0,25)

        number_one = random.randint(0,9)
        number_two = random.randint(0, 9)
        
        FIRST_LIST=0
        SECOND_LIST=1
        THIRD_LIST=2
        FOURTH_LIST=3

        l.append(char[FIRST_LIST][lower_one])
        l.append(char[SECOND_LIST][upper_one])
        l.append(str(char[THIRD_LIST][number_one]))
        l.append(str(char[THIRD_LIST][number_two]))
        l.append(char[SECOND_LIST][upper_two])
        l.append(char[FIRST_LIST][lower_two])
        l.append(char[FOURTH_LIST][special_one])
        l.append(char[FOURTH_LIST][special_two])
        generated = "".join(l)
        if generated in table:
            continue
        else:
            return generated
        
        
def sum_of_list(list):
    ''' takes a list as a parameter and return the sum of it'''
    result = 0
    for elem in list:
        result +=elem
    return result


def avg_of_list(list):
    ''' takes a list as a parameter and return the avg of it'''
    num = 0
    for element in list:
        num += element
    return num/len(list)






