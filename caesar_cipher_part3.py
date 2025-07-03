# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
restart_program = False

while not restart_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'end' to end the program:\n").lower()
    if direction == "end" :
        restart_program = True
        print("goodbye!")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


#applying while loop to give the code a continious flow till the user want to end
# importing logo and using it 
# adding a catch for unknow letter

