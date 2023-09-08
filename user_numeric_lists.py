"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics


# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
list_A = [
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
    
]
logger.info(f" list_A is {list_A}")

list_X = [10,10,45,34,88,40,34,66,80,70]
logger.info(f"list_x is {list_X}")
print(f"list_x is {list_X}")

list_y = [
    45,
    32,
    23,
    11,
    12,
    14,
    78,
    67,
    56,
    48,
]
logger.info(f" list_y is {list_y}")

# TODO: define some custom functions
def list_statistics():
    mean = statistics.mean(list_A)
    median = statistics.median(list_A)
    mode = statistics.mode(list_A)

    logger.info(f"mean of list_A is {mean} ")
    logger.info(f"median of list_A is {median}")
    logger.info(f"mode of list_A is {mode}")

    print(f"mean of list_A is {mean} ")
    print(f"median of list_A is {median}")
    print(f"mode of list_A is {mode}")

    var =statistics.variance(list_A)
    stdev = statistics.stdev(list_A)


    logger.info(f"variance of list_A is {var}")
    print(f"variance of list_A is {var}")

    logger.info(f"standard deviation of list_A is {stdev}")
    print(f"standard deviation of list_A is {stdev}")

def list_correlation_prediction():
    logger.info(f" list_x is {list_X}")
    logger.info(f" list_y is {list_y}")

    correlation_xy =statistics.correlation(list_X,list_y)
    logger.info(f" correlation between list_x and list_y is {correlation_xy}")

    slope,intercept = statistics.linear_regression(list_X,list_y)
    logger.info(f"The equation of best fit line is y= {slope}x + {intercept}")

    x_max= max(list_X)
    newx= x_max *15

    newy= slope * newx + intercept
    logger.info("We predict that when x = {newx}, y will be about {newy}")

def list_builtinfunction():
    max_value = max(list_A)
    min_value = min(list_A)

    logger.info(f"lis_A is {list_A}")
    logger.info(f"the max value is {max_value}")
    logger.info(f" the min value is {min_value}")

    len_list = len(list_A)
    logger.info(f" the len() of list_A is {len_list}")

    sum_list = sum(list_A)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {list_A}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(list_A)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(list_A, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )


def list_methods():
    
    list_B = list_A.append(34)
    logger.info(f" list_A is append() with list_B is {list_B}")

    list_C= [45,32,77,56,66]
    list_D = list_A.extend(list_C)
    logger.info(f"the extend() is list_A is {list_D}")

    list_E = list_A.insert(0,55)
    logger.info(f" the insert() in list_A is {list_E}")

    item_to_remove = 66
    list_F = list_C.remove(66)
    logger.info(f"the remove item from list_C is {list_F}")

    ct_list_A = list_A.count(111)
    logger.info(f"How many times 111 appear in list is {ct_list_A}")

    asc_list_A = list_A.sort()
    logger.info(f"Asc sort of list_A is {asc_list_A}")

    desc_list_A = list_A.sort(reverse=True)
    logger.info(f" Desc sort of list_A is {desc_list_A}")

    copy_list_A  = list_A.copy()
    logger.info(f"copy of list_A is {copy_list_A}")

    first = list_A.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_list is: {list_A}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = list_A.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_list is: {list_A}"
    )


def list_transformation():
    logger.info(f"The list: {list_A}")

    listA_over_100 = [filter(lambda x: x > 100, list_A)]
    logger.info(f"Scores over 100: {listA_over_100}")

    listA_doubled = [map(lambda x: x * 2, list_A)]
    logger.info(f"Doubled list_A: {listA_doubled}")

    list_A_sqrt = map(lambda x: math.sqrt(x), list_A)
    logger.info(f"Square root of scores: {list_A_sqrt}")

    radius_list = [7,8,9,10,11]
    logger.info(f"Radius list: {radius_list}")
    # Say "map r to pi r squared" given radius_list
    # cast the result to a list using square brackets
    area_list = [map(lambda r: math.pi * r * r, radius_list)]
    logger.info(f"Area of circles: {area_list}")

def list_comprehensions():
    logger.info(f"The list: {list_A}")

    listA_over_100 = [x for x in list_A if x > 100]
    logger.info(f"list_A over 100 (using list comprehensions!): {listA_over_100}")

    listA_under_42 = [x for x in list_A if x < 42]
    logger.info(f"In the list_A under 42 (using list comprehensions!): {listA_under_42}")

    list_A_doubled = [x * 2 for x in list_A]
    logger.info(f"Doubled list_A is (using list comprehensions!): {list_A_doubled}")

    list_A_sqrt = [math.sqrt(x) for x in list_A]

    radius_list = [7,6,9,8,9]
    logger.info(f"Given radius_list: {radius_list}")

    area_list = [math.pi * r * r for r in radius_list]
    logger.info(f"Area of circles: {area_list}")

    circumference_list = [2 * math.pi * r for r in radius_list]
    logger.info(f"Circumference of circles: {circumference_list}")

    logger.info("Mastering comprehesions is a valuable skill for data scientists.")
    numbers = [9,8,7,6,5]
    squares = [x**3 for x in numbers]
    logger.info(f"Given numbers: {numbers}")
    logger.info(f"Squares of numbers using [x ** 3 for x in numbers] is {squares}")

    

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    print("calling list_statistics()" )
    list_statistics()
    print("calling  list_correlation_prediction()")
    list_correlation_prediction()
    print("calling  list_builtinfunction()")
    list_builtinfunction()
    print("calling list_methods()")
    list_methods()
    print("calling  list_transformation()")
    list_transformation()
    print("calling list_comprehensions()")
    list_comprehensions()
    
    show_log()
    



