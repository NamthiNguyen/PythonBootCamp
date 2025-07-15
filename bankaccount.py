class BankAccount:
  def __init__(self, owner: str, balance: float) -> None:
    self.owner = owner
    self.balance = balance

  def deposit(self, amount: float):
    self.balance += amount
    print(newbalance)

  def withdraw(self, amount: float):
    if self.balance - amount < 0:
      print("Insufficient funds")
    else:
      print(check)

  def get_balance(self):
    print(f"Your current balance = {self.balance}")


# ✅ Create an instance of BankAccount
payroll : BankAccount = BankAccount("Namthi Nguyen", 100)

# ✅ Use class methods
payroll.deposit(100)
payroll.withdraw(10)
payroll.get_balance()

#working with python classes
#created a class call bankaccount
#give the class an  initializer method which is def __init__(self)
#when you create and instance of this class aka payroll : BankAccount = BankAccount("Namthi Nguyen, 100")
#essintially your making a copy of the class and making an object of it. 
    #first give the object a name payroll
    #then connect it to the class Bankaccount
    #initialize a copy of the class and give it parameters 
    #now payroll can access all the class methods

# We're working with Python classes.

# We created a class called BankAccount.
# It has an initializer method (__init__) to set up the owner and balance.

# When you create an instance of this class, like:
# payroll = BankAccount("Namthi Nguyen", 100)

# You're making an object (called 'payroll') from the class.

# Now, the 'payroll' object has access to all the class methods,
# such as deposit(), withdraw(), and get_balance().
