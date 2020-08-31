In order to accomplish json2mask task, data types (list and dictionary) should be understood well.

If you know/learn the aforementioned datatypes this task will be easy peasy (lemon squuezy). 

In our annotation files, json files have the structure as in the following.

    json_dict = {
        "description": empty string
        "tags": list of tag_dict
        "size": size_dict
        "objects": list of object_dict
}

In this dictionary, we will be working on "objects"'s values. Other key-value pairs will not be important.

tag_dict, size_dict are not important but shared in below for whom interested.

    tag_dict = {
        "id": int
        "tagId": int
        "name": string
        "value": string
        "labelerLogin": string
        "createdAt": string
        "updatedAt": string
    }

    size_dict = {
        "height": int
        "width": ing
    }

Our main focus is to find freespace objects. In order to do that, you have to go through every object and check out if the object belongs to "Freespace" classTitle.

If so, you need to get every point of the polygon by calling "exterior" of points.

    object_dict = {
        "id": int
        "classId": int,
        "description": empty string
        "geometryType": string
        "labelerLogin": string,
        "createdAt": string,
        "updatedAt": string,
        "tags": empty list,
        "classTitle": string
        "points": point_dict
    }

    point_dict = {
        "exterior": list of point_list
        "interior": empty list
    }

    point_list : [x, y]


An example is shared in below. In the example I am reading a json file and, I am checking out if the object's id is smaller than 61. If so, I accept the object to use and extract its values, else I continue iterating.

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