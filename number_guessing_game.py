import random
def main():

    comp = computerguess()
    print("(Debug) Computer chose:", comp)
    user = userguess()

    while True:                   #control the loop for the hot and cold hint
        user = userguess()        # this ask the user 
        if hotandcold(comp,user): # this loops is control here , if user not correct it return True or False
            break                 # once true it break the loop

  
def computerguess():
    return random.randint(1,100)

def userguess():
    while True:
        try:
            return int(input("Guess the number (between 1 and 100): "))
        except ValueError:
            print("❌ Please enter a valid number.")
        

def hotandcold(generated,answer):
    if answer > generated:
        print( "Too High, Please Try to Guess again")
        return False # help to conntinue the loop
    elif answer < generated:
        print("Too Low, Please Try Again")
        return False # help to conntinue the loop
    else:
        print(f"you are correct the answer is {generated}")
        return True # help to conntinue the loop

main()