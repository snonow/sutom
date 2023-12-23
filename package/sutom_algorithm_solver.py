def check_word_length(lst_letters, word):
    """
    Check if the word is the right length.

    Args:
        lst_letters (list): _description_
        word (str): _description_

    Returns:
        _type_: _description_
    """
    if len(lst_letters) == len(word):
        return True
    return False



def compare_words(lst_letters, lst_known_letters, word):
    """
    Check if the word is in the list of words.

    Args:
        lst_letters (list): _description_
        lst_words (list): the list of words
        word (str): the word to check.

    Returns:
        Bool: Used in the main_solver and init function.
    """
    # Check that the good letters are in the right position
    for i in range(len(lst_letters)):
        if lst_letters[i] != word[i] and lst_letters[i] != 0:
            return False
    
    # Check that the good letters are in the word
    for letter in lst_known_letters:
        if letter not in word:
            return False
    
    # If all the good letters are in the word
    return True

def choose_word():
    pass


def solver_init(lst_letters):
    """
    Initialize the algorithm.

    Args:
        lst_letters (list): List of the right letters with the good length.
        lst_words (list): List of good words that are part of the word 
                        but that arent in the first list.
    
    Returns:
        _type_: _description_
    """
    # Initialize the dictionary
    dic = open("dict_french.txt", "r")
    temp_dic = open("temp_dict.txt", "w")
    
    for word in dic.readlines():
        if check_word_length(lst_letters, word[:-1]):
            if compare_words(lst_letters, [], word[:-1]):
                temp_dic.write(word)
                
                
def main_solver(lst_letters, lst_known_letters):
    """
    Algorithm that can solve sutom and that will be called within sutom_solver.py file.

    Args:
        lst_letters (list): List of the right letters with the good length.
        lst_words (list): List of good words that are part of the word 
                        but that arent in the first list.
    
    Returns:
        _type_: _description_
    """
    # Initialize the dictionary
    temp_dic = open("temp_dict.txt", "w")
    
    for word in temp_dic.readlines():
        if check_word_length(lst_letters, word[:-1]):
            if compare_words(lst_letters, lst_known_letters, word[:-1]):
                temp_dic.write(word)
                
    
        
        
    
    
    