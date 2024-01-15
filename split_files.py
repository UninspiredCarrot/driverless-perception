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




# write_folder = '/Users/bolt/code/driverless-perception/fsoco-YOLO/'
        
# for folder_name in os.listdir(folder_path):
#     if os.path.isdir(folder_path + folder_name):

#         for filename in os.listdir(folder_path + folder_name + '/img/'):

#             random_float = random.random()

#             if random_float < 0.8:
#                 choice = 'train/'
#             elif random_float < 0.9:
#                 choice = 'val/'
#             else:
#                 choice = 'test/'
        
#             shutil.copy(folder_path + folder_name + '/img/' + filename, write_folder + 'images/' + filename)

#             try:
#                 with open(folder_path + folder_name + '/ann/' + filename[:-3] + 'jpg.json', 'r') as json_file:
#                     data = json.load(json_file)
#             except FileNotFoundError:
#                 with open(folder_path + folder_name + '/ann/' + filename[:-3] + 'png.json', 'r') as json_file:
#                     data = json.load(json_file)
                    

#             with open(write_folder +  'labels/' + filename[:-3] + 'txt', 'w') as txt_file:

#                 for object in data['objects']:

                    
#                     [x1, y1], [x2, y2] = object['points']['exterior']

#                     image_width = data['size']['width']
#                     image_height = data['size']['height']

#                     txt_file.write(' '.join(normalize_coordinates(object['classTitle'], x1, y1, x2, y2, image_width, image_height)) + '\n')


