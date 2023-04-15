import cv2

import numpy as np
import matplotlib.pyplot as plt

FIGSIZE = (12, 8)

def read_image(path):
    """Reads image in RGB colors
    
    Args:
        - path: path to image

    Returns:
        - image: read image from path
    """
    image = cv2.imread(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def show_image(image):
    """Displays image
    
    Args:
        - image: RGB image to display
    """
    plt.figure(figsize=FIGSIZE)
    plt.imshow(image)
    plt.show()

def sort_image(image, axis=-1):
    """Sort image along one of axis
    
    Args:
        - image: RGB image to sort
        - axis: axis along which the image will be sorted

    Returns:
        - sorted_image: image sorted along one of its axises
    """
    return np.sort(image, kind='mergesort', axis=axis)

def main():
    image = read_image('lena.png')
    image = sort_image(image, 0)
    show_image(image)
    

if __name__ ==  '__main__':
    main()