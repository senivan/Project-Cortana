"""Lab №6_4"""
import random

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    cons_list= ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    final_lisg = []
    for _ in range(3):
        small_list = []
        random_let = random.randint(1,2)
        count = 0
        for __ in range(3):
            if random_let == 1 and count == 0:
                rand = random.choice(vowel_list)
                random_let = 2
                count +=1
                small_list.append(rand)
                continue
            rand = random.choice(cons_list)
            random_let = 1
            small_list.append(rand)
            continue
        final_lisg.append(small_list)
    return final_lisg

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt', [el for el in 'wumrovkif'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', \
'irok', 'komi', 'kori', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    """
    final_lst = []
    line_check = 'a'
    with open(f,'r+',encoding='utf-8') as file:
        for line in file:
            count = 0
            c = 0
            line_sliced = line.strip().lower()
            if line_sliced == line_check:
                continue
            if len(line_sliced)>=4 and line_sliced.count(letters[4])>0:
                for j in line_sliced:
                    if j in letters:
                        count +=1
                    if line_sliced.count(j) <= letters.count(j):
                        c +=1
                if count == len(line_sliced) == c:
                    final_lst.append(line_sliced)
            line_check = line_sliced
        return final_lst



def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_words_list = []
    while True:
        try:
            word_inp = str(input())
            user_words_list.append(word_inp)
        except EOFError:
            return user_words_list

def get_words_without_user(f: str, letters: list[str]) -> list[str]:
    """
    This function returns words that are in the dictionary, but the player missed them.
    """
    all_words_list = get_words(f,letters)
    user_words_list = get_user_words()
    for i in user_words_list:
        if i in all_words_list:
            all_words_list.remove(i)
    return all_words_list

def get_pure_user_words(user_words: list[str], letters: list[str],
                        words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['form','forum','four','forumi'],\
[el for el in 'wumrovkif'],['fork', 'form', 'forum', 'four', 'fowk', \
'from', 'frow', 'irok', 'komi', 'kori', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf'])
    ['forumi']
    """
    final_lst = []
    for line in user_words:
        count = 0
        c = 0
        line_sliced = line.strip().lower()
        if len(line_sliced)>=4 and line_sliced.count(letters[4])>0:
            for j in line_sliced:
                if j in letters:
                    count +=1
                if line_sliced.count(j) <= letters.count(j):
                    c +=1
            if line not in words_from_dict:
                if count == len(line_sliced) == c:
                    final_lst.append(line_sliced)
    return final_lst


def main():
    """
    This is the main function
    """
    print('Your board is', generate_grid())
    print('Please suggest your words here:')
    get_user_words()
    print('All possible words:')
    print(get_words('en.txt', list('wumrovkif')))
    print('You missed folowing words:')
    print(get_words_without_user('en.txt', list('wumrovkif')))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    main()
