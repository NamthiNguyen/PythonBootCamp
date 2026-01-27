import random

round_active = True

def main():
   start = input("Roll the dice? (y/n): ").lower()
   if start == "y":
    startgame()
   else:
      print("Thank you for playing!")

def rolldice():
   
   dice1= random.randint(1,6)
   dice2= random.randint(1,6)

   return [dice1,dice2]


def startgame():
    global round_active
    while round_active:
       result =rolldice()
       print(result)
       roll = input("Roll the dice? (y/n): ").lower()

       if roll != "y":
          round_active = False



main()

