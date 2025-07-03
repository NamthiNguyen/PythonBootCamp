alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text,shift_amount , direction1):
    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")
        return (cipher_text)


    def decrypt( original_text,shift_amount):
        cipher_text = ""
        for letter2 in original_text:
            postion_back = alphabet.index(letter2)
            new_position = (postion_back - shift_amount) % 26
            cipher_text += alphabet[new_position]
        print(f"Here is the decoded result: {cipher_text}")
        return(cipher_text)

    if direction1 == "encode":
        return(encrypt(original_text,shift_amount))
    elif direction1 == "decode":
        return(decrypt(original_text, shift_amount))
    else:
        print("you chose the wrong direction")


result = caesar(text,shift,direction)
print(result)

# learn how to combine the function into one function
# added a if statement to capture user answer 
# set the condition of the if statement to which ever the user type the corresponding function in side the function will run , using the return statement to return the value
# return in both function is equally important for data to be return 
# in the end you can call the def casar to access both function


#improvement***
#can sperate the decrypt and encrypt function and the if statement
#better variable names