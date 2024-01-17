import os
import random

folder_path = '/Users/bolt/code/driverless-perception/fsoco-YOLO/'

for filename in os.listdir(folder_path + 'images/'):
    if not os.path.isdir(folder_path + 'images/' + filename):
        random_float = random.random()

        if random_float < 0.8:
            choice = 'train/'
        elif random_float < 0.9:
            choice = 'val/'
        else:
            choice = 'test/'
        os.rename(folder_path + 'images/' + filename, folder_path + 'images/' + choice + filename)
        os.rename(folder_path + 'labels/' + filename + '.txt', folder_path + 'labels/' + choice + filename[:-4] + '.txt')