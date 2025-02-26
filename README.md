# Steganography

This project is based on **Steganography**, which allows users to input a message and passcode. The message is then encrypted into a default image provided. The project also supports decryption, where the correct passcode is required to retrieve the hidden message.

### Modules Used:
- **Pillow (PIL)** for image processing
- **Tkinter** for the graphical user interface (GUI)
- **OS** for system access

### How it Works:
1. The code accepts a **message** and a **passcode**.
2. The message is **encoded into the pixels** of the provided image. The image is slightly altered, but the changes are subtle and not easily noticeable.
3. During **decryption**, the user must enter the **passcode**.
4. If the entered passcode matches the encryption passcode, the hidden **message** is revealed.

---

This project demonstrates a basic implementation of hiding information within an image, providing a simple yet effective means of secure communication.
