# Sutom Game Script

# Importing necessary functions from custom modules
from package.sutom_algorithm_solver import main_solver
from package.sutom import main_sutom

def check_syntax_init(syntax):
    """_summary_

    Args:
        syntax (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if not syntax[0].isalpha():
        raise ValueError("Syntax must start with a letter.")
    for letter in syntax[1:]:
        if letter == "_":
            continue
        else:
            raise ValueError("Syntax must contain only underscores after the first letter.")
    
    return True
    

def check_syntax_in_loop(syntax):
    """
    Function to check the syntax of the user input for the solver.
    Args:
        syntax (str): User input containing known and forbidden letters.
    Raises:
        ValueError: If the syntax is incorrect.
    """
    try:
        # Split the syntax into two parts using space as a separator
        parts = syntax.split(" ")

        # Check if there are exactly two parts
        if len(parts) != 3:
            raise ValueError("Syntax must have exactly two parts separated by a space.")

        known_letters, forbidden_letters, missplaced_letters  = parts

        # Check if known letters contain only letters and underscores
        if not all(c.isalpha() or c == "_" for c in known_letters):
            raise ValueError("Known letters should contain only letters and underscores.")

        # Check if forbidden letters contain only letters
        if not all(c.isalpha() or c == "_" for c in forbidden_letters):
            raise ValueError("Forbidden letters should contain only letters and underscores.")
        
        # Check if forbidden letters contain only letters
        if not all(c.isalpha() or c == "_" for c in missplaced_letters):
            raise ValueError("Missplaced letters should contain only letters and underscores.")
        
        return True

    except ValueError as e:
        print(f"Syntax error: {e}")

def help_loop():
    """
    Function to provide help options to the user in a loop until 'help' is entered.
    Returns:
        str: User input after help is entered.
    """
    user_input = "help"
    while user_input == "help":
        print("To play Sutom manually, type M.",
              "To use the solver, type S.",
              "To see the solver complete a part by itself, type A.", sep="\n")
        user_input = str(input("What do you want to do? (help)\n"))
    return user_input



def main_game_mode(user_input=None):
    """
    Function to determine the game mode based on user input.
    """
    if user_input is None:
        user_input = str(input("What do you want to do? (help)\n"))

    if user_input == "help":
        help_loop()
        main_game_mode()

    elif user_input == "M":
        print("Good luck with your Sutom game!\n")
        main_sutom()

    elif user_input == "S":
        print("Launching the solver.\n")
        while True:
            solver_input = str(input("What does the word you're looking for look like?\n"
                                      "(Enter \"help\" to see the required syntax)\n"))
            if solver_input == "help":
                print("Syntax:\n",
                      "Enter the known letters and the unknown letters as \"_\"\n",
                      "Enter forbidden letters all together.\n",
                      "Enter misplaced letters all together.\n"
                      "Separate these two parts by a space \" \".\n")
            else:
                try:
                    check_syntax_init(solver_input)
                    known_letters = solver_input
                    choosen_word, cond = main_solver(known_letters)
                    while not cond:
                        print(f"The word you're looking for looks like:\n{choosen_word}")
                        solver_input = str(input("What does the word you're looking for look like?\n"))
                        check_syntax_in_loop(solver_input)
                        parts = solver_input.split(" ")
                        known_letters, forbidden_letters, missplaced_letters = parts
                        if forbidden_letters == "_":
                            forbidden_letters = []
                        if missplaced_letters == "_":
                            missplaced_letters = []
                        choosen_word, cond = main_solver(known_letters, forbidden_letters, missplaced_letters)
                    print("The following word is the correct answer.\n", f"It was {choosen_word}.\n")
                    break
                except ValueError as e:
                    print(f"Syntax error: {e}")

    elif user_input == "A":
        main_solver()

    else:
        raise ValueError("Syntax error")
