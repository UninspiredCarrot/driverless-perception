import cv2
import numpy as np

def get_right_point(left_image, right_image, xl, y, width, height, grayscale=False):
    # if grayscale:
    #     left_image = cv2.imread(left_image, cv2.IMREAD_GRAYSCALE)
    #     right_image = cv2.imread(right_image, cv2.IMREAD_GRAYSCALE)
    # else:
    #     left_image = cv2.imread(left_image)
    #     right_image = cv2.imread(right_image)
    top = y - height//2
    bottom = y + height//2
    if top < 0:
        bottom -= top
        top = 0
    if bottom >= len(left_image):
        top -= len(left_image) - bottom - 1
        bottom = len(left_image) - 1
    left = xl - width//2
    right = xl + width//2
    if left < 0:
        print('used')
        right -= left
        left = 0
    if right >= len(left_image[0]):
        print('used')
        left -= len(left_image[0]) - right - 1
        right = len(left_image[0]) - 1
    template = left_image[top:bottom, left:right]

    min_similarity = float('inf')
    xr = xl

    for xi in range(xl, xl - left, -1):
        window = right_image[top:bottom, xi - (xl - left) : xi + (right - xl)]
        similarity = np.sum((template - window)**2)
        if similarity < min_similarity:
            min_similarity = similarity
            xr = xi
    return xr