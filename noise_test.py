import noise
import cv2
import numpy as np

img = cv2.imread('green.jpeg')
img = np.uint8(noise.noise_image(img, 0.5))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.desAllWindows()
