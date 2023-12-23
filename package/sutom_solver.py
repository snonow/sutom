class Solver():
    def __init__(self, first_initial, number_of_letters):
        self.rightWord = [0]*number_of_letters
        self.rightWord.append(first_initial)
        self.goodLetters = []
    
    
    