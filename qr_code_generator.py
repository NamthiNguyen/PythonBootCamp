import qrcode # Import the qrcode library to generate QR codes
from tkinter import messagebox
import tkinter as tk

def main():
    
    url = input("Enter the text or URL for the QR code: ") #get qr info
    file_name = input("Enter the filename: ") # store name for file qr is being saved too

    qr_rendering(url,file_name) # pass in those two arugments 


# renders the qr here    
def qr_rendering(link, file):
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )

    qr.add_data(link) #add_data fill in the qr info 
    qr.make(fit=True)
    image_qr = qr.make_image(fil_color="black", back_color="white") #color and atribute of the qr code
    image_qr.save(file) #store it to the file name the user inputed

    print(f"✅ Qr code save as {file} ")





if __name__ == "__main__":
    main()
