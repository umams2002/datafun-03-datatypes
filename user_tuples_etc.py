# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def tuples_methods():
    tupleA = (55,66,77,88,99)
    tupleB = (55,44,33,22,11)

    logger.info(f"tupleA = {tupleA}")
    logger.info(f"tupleB = {tupleB}")

    # tuple concatenation
    tupleCat = tupleA + tupleB

    # tuple repetition
    tupleAThrice = tupleA * 3

    # TODO: Start using this f-string "syntactic sugar" for quick ouptut
    # just add space = space inside the curly braces
    # it will print the name of the variable and the value
    logger.info(f"{tupleA = }")
    logger.info(f"{tupleB = }")
    logger.info(f"{tupleCat = }")
    logger.info(f"{tupleAThrice = }")

    tupleD = (111,222,333)
    hasOne = 1 in tupleD  # True
    hasFour = 4 in tupleD  # False

    # tuple indexing (0 is first, -1 is last, or 1 less than the length)

    my_tuple = (111,222,333)
    first = my_tuple[0]
    second = my_tuple[1]
    third = my_tuple[2]
    last = my_tuple[-1]

    # Use tuples to return multiple values from a function

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_and_remainder(10, 3)
logger.info(f"Quotient: {q}, Remainder: {r}")

def sets_method():
    setA = {11, 22, 33, 44, 55}
    setB = {44, 55, 66, 77, 88}

    logger.info(f"setA = {setA}")
    logger.info(f"setB = {setB}")

    # set union
    setC = setA | setB

    # set intersection
    setD = setA & setB

    # set difference
    setE = setA - setB

    # Define a list of adjectives
    list_adjectives = ["happy", "sad", "angry", "scared", "confused", "bored","happy","sad"]
    setWords = set(list_adjectives)
    listWordsNoDuplicates = list(setWords)
    listWordsNoDuplicates = [setWords]  # same as above

def dictionaries_method():
    plantA = {"name": "Rose", "Year": 2, "Height_cm": 13.4}
    plantB = {"name": "Hibiscus", "age": 4, "Height_cm": 17.2}

    logger.info(f"plant A is {plantA}")
    logger.info(f"plant B is {plantB}")

    assessment_dict = {"low": 0, "medium": 1, "high": 2}
    logger.info(f"assessment_dict = {assessment_dict}")

    data_dict = {
        "name": ["Rose", "Hibiscus"],
        "years": [2,4],
        "height_cm": [13.4, 17.2],
    }
    logger.info(f"data_dict = {data_dict}")

    with open("text_juliuscaesar.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info("Word count is a good way to begin processing text.")
    logger.info(f"Given text_juliuscaesar.txt, the word_counts_dict = {word_counts_dict}")

    word_counts_dict2 = {word: word_list.count(word) for word in word_list}
    logger.info("Given text_simple.txt and comprehensions,")
    logger.info(f"the the text_juliuscaesar = {word_counts_dict2}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    logger.info("Calling functions from main block")
    tuples_methods()
    dictionaries_method()
    show_log()