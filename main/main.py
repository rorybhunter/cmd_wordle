import random

class bcolors:
    G = '\033[92m'
    R = '\033[91m'
    Y = '\033[93m'
    B = '\033[30m'


def get_word() -> str:
    with open("../static/words.txt") as word_file:
        words = word_file.read()
        words = words.split('\n')
    index = random.randrange(0, len(words))
    return words[index]


def print_guesses(guesses: list) -> None:
    return


def get_difficulty() -> str:
    return input("Choose difficulty:\n1: Easy (10 guesses)\n2. Meduim(5 guesses)\n3: Hard (3 guesses)\n")


def diff_to_guesses(diff: str) -> int:
    if diff == "1":
        return 10
    elif diff == "2":
        return  5
    else:
        return 3
    
def guess(guesses: list, word: str) -> bool:
    if word in guesses:
        return True
    guesses = [guess for guess in guesses if guess is not None]
    guess = guesses[-1]
    correct_letters = []
    guessed_letters = []
    for letter in guess:
        if letter in word:
            correct_letters.append(letter)
    
    for gl, wl in zip(guess, word):
        guessed_letters.append(gl)
        if gl == wl:
            print(f"{bcolors.G}{gl}" , end="")
        elif gl in correct_letters and word.count(gl) >= guessed_letters.count(gl):
            print(f"{bcolors.Y}{gl}", end="")
        else:
            print(f"{bcolors.R}{gl}", end="")
        print(f"{bcolors.B}", end="")
                    

def main() -> None:
    word = get_word()
    print(word)
    
    # get difficulty
    diffs = ["1", "2", "3"]
    diff = None
    while diff not in diffs:
        diff = get_difficulty() 
    del diffs
    print()

    num_guesses = diff_to_guesses(diff)
    guesses = [None] * num_guesses
    won = False
    for i in range(num_guesses):    
        g = input(f"\nEnter your guess:")
        guesses[i] = g
        won = guess(guesses, word)
        if won:
            print("\n\nCongratulations!!!!!\n")
            break;
    if not won:
        print(f"The word was {word}")







if __name__ == "__main__":
    main()