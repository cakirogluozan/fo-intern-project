import numpy as np
import cv2
import json
import os

JSON_DIR  = '../data/ex_jsons'
json_name = 'ozan.json'
json_path = os.path.join(JSON_DIR, json_name)
json_file = open(json_path, 'r')
json_dict = json.load(json_file)
json_objs = json_dict["objects"]

for obj in json_objs:
    obj_id = obj['id']
    if obj_id > 61:
        # this is my condition that I want
        print('I like it')
    else:
        continue