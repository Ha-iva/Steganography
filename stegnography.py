from tkinter import *
import os 
from PIL import Image

def encrypt_image():
    msg = message_entry.get()
    passcode = encrypt_passcode_entry.get()
    if not passcode:
        result_label.config(text="Please enter an encryption passcode.")
        return

    img = Image.open( r"D:\vscode\AICTE\image.jpg").convert("RGB")
    pixels = img.load()
    width, height = img.size

    msg_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if msg_index < len(msg):
                ascii_val = ord(msg[msg_index])
                pixels[x, y] = (ascii_val, g, b)
                msg_index += 1
            else:
                break
        if msg_index >= len(msg):
            break

    img.save("encrypted_image.png")
    result_label.config(text="Image Encrypted!")
    os.system("start encrypted_image.png")

def decrypt_image():
    passcode = decrypt_passcode_entry.get()
    original_passcode = encrypt_passcode_entry.get()

    if passcode != original_passcode:
        result_label.config(text="Incorrect decryption passcode.")
        return

    img = Image.open("encrypted_image.png")
    pixels = img.load()
    width, height = img.size
    decrypted_msg = ""
    msg_len = len(message_entry.get())

    msg_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if msg_index < msg_len:
                decrypted_msg += chr(r)
                msg_index += 1
            else:
                break
        if msg_index >= msg_len:
            break

    result_label.config(text="Decrypted message is: " + decrypted_msg)

# Tkinter GUI
root = Tk()
root.title("Steganography")

Label(root, text="Enter your message:").pack()
message_entry = Entry(root, width=50)
message_entry.pack()

Label(root, text="Enter your passcode:").pack()
encrypt_passcode_entry = Entry(root, width=50, show="*")
encrypt_passcode_entry.pack()

encrypt_btn = Button(root, text="Encrypt", command=encrypt_image)
encrypt_btn.pack()

Label(root, text="Enter your passcode:").pack()
decrypt_passcode_entry = Entry(root, width=50, show="*")
decrypt_passcode_entry.pack()

decrypt_btn = Button(root, text="Decrypt", command=decrypt_image)
decrypt_btn.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()