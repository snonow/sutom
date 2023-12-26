import os
import package.compare_words as compare_words
import package.letter_choosing as letter_choosing


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
        rate = letter_choosing.word_rate_calc(word[:-1])
        if rate > best_rate:
            best_word = word
            best_rate = rate   
            
    return best_word[:-1]


def solver_init(lst_letters, lst_not_in_letters=[], missplaced_letters=[]):
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
            if compare_words.main(lst_letters, word[:-1], lst_not_in_letters, missplaced_letters):
                new_dic.write(word)


def main_solver(lst_letters, lst_not_in_letters=[], missplaced_letters=[]):
    """
    Algorithm that can solve custom and that will be called within custom_solver.py file.

    Args:
        lst_letters (list): List of the right letters with the correct length.
    
    Returns:
        str: Best word from the good possible words.
    """
    if (not os.path.exists(".temp_dic/temp_dict.txt")) or (lst_not_in_letters == [] and missplaced_letters == []):
        if os.path.exists(".temp_dic/temp_dict.txt"):
            os.remove(".temp_dic/temp_dict.txt")
        solver_init(lst_letters, lst_not_in_letters, missplaced_letters)
        return (choose_word(), False)

    else:
        with open(".temp_dic/temp_dict.txt", "r") as temp_dic:
            lst_temp_dic = temp_dic.readlines()

        os.remove(".temp_dic/temp_dict.txt")
        
        # Initialize the new dictionary
        with open(".temp_dic/temp_dict.txt", "w") as new_temp_dic:
            for word in lst_temp_dic:
                if compare_words.main(lst_letters, word[:-1], lst_not_in_letters, missplaced_letters):
                    new_temp_dic.write(word)
        
        if len(lst_temp_dic) == 1:
            return (choose_word(), True)
        
        return (choose_word(), False)
