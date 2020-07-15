import numpy as np
import cv2

def noise_image(image, factor):

    row, col, channel = image.shape
    gauss = np.random.randn(row, col, channel)
    assert (gauss.shape == (row, col, channel))

    noisy_image = np.add(image, np.multiply(image, np.multiply(gauss, factor)))

    return noisy_image
