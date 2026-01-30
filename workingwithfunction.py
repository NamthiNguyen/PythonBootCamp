def format_name(first_name, last_name):
    first_name_fix = first_name.capitalize()
    last_name_fix = last_name.capitalize()
    full_name_fix = first_name_fix + " " +last_name_fix

    return full_name_fix

first_name = input("please type your first name ")
last_name = input("please type your last name ")
full_name = format_name(first_name, last_name)

print(full_name)

def function_1(text):
    return text + text

def function_2(text):
    #this also make the word capitalize but it more better since it recongize each word in the text
    return text.title()

output = function_1("hello")

#using the return result of the result from function one and put it as an input into function 2
output2 = function_2(function_1("bye"))