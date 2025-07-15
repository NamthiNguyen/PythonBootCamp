def format_name(first_name, last_name):
    #.capitalize() function capitalize the first letter 
    #using [0].upper() only give you back the first inital as a capitalize which return only those char
    first_name_fix = first_name.capitalize()
    last_name_fix = last_name.capitalize()
    full_name_fix = first_name_fix + " " +last_name_fix

    return full_name_fix

first_name = input("please type your first name ")
last_name = input("please type your last name ")

full_name = format_name(first_name, last_name)

print(full_name)

