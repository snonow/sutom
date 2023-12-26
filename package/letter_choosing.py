

frequence_lettres_fr = {
    'A': 9,
    'B': 2,
    'C': 3,
    'D': 3,
    'E': 15,
    'F': 1,
    'G': 1,
    'H': 1,
    'I': 8,
    'J': 1,
    'K': 1,
    'L': 5,
    'M': 3,
    'N': 6,
    'O': 6,
    'P': 3,
    'Q': 1,
    'R': 6,
    'S': 6,
    'T': 6,
    'U': 6,
    'V': 2,
    'W': 1,
    'X': 1,
    'Y': 1,
    'Z': 1
}


def word_rate_calc_v2(word):
    """
    Calculate the word rate.

    Args:
        word (str): The word to calculate the word rate.
    
    Returns:
        int: The word rate.
    """
    dic_rate, rate = {}, 0
    for letter in list(word):
        if not letter in dic_rate:
            dic_rate[letter] = frequence_lettres_fr[letter]
    for letter in dic_rate.keys():
        rate += dic_rate[letter]
    return rate

def word_rate_calc(word):
    """
    Blablabla

    Args:
        word (_type_): _description_

    Returns:
        _type_: _description_
    """
    return nb_of_unique_consonants(word) + nb_of_unique_vowels(word)

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