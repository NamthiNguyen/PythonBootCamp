import qrcode # Import the qrcode library to generate QR codes
from tkinter import messagebox
import tkinter as tk


# renders the qr here    
def qr_rendering():
    data = url_entry.get()
    filename = filename_entry.get()

    if not data or not filename:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )

    qr.add_data(data) #add_data fill in the qr info 
    qr.make(fit=True)
    image_qr = qr.make_image(fill_color="black", back_color="white") #color and atribute of the qr code
    image_qr.save(filename) #store it to the file name the user inputed

    messagebox.showinfo("Success", f"QR Code saved as {filename}.png")


app = tk.Tk()
app.title("QR Maker")
app.geometry("400x300")

tk.Label(app, text="URL or Text").pack()
url_entry = tk.Entry(app)
url_entry.pack()

tk.Label(app, text="Tip %").pack()
filename_entry = tk.Entry(app)
filename_entry.pack()

tk.Button(app,text= "Render", command=qr_rendering).pack(pady=10)



app.mainloop()