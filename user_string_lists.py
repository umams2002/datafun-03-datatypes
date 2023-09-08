import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

list_subject = ["english","math", "science","social studies","physical education"]

list_outcomes = ["pass","fail"]


def processed_text_text_names_in():
     with open("text_names_in.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")


def create_random_sentence():
    logger.info("Calling create_random_sentence()")
    sentence = (
        f"The {random.choice(list_subject)} {random.choice(list_outcomes)} "
     )

    logger.info(f"Random sentence: {sentence}")

def get_winner_message(userguess, botguess):
    if userguess == botguess:
        return "We tied!"
    elif userguess == "math":
        if botguess == "english":
            return "I win!"
        else:
            return "You win!"
    elif userguess == "english":
        if botguess == "math":
            return "You win!"
        else:
            return "I win!"

def play_game():
    logger.info("Calling play_game()")
    ready_for_continous_game = True  # TODO: change this when ready
    logger.info(f"ready_for_continous_game = {ready_for_continous_game}")

    if not ready_for_continous_game:
        logger.info("Not yet ready for continous game of rock, paper, scissors.")
        logger.info("Find the TODO and change False to True to play a game.")
        logger.info("Exiting the function early without kicking off the game.")
        return
    
    while True:
        print()
        user_choice = input("Say your favourite subject in school or q to quit:")
        if user_choice == "q":
            break
        bot_choice = random.choice(list_subject)
        print(f"You said {user_choice}.")
        print(f"I said {bot_choice}.")
        msg1 = get_winner_message(userguess=user_choice, botguess=bot_choice)
        msg2 = get_winner_message(botguess=bot_choice, userguess=user_choice)
        if msg1 == msg2:
            print(msg1)
        print()
        print("This program will run forever unless you type q to quit.")
        print("or use Ctrl-C to stop the program.")
        print()

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    logger.info("Calling functions from main block")
    processed_text_text_names_in()
    create_random_sentence()
    play_game()
    show_log()