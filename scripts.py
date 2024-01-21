import os

classes = set()

for filename in os.listdir('/Users/bolt/code/driverless-perception/fsoco-YOLO-all/labels'):
    lines = open('/Users/bolt/code/driverless-perception/fsoco-YOLO-all/labels/'+filename).read().split('/n')
    for line in lines:
        class_ = line.split()[0]
        classes.add(class_)

print(classes)