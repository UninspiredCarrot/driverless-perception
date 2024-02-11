import numpy as np



def get_right_point(left_image, right_image, xl, y, width, height, previous_disparity):
    # left_image = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
    # right_image = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)
    top = y - height//2
    bottom = y + height//2
    if top < 0:
        top = 0
    if bottom >= len(left_image):
        bottom = len(left_image) - 1
    left = xl - width//2
    right = xl + width//2
    if left < 0:
        left = 0
    if right >= len(left_image[0]):
        right = len(left_image[0]) - 1
    template = left_image[top:bottom, left:right]


    min_similarity = float('inf')
    xr = xl

    start = xl - previous_disparity
    if start < width//2:
        start = width//2

    for xi in range(start, xl):
        window = right_image[top:bottom, xi - width//2 : xi + width//2]
        similarity = np.sum((template - window)**2)
        if similarity < min_similarity:
            min_similarity = similarity
            xr = xi
    return xr