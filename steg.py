# Import libraries
import cv2                  # for image processing
import numpy as np          # for arrays
import matplotlib.pyplot as plt  # for displaying images

# ASCII conversion dictionaries
d = {chr(i): i for i in range(255)}     # character to ASCII
c = {i: chr(i) for i in range(255)}     # ASCII to character

# Cover image path
image_path = "E:/projects/snake game/snakebg.jpg"
x = cv2.imread(image_path)

# Convert to RGB for visualization
xrgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
plt.imshow(xrgb)
plt.axis("off")
plt.title("Original Image")
plt.show()

# Message and key
text = "https://www.youtube.com/"
text_ascii = [d[ch] for ch in text]
l = len(text)

# Create a grayscale version for edge detection
gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

# Generate edge mask using Canny
edges = cv2.Canny(gray, 100, 200)
mask = edges > 0  # Boolean mask of edge pixels

# Encrypt using masking
x_enc = x.copy()
h, w, _ = x.shape

idx = 0  # message index
for i in range(h):
    for j in range(w):
        if mask[i, j] and idx < l:
            for z in range(3):  # Use R, G, B
                if idx < l:
                    x_enc[i, j, z] = text_ascii[idx]  # Overwrite value (simple embed)
                    idx += 1

# Save and show encrypted image
cv2.imwrite("masked_encrypted.jpg", x_enc)
x_enc_rgb = cv2.cvtColor(x_enc, cv2.COLOR_BGR2RGB)
plt.imshow(x_enc_rgb)
plt.axis("off")
plt.title("Masked Encrypted Image")
plt.show()

# Decryption
idx = 0
decrypt = ""
for i in range(h):
    for j in range(w):
        if mask[i, j] and idx < l:
            for z in range(3):
                if idx < l:
                    val = x_enc[i, j, z]
                    decrypt += c[val]
                    idx += 1

print("🔓 Decrypted Message:", decrypt)
