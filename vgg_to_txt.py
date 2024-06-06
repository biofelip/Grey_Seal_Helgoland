""" scripts that takes the json labels from VGG labeler and transforms then into a txt per file with the 
 yolo format"""

import json
import os
import glob

json_file="annotations2.json"

with open(json_file) as f:
    data = json.load(f)


image_name=[]
for img in data['images']:
    image_name.append(os.path.basename(img['file_name']))

annotations=data['annotations']

annotations_per_image={x:[] for x,y in enumerate(image_name)}
for annotaiton in annotations:
    image_id=annotaiton['image_id']
    category=annotaiton['category_id']
    xc=annotaiton['bbox'][0]/5312
    yc=annotaiton['bbox'][1]/3984
    w=annotaiton['bbox'][2]/5312
    h=annotaiton['bbox'][3]/3984
    annotations_per_image[image_id].append(f'{category} {xc} {yc} {w} {h}\n')


for id,image  in zip(annotations_per_image.keys(), image_name):
    with open(f'labels\\{image[:-4]}.txt', 'w') as f:
        for line in annotations_per_image[id]:
            f.write(line)

