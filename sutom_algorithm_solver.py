import os


def compare_words(lst_letters, word, lst_known_letters=None):
    """
    Check if the word is in the list of words.

    Args:
        lst_letters (list): List of the right letters with the correct length.
        lst_known_letters (list): List of known letters.
        word (str): The word to check.

    Returns:
        bool: True if the word matches the criteria, False otherwise.
    """
    #
    if len(lst_letters) != len(word):
        return False
    # 
    else :
        for i in range(len(lst_letters)):
            if lst_letters[i]!= word[i] and lst_letters[i] not in [0,'0',"0"]:
                return False
        if lst_known_letters != None:
            for letter in lst_known_letters:
                if letter not in word:
                    return False
        return True
    
    

def nb_of_unique_vowels(word):
    """
    Count the number of unique vowels in the word.

    Args:
        word (str): The word to count the number of unique vowels.

    Returns:
        int: The number of unique vowels in the word.
    """
    vowels = set("aeiou")
    unique_vowels = set(char.lower() for char in word if char.lower() in vowels)
    return len(unique_vowels)


def nb_of_unique_consonants(word):
    """
    Count the number of unique consonants in the word.

    Args:
        word (str): The word to count the number of unique consonants.

    Returns:
        int: The number of unique consonants in the word.
    """
    consonants = set("bcdfghjklmnpqrstvwxyz")
    unique_consonants = set(char.lower() for char in word if char.lower() in consonants)
    return len(unique_consonants)



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
        rate = nb_of_unique_consonants(word) + nb_of_unique_vowels(word)*10
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
            if compare_words(lst_letters, word[:-1]):
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
                if compare_words(lst_letters, word[:-1], lst_known_letters):
                    new_temp_dic.write(word)
        
        return choose_word()

# TEST
os.remove(".temp_dic/temp_dict.txt")
main_solver(list("00000"), [])