import random
import itertools

# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result


def main_program():
    for i in itertools.repeat(1):
        if play_once(True) == -1:
            print("I win!")
        if play_once(True) == 0:
            print("Game drawn")
        if play_once(True) == 1:
            print("You win!")
        again = input("Do you want to play again?")
        if again == "Yes":
            continue
        if again == "No":
            print("Goodbye")
            break



main_program()
