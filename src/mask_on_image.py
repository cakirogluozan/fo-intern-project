import os, cv2, tqdm
import numpy as np


MASK_DIR  = '../data/masks'
IMAGE_DIR = '../data/images'
IMAGE_OUT_DIR = '../data/masked_images'

if not os.path.exists(IMAGE_OUT_DIR):
    os.mkdir(IMAGE_OUT_DIR)


mask_list = os.listdir(MASK_DIR)

for mask_name in tqdm.tqdm(mask_list):
    mask_path      = os.path.join(MASK_DIR, mask_name)
    image_path     = os.path.join(IMAGE_DIR, mask_name)
    image_out_path = os.path.join(IMAGE_OUT_DIR, mask_name)

    mask  = cv2.imread(mask_path, 0).astype(np.uint8)
    image = cv2.imread(image_path).astype(np.uint8)

    mask_ind   = mask == 1
    cpy_image  = image.copy()
    image[mask==1, :] = (255, 0, 125)
    opac_image = (image/2 + cpy_image/2).astype(np.uint8)
    
    cv2.imwrite(image_out_path, opac_image)
    if False:
        cv2.imshow('o', opac_image)
        cv2.waitKey(1)
