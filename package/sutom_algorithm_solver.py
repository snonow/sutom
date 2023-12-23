def solver(lst_letters, lst_words):
    """
    Algorithm that can solve sutom and that will be called within sutom_solver.py file.

    Args:
        lst_letters (list): List of the right letters with the good length.
        lst_words (list): List of good words that are part of the word 
                        but that arent in the first list.
    
    Returns:
        _type_: _description_
    """
    dict = open("dict_french.txt", "r")
    
    