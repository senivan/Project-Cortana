import random
from benchmark_funcs import time_to_run, memory_used

def generate_grid() -> list[list[str]]:
    """Generates a 3x3 grid with alternating vowels and consonants.

    Returns:
        A list of lists representing the game board, where each inner list
        represents a row of letters.
    """

    vowel_list = ['A', 'E', 'I', 'O', 'U']
    consonant_list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    grid = [[random.choice(vowel_list if i % 2 == 0 else consonant_list) for _ in range(3)] for i in range(3)]
    return grid


def get_words(filename: str, letters: list[str]) -> list[str]:
    """Reads words from a file and returns those formed using the given letters.

    Args:
        filename (str): The path to the dictionary file.
        letters (list[str]): The list of letters available on the game board.

    Returns:
        list[str]: A list of valid words found in the dictionary that can be formed
                   using the given letters.
    """

    valid_words = []
    letter_counts = {letter: letters.count(letter) for letter in set(letters)}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            if len(word) >= 4:
                for char in word:
                    if word.count(char) > letter_counts.get(char, 0):
                        break  # Skip to next word if char count exceeds available letters
                else:
                    valid_words.append(word)

    return valid_words


def get_user_words() -> list[str]:
    """Gets words from user input and returns a list with these words.

    Returns:
        list[str]: A list of words entered by the user.
    """

    user_words_list = []
    while True:
        try:
            word_inp = str(input())
            user_words_list.append(word_inp)
        except EOFError:
            return user_words_list


def get_missed_words(dictionary_words: list[str], user_words: list[str]) -> list[str]:
    """Returns all words from the dictionary that the user missed.

    Args:
        dictionary_words (list[str]): The list of words from the dictionary.
        user_words (list[str]): The list of words entered by the user.

    Returns:
        list[str]: A list of words from the dictionary that are not found in
                   the user's input.
    """

    missed_words = [word for word in dictionary_words if word not in user_words]
    return missed_words


def main():
    """The main function that runs the game."""

    print("Your board is:", generate_grid())
    print("Please suggest your words here:")
    user_words = get_user_words()

    print("All possible words:")
    print(get_words("en.txt", list("wumrovkif")))  # Replace "en.txt" with your actual dictionary file path

    print("You missed the following words:")
    dictionary_words = get_words("en.txt", list("wumrovkif"))  # Replace "en.txt" with your actual dictionary file path
    missed_words = get_missed_words(dictionary_words, user_words)
    print(missed_words)

if __name__ == "__main__":
    main()
