import cv2
import os

# Load image
img = cv2.imread("img2.webp")
if img is None:
    print("Error: Image not found or could not be loaded.")
    exit()

# Input message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionary for char to int
d = {chr(i): i for i in range(255)}

# Embed message into image pixels
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1

# Add 0 as end-of-message marker
img[n, m, z] = 0

# Save encrypted image
cv2.imwrite("encryptedImage.png", img)

# Save password
with open("password.txt", "w") as f:
    f.write(password)

print("Message encrypted and saved in 'encryptedImage.png'")
