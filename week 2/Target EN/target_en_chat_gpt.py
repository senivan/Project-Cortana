import random


def generate_grid() -> list[list[str]]:
    """Generates a 3x3 grid of random letters with at least one vowel in each row."""
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    consonant_list = 'BCDFGHJKLMNPQRSTVWXYZ'
    grid = []
    for _ in range(3):
        row = random.choices(vowel_list, k=1) + random.choices(consonant_list, k=2)
        random.shuffle(row)
        grid.append(row)
    return grid


def get_words(filepath: str, letters: list[str]) -> list[str]:
    """
    Retrieve words from file that are composed 
    of the given letters and have at least 4 letters.
    """
    valid_words = []
    letters_set = set(letters)
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            if len(word) >= 4 and all(char in letters_set for char in word):
                if all(word.count(char) <= letters.count(char) for char in word):
                    valid_words.append(word)
    return valid_words


def get_user_words() -> list[str]:
    """Collects words from user input until an EOFError is raised."""
    user_words_list = []
    print("Enter words (press CTRL+D or CTRL+Z then Enter to stop):")
    while True:
        try:
            user_words_list.append(input().strip())
        except EOFError:
            break
    return user_words_list


def get_words_without_user(user_words: list[str], all_words_list: list[str]) -> list[str]:
    """Filters out words from all_words_list that were found by the user."""
    return [word for word in all_words_list if word not in user_words]


def get_pure_user_words(user_words: list[str], letters: list[str],
                        words_from_dict: list[str]) -> list[str]:
    """Returns user words not found in the dictionary and that obey the letter restrictions."""
    letters_set = set(letters)
    return [
        word for word in user_words
        if len(word) >= 4
        and all(word.count(char) <= letters.count(char) for char in word)
        and all(char in letters_set for char in word)
        and word not in words_from_dict
    ]


def main():
    """Main function to run the word game logic."""
    grid = generate_grid()
    print(f'Your board is: {grid}')
    letters = [char for row in grid for char in row]
    print('Please suggest your words here:')
    user_words = get_user_words()
    all_words = get_words('en.txt', letters)
    print('All possible words:', all_words)
    missed_words = get_words_without_user(user_words, all_words)
    print('You missed following words:', missed_words)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
