import numpy as np
import cv2
import json
import os

MASK_DIR  = '../data/masks'
if not os.path.exists(MASK_DIR):
    os.mkdir(MASK_DIR)

JSON_DIR  = '../data/jsons'
json_name = 'ozan.json'
json_path = os.path.join(JSON_DIR, json_name)
json_file = open(json_path, 'r')
json_dict = json.load(json_file)
json_desc = json_dict["description"]
json_tags = json_dict["tags"]
json_size = json_dict["size"]
width     = json_size['width']
height    = json_size['height']
json_objs = json_dict["objects"]

mask = np.zeros((height, width), dtype=np.uint8)

for obj in json_objs:
    obj_id = obj['id']
    obj_class = obj['classTitle']
    if obj_id > 61 and obj_class == "Freespace":
        # this is my condition that I want
        obj_pts = obj['points']
        obj_ext_pts = obj_pts['exterior'] # this is the point list we want
        cv2.fillPoly(mask, np.array([obj_ext_pts]), 255) #

        mask_name = json_name.split('.')[-1] + '.png'
        mask_path = os.path.join(MASK_DIR, mask_name)
        cv2.imwrite(mask_path, mask)