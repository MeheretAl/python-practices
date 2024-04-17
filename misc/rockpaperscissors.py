'''importing random to determine computer's choice randomly and
time module to make it lag a bit to make it realistic'''
import random
import time

'''possible choices of the game'''
possiblechoices = {'r': 'rock',
                   'p' : 'paper',
                   's':'scissors',}


'''writing the logic of the game'''
def play_game():

    '''showing user what the possible choices are and letting user choose'''
    print("\nThe possible choices are:")
    for keys,values in possiblechoices.items():
        print(f"\t\t\t {keys} for {values}.")
    user_choice = str(input("What is your choice?\n"))


    '''linking the user's choice with it's key in possible choices
    and determing the computer choice randomly'''
    user_choice = possiblechoices.get(user_choice)
    computer_choice = random.choice(list(possiblechoices.values()))

    '''checking whether user_choice is a valid choice'''
    if (user_choice in possiblechoices.values()):
        if user_choice == computer_choice:
            print(f"Draw! We both chose {computer_choice}.\n")
            time.sleep(0.5)
            play_again()
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissors' and computer_choice=='paper'):
            print("You won.")
            print(f"My choice was {computer_choice}.\n")
            time.sleep(0.5)
            play_again()
        else:
            print(f"I've won\nI chose {computer_choice}.\n")
            time.sleep(0.5)
            play_again()
    else:
        print("Choose a valid option.")
        play_game()

'''letting the user play again'''
def play_again():
    user_input = input(str("Do you want to play again?\nY for yes and N for no.\n"))
    if user_input.lower() == 'y':
        play_game()
    elif user_input.lower() == 'n':
        quit
    else:
        print("Please choose a valid option")
        play_again()

'''calling the function'''
play_game()