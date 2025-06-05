import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


my_new_pass =[]

for char in range(0,nr_letters):
    my_new_pass.append(random.choice(letters))
for char in range(0, nr_numbers):
    my_new_pass.append(random.choice(numbers))
for char in range(0, nr_symbols):
    my_new_pass.append(random.choice(symbols))

print(my_new_pass)
random.shuffle(my_new_pass)
print(my_new_pass)

my_password = " "
for char in my_new_pass:
    my_password += char

print(my_password)