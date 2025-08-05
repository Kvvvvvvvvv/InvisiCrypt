import cv2
import os

# Load image
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found.")
    exit()

# Load password
password_file = "password.txt"
if not os.path.exists(password_file):
    print("Error: Password file not found.")
    exit()

with open(password_file, "r") as f:
    stored_password = f.read().strip()

# Ask user for password
pas = input("Enter passcode for Decryption: ")

# Dictionary for int to char
c = {i: chr(i) for i in range(255)}

# Decrypt if password matches
if stored_password == pas:
    n, m, z = 0, 0, 0
    message = ""
    while n < img.shape[0] and m < img.shape[1]:
        pixel_value = int(img[n, m, z])
        if pixel_value == 0:
            break
        message += c[pixel_value]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
