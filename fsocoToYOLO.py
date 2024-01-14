import os
import json

folder_path = '/Users/bolt/code/driverless-perception/fsoco_sample/'
json_folder_path = folder_path + 'bounding_boxes/'

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
        


for filename in os.listdir(folder_path + 'bounding_boxes/'):

    with open(folder_path + 'bounding_boxes/' + filename, 'r') as json_file:
        data = json.load(json_file)

    with open(folder_path + 'bounding-boxes-YOLO/' + filename[:-9] + '.txt', 'w') as txt_file:

        for object in data['objects']:

            
            [x1, y1], [x2, y2] = object['points']['exterior']

            image_width = data['size']['width']
            image_height = data['size']['height']

            txt_file.write(' '.join(normalize_coordinates(object['classTitle'], x1, y1, x2, y2, image_width, image_height)) + '\n')
    
        

