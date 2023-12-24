def main(lst_letters, word, lst_forbidden_letters=[], lst_misplaced_letters=[]):
    """
    Check if the word is in the list of words.

    Args:
        lst_letters (list): List of the right letters with the correct length.
        word (str): The word to check.
        lst_forbidden_letters (list): List of forbidden letters, initially empty.
        lst_misplaced_letters (list): List of misplaced letters, initially empty.

    Returns:
        bool: True if the word matches the criteria, False otherwise.
    """
    if correct_length(lst_letters, word):
        if correct_letters(lst_letters, word):
            if forbidden_letters(lst_letters, word, lst_forbidden_letters):
                if missplaced_letters(lst_letters, word, lst_misplaced_letters):
                    return True
    else:
        return False

def correct_length(lst_letters, word):
    return len(word) == len(lst_letters)

def correct_letters(lst_letters, word):
    lst_word = list(word)
    for i in range(len(lst_word)):
        if lst_word[i]!= lst_letters[i] and lst_letters[i] != "_":
            return False
        
    return True
        
def missplaced_letters(lst_letters, word, missplaced_letters=[]):
    lst_word = list(word)
    word_unknown_letters = []
    for i in range(len(lst_word)):
        if lst_letters[i] == "_":
            word_unknown_letters.append(lst_word[i])
    
    for missplaced_letter in missplaced_letters:
        if missplaced_letter not in word_unknown_letters:
            return False
    
    return True

def forbidden_letters(lst_letters, word, lst_forbidden_letters=[]):
    lst_word = list(word)
    word_unknown_letters = []
    for i in range(len(lst_word)):
        if lst_letters[i] == "_":
            word_unknown_letters.append(lst_word[i])
    
    for unknown_letter in word_unknown_letters:
        if unknown_letter in lst_forbidden_letters:
            return False
    
    return True