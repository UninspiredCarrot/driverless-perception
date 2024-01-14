import os
import json
import shutil
import random

folder_path = '/Users/bolt/code/driverless-perception/fsoco_bounding_boxes_train/'
json_folder_path = folder_path + 'bounding_boxes/'

write_folder = '/Users/bolt/code/driverless-perception/fsoco-YOLO/'

def normalize_coordinates(className, x, y, width, height, img_width, img_height):
    if 'blue' in object['classTitle']:
        className = 0
    elif 'yellow' in object['classTitle']:
        className = 1
    elif 'orange' in object['classTitle']:
        className = 2
    elif 'unknown' in object['classTitle']:
        className = 3

    x_center = (x + width / 2) / img_width
    y_center = (y + height / 2) / img_height
    normalized_width = width / img_width
    normalized_height = height / img_height
    return map(str, [className, x_center, y_center, normalized_width, normalized_height])
        
for folder_name in os.listdir(folder_path):
    if os.path.isdir(folder_path + folder_name):

        for filename in os.listdir(folder_path + folder_name + '/img/'):

            random_float = random.random()

            if random_float < 0.8:
                choice = 'train/'
            elif random_float < 0.9:
                choice = 'val/'
            else:
                choice = 'test/'
        
            shutil.copy(folder_path + folder_name + '/img/' + filename, write_folder + choice + 'images/' + filename)

            try:
                with open(folder_path + folder_name + '/ann/' + filename[:-3] + 'jpg.json', 'r') as json_file:
                    data = json.load(json_file)
            except FileNotFoundError:
                with open(folder_path + folder_name + '/ann/' + filename[:-3] + 'png.json', 'r') as json_file:
                    data = json.load(json_file)
                    

            with open(write_folder + choice +  'labels/' + filename[:-3] + 'txt', 'w') as txt_file:

                for object in data['objects']:

                    
                    [x1, y1], [x2, y2] = object['points']['exterior']

                    image_width = data['size']['width']
                    image_height = data['size']['height']

                    txt_file.write(' '.join(normalize_coordinates(object['classTitle'], x1, y1, x2, y2, image_width, image_height)) + '\n')