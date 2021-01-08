#welcome to hangman game 

import sys 
import random

def  randomworda(numwordpro): # For reading file
    key ="key.txt"
    currwo = None
    numwordpro=int(numwordpro)
    f = open(key,"r")
    for word in f:
        word = word.strip().lower()
        names =list(word.split(','))
    currwo = random.choice(names)
    return(currwo)

    
def start():  #Intro
    print("")
    print("________ ")
    print( "| ")
    print( "|  | ")
    print( "|  0 ")
    print( "| /|\ ")
    print( "| / \ ")
    print( "| ")
    print( " ")
    print( " WELCOME TO HANG MAN ")
    print("Press '1' for Rules and Regulation")
    print("Press '2' for start")
    print("Press '3' for exit()")
    selection =int(input())
    if (selection == 1):
            print("      _____________________________________________RULES___________________________________-")
            print("     1.Play individually or in groups. ")
            print("     2.If the letter is contained in the word/phrase, the group or individual takes another turn guessing a letter.To reveal a letter ")
            print("     3.If the letter is not contained in the word/phrase, click the Try Again button, a portion of the hangman is added. ")
            print(f"    4.The game continues until\n             the word/phrase is guessed (all letters are revealed) – WINNER or \n              all the parts of the hangman are displayed – LOSER")

    if (selection == 2):
        keyword = randomworda(0)
        hangman(keyword)
    if (selection == 3):
        sys.exit(0)


def hangman(word): #game 
    wrong = 0
    stages = ["",
             "________ ",
             "| ",
             "|  | ",
             "|  0 ",
             "| /|\ ",
             "| / \ ",
             "| "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print(" Ready...... set............. go .....")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter   "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


start()





