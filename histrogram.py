import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('123.png', cv2.IMREAD_GRAYSCALE)

# Get the image dimensions
height, width = img.shape

# Initialize an empty array to store the intensity values
intensity = np.zeros(width)

start_row = 200
stop_row = 200
# Loop through each row of the image and sum up the pixel values
for i in range(start_row, stop_row + 1):
    intensity += img[i,:]   
    print(intensity)
# Plot the intensity values

line_color = (0, 0, 255)  # (B, G, R) format
line_thickness = 2

cv2.line(img, (0, start_row), (img.shape[1], start_row), line_color, line_thickness)
# cv2.imshow("img", img)
plt.plot(intensity)
plt.imshow(img, cmap='gray')
plt.show()

