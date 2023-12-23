import os

def check_word_length(lst_letters, word):
    """
    Check if the word is the right length.

    Args:
        lst_letters (list): List of the right letters with the correct length.
        word (str): The word to check.

    Returns:
        bool: True if the word has the correct length, False otherwise.
    """
    return len(lst_letters) == len(word)


def compare_words(lst_letters, lst_known_letters, word):
    """
    Check if the word is in the list of words.

    Args:
        lst_letters (list): List of the right letters with the correct length.
        lst_known_letters (list): List of known letters.
        word (str): The word to check.

    Returns:
        bool: True if the word matches the criteria, False otherwise.
    """
    for i in range(len(lst_letters)):
        if lst_letters[i] != word[i] and lst_letters[i] != 0:
            return False
    
    for letter in lst_known_letters:
        if letter not in word:
            return False
    
    return True


def nb_of_vowels(word):
    """
    Count the number of vowels in the word.

    Args:
        word (str): The word to count the number of vowels.

    Returns:
        int: The number of vowels in the word.
    """
    vowels = set("aeiou")
    return sum(1 for char in word if char.lower() in vowels)


def nb_of_consonants(word):
    """
    Count the number of consonants in the word.

    Args:
        word (str): The word to count the number of consonants.

    Returns:
        int: The number of consonants in the word.
    """
    consonants = set("bcdfghjklmnpqrstvwxyz")
    return sum(1 for char in word if char.lower() in consonants)


def choose_word():
    """
    Choose the best word from the good possible words.

    Returns:
        str: The best word from the good possible words.
    """
    # Initialize the dictionary
    with open(".temp_dic/temp_dict.txt", "r") as dic:
        lst_words = dic.readlines()
    
    # Initialize the variables
    best_word = ""
    best_rate = 0
    
    for word in lst_words:
        rate = nb_of_consonants(word) + nb_of_vowels(word)*10
        if rate > best_rate:
            best_word = word
            best_rate = rate   
            
    return best_word[:-1]
         


def solver_init(lst_letters):
    """
    Initialize the algorithm.

    Args:
        lst_letters (list): List of the right letters with the correct length.
    
    Returns:
        None
    """
    # Initialize the dictionary
    full_dict = open("french_dict.txt", "r")
    dic = full_dict.readlines()
    full_dict.close()
    
    with open(".temp_dic/temp_dict.txt", "w") as new_dic:
        for word in dic:
            if check_word_length(lst_letters, word[:-1]):
                print('first phase ok')
                if compare_words(lst_letters, [], word[:-1]):
                    print('second phase ok')
                    new_dic.write(word)


def main_solver(lst_letters, lst_known_letters):
    """
    Algorithm that can solve custom and that will be called within custom_solver.py file.

    Args:
        lst_letters (list): List of the right letters with the correct length.
        lst_known_letters (list): List of good words that are part of the word 
                        but that aren't in the first list.
    
    Returns:
        str: Best word from the good possible words.
    """
    if not os.path.exists(".temp_dic/temp_dict.txt"):
        solver_init(lst_letters)
        return choose_word()
    
    else:
        # Initialize the dictionary
        with open(".temp_dic/temp_dict.txt", "r") as temp_dic:
            lst_temp_dic = temp_dic.readlines()

        os.remove(".temp_dic/temp_dict.txt")
        
        # Initialize the new dictionary
        with open(".temp_dic/temp_dict.txt", "w") as new_temp_dic:
            for word in lst_temp_dic:
                if compare_words(lst_letters, lst_known_letters, word[:-1]):
                    new_temp_dic.write(word)
        
        return choose_word()

# TEST

main_solver(list("ABRICOT"), [])