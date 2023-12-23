import random
import os

def choose_secret_word():
    full_dict = open("french_dict.txt", "r")
    dic = full_dict.readlines()
    full_dict.close()
    
    secret_word = random.choice(dic)
    secret_word = secret_word[:-1]
    
    return secret_word

def ask_guess(secret_word):
    guess = str(input("Entrez un mot:\n"))
    guess = guess.upper()
    
    full_dict = open("french_dict.txt", "r")
    dic = full_dict.readlines()
    full_dict.close()
    
    while not(guess + "\n" in dic and len(guess) == len(secret_word)):
        guess = input("Mot invalide, entrez un mot:\n")
        guess = guess.upper()
    
    return guess

def hint_maker(secret_word, guess=None):
    """
    _summary_
    """
    if guess == None:
        n = len(secret_word)
        return str(secret_word[0]) + "_"*(n-1)
    else:
        hint, lst_not_in_letters  = "", []
        for i in range(len(secret_word)):
            if secret_word[i] == guess[i]:
                hint += secret_word[i]
            else:
                hint += "_"
                if guess[i] not in secret_word:
                    lst_not_in_letters.append(guess[i])
        return str(hint), lst_not_in_letters
    
    
def main_sutom():
    secret_word, count = choose_secret_word(), 1
    hint = hint_maker(secret_word)
    print(hint)
    guess = ask_guess(secret_word)
    
    while guess!= secret_word:
        count += 1
        hint = hint_maker(secret_word, guess)
        print(hint[0],"\n",f"Les lettres qui ne sont pas dans le mot sont les suivantes {hint[1]}.\n")
        guess = ask_guess(secret_word)
        
    os.remove(".temp_dic/temp_dict.txt")
    print(f"Bravo, vous avez trouvé le mot en seulement {count} tentatives.\n")
    