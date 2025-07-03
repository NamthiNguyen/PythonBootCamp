alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def encrypt(original_text, shift_amount):
    encrypt_text = ""
    for letter in original_text:
        #.index() find the index of the letter pass into it
        position = alphabet.index(letter)
        #add the shift amount to the  index of the letter and loop through the alphabest
        new_position = (position + shift_amount) % 26
        #store the next letter by the new index given to the variable encrypted text
        encrypt_text += alphabet[new_position]
    return(encrypt_text)

result = encrypt(text, shift)
print(result)

#concept that can be learn. how to find the index of letter in a list 
#looping through a string and it char
#using the index function to find the index and then adding to that value to change the value of the index
#creating a variable in a function and not in a loop function to update the state of the varible and not just reset it, so every time the for loop function is call it doesnt reset the value