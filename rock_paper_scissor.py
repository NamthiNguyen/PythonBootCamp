import random
import emoji
pick= [emoji.emojize(":victory_hand:"), emoji.emojize(":raised_fist:"),emoji.emojize(":raised_hand:")] # computer choses 

def main():
    
    while True: #loop until the user quiet
        
        try:
            start_game = input("please choose rock, paper or scissor using ( r / p / s ):  ").lower()
            user_pick(start_game, pick)
            restart = input("Do you want to play again: type 'y' to play again or 'n' to stop: " ).lower()
            play_again(restart)
            break # incase we keep looping 
        except ValueError:
            print("Your following input is not r , p or s.") # incase user choose a non string 
    



def user_pick(chosen,counter):
    #Take in the user Chose and match to the output to the userinput
    if chosen == "r":
       return print(f"You have chose {counter[1]} ! \nThe computer chose {random.choice(counter)} ") #print both the users and the computer choses
    elif chosen == "p":
        return print(f"You have chosen {counter[2]} ! \nThe computer chose {random.choice(counter)}  ") #print both the users and the computer choses
    elif chosen == "s":
        return print(f"You have chosen {counter[0]} ! \nThe computer chose {random.choice(counter)}") #print both the users and the computer choses
    else:
        print("Your following input is not r , p or s.") # cpatures any other input other then the choses provided
    

# function to allow the user to choose to play again
def play_again(again):
    if again == "y":
        return True
    elif again == 'n':
        print("Thank you! comae and play with us again")
        return False


main()