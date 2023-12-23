# Sutom Game Script

# Importing necessary functions from custom modules
from package.sutom_algorithm_solver import main_solver
from package.sutom import main_sutom

def check_syntax(syntax):
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
        if len(parts) != 2:
            raise ValueError("Syntax must have exactly two parts separated by a space.")

        known_letters, forbidden_letters = parts

        # Check if known letters contain only letters and underscores
        if not all(c.isalpha() or c == "_" for c in known_letters):
            raise ValueError("Known letters should contain only letters and underscores.")

        # Check if forbidden letters contain only letters
        if not all(c.isalpha() for c in forbidden_letters):
            raise ValueError("Forbidden letters should contain only letters.")

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
        new_user_input = help_loop()
        main_game_mode(new_user_input)

    elif user_input == "M":
        print("Good luck with your Sutom game!\n")
        main_sutom()

    elif user_input == "S":
        print("Launching the solver.\n")
        solver_input = str(input("What does the word you're looking for look like?\n"
                                  "(Enter \"help\" to see the required syntax)"))
        if solver_input == "help":
            print("Syntax:\n",
                  "Enter the known letters and the unknown letters as \"_\"\n",
                  "Enter forbidden letters all together.\n",
                  "Separate these two parts by a space \" \".\n")

        else:
            check_syntax(solver_input)
            known_letters, forbidden_letters = solver_input.split(" ")
            main_solver(known_letters, forbidden_letters)

    elif user_input == "A":
        main_solver()

    else:
        raise ValueError("Syntax error")