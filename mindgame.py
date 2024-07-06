import random

def generate_code(code_length, colors):
    """Generates a secret code of the specified length from the given set of colors."""
    code = []
    for _ in range(code_length):
        code.append(random.choice(colors))
    return code

def get_guess(code_length):
    """Gets a guess from the player as a list of colors."""
    guess = []
    while len(guess) != code_length:
        try:
            guess_str = input("Enter your guess (space-separated colors): ").strip().split()
            guess = [str(x) for x in guess_str]
            if len(guess) != code_length:
                print("Guess must be", code_length, "colors long.")
        except ValueError:
            print("Guess must be valid colors.")
    return guess

def check_guess(code, guess):
    """Checks the guess against the secret code and returns a tuple containing the number of exact matches (black pegs) 
    and the number of correct colors in the wrong positions (white pegs)."""
    black_pegs = 0
    white_pegs = 0
    code_copy = code.copy()
    guess_copy = guess.copy()

    # First pass: count black pegs and remove them from consideration
    for i in range(len(code)):
        if guess[i] == code[i]:
            black_pegs += 1
            code_copy[i] = None
            guess_copy[i] = None

    # Second pass: count white pegs
    for i in range(len(guess)):
        if guess_copy[i] is not None and guess_copy[i] in code_copy:
            white_pegs += 1
            code_copy[code_copy.index(guess_copy[i])] = None

    return black_pegs, white_pegs

def play_mastermind():
    """Plays a two-player game of Mastermind."""
    code_length = 4  # Can be modified to change the number of digits in the code
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]  # Can be modified to change the number of colors
    max_guesses = 10  # Can be modified to change the maximum number of guesses allowed

    print("Welcome to the two-player Mastermind game!")
    print("Available colors are:", ", ".join(colors))
    print("Player 1 sets the code, and Player 2 tries to guess it.")

    # Player 1 sets the code
    code = []
    while len(code) != code_length:
        try:
            code_str = input("Player 1, set the code (space-separated colors): ").strip().split()
            code = [str(x) for x in code_str]
            if len(code) != code_length:
                print("Code must be", code_length, "colors long.")
        except ValueError:
            print("Code must be valid colors.")
    
    # Player 2 guesses the code
    num_guesses_p2 = 0
    while num_guesses_p2 < max_guesses:
        guess = get_guess(code_length)
        black_pegs, white_pegs = check_guess(code, guess)
        print("Black pegs:", black_pegs)
        print("White pegs:", white_pegs)
        num_guesses_p2 += 1
        if black_pegs == code_length:
            print("Player 2 guessed the code in", num_guesses_p2, "guesses!")
            break
    else:
        print("Player 2 ran out of guesses. The code was:", code)

    # Player 1 guesses the code set by Player 2
    if black_pegs == code_length:
        print("Now Player 2 sets the code, and Player 1 tries to guess it.")
        code = []
        while len(code) != code_length:
            try:
                code_str = input("Player 2, set the code (space-separated colors): ").strip().split()
                code = [str(x) for x in code_str]
                if len(code) != code_length:
                    print("Code must be", code_length, "colors long.")
            except ValueError:
                print("Code must be valid colors.")

        num_guesses_p1 = 0
        while num_guesses_p1 < max_guesses:
            guess = get_guess(code_length)
            black_pegs, white_pegs = check_guess(code, guess)
            print("Black pegs:", black_pegs)
            print("White pegs:", white_pegs)
            num_guesses_p1 += 1
            if black_pegs == code_length:
                print("Player 1 guessed the code in", num_guesses_p1, "guesses!")
                break
        else:
            print("Player 1 ran out of guesses. The code was:", code)

        # Determine the winner
        if num_guesses_p1 < num_guesses_p2:
            print("Player 1 wins and is crowned Mastermind!")
        else:
            print("Player 2 wins and is crowned Mastermind!")

if __name__ == "__main__":
    play_mastermind()
