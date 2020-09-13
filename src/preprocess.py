import cv2, torch
import numpy as np
import glob

def tensorize_image(image_path_list, output_shape):
    image_list = []
    for image_path in image_path_list:
        image = cv2.imread(image_path)
        image = cv2.resize(image, output_shape)
        image_list.append(image)
    image_array = np.array(image_list, dtype=np.float32)
    torch_image = torch.from_numpy(image_array)
    image_tensor = torch_image.cuda()
    return image_tensor
    

def tensorize_mask(mask_path_list, output_shape, n_class):
    mask_list = []
    for mask_path in mask_path_list:
        mask = cv2.imread(mask_path, 0)
        mask = cv2.resize(mask, output_shape)
        mask = one_hot_encoder(mask, n_class)
        mask_list.append(mask)
    mask_array = np.array(mask_list, dtype=np.int)
    torch_mask = torch.from_numpy(mask_array)
    mask_tensor = torch_mask.cuda()
    return mask_tensor


def one_hot_encoder(data, n_class):
    encoded_data = np.zeros((*data.shape, n_class), dtype=np.int) # (width, height, number_of_class)'lık bir array tanımlıyorum.
    encoded_labels = [0] * n_class # buraya da [0, 0, .., 0] (n tane 0) bir encoded_labels, bizim durumumuz için [0, 0] oluyor bu (n=2)
    for lbl in range(n_class):
        encoded_labels[lbl] = 1 # lbl = 0 için (arkaplan) [1, 0] labelini oluşturuyorum, 
                                # lbl = 1 için (freespace) [0, 1] labelini oluşturuyorum.
        numerical_class_inds = data[:,:] == lbl # lbl = 0 için data'nın 0'a eşit olduğu w,h ikililerini alıyorum diyelim ki (F).
                                                # lbl = 1 için data'nın 1'e eşit olduğu w,h ikililerini alıyorum diyelim ki (O).
        encoded_data[numerical_class_inds] = encoded_labels # lbl = 0 için tüm F'in sahip olduğu tüm w,h ikililerini [1, 0]'a eşitliyorum.
                                                            # lbl = 1 için tüm O'un sahip olduğu tüm w,h ikililerini [0, 1]'e eşitliyorum.
    return encoded_data

if __name__ == '__main__':


    image_list = glob.glob('../data/images/*')
    image_list.sort()
    batch_image_list = image_list[:4]
    batch_image_tensor = tensorize_image(batch_image_list, (224, 224))


    print(batch_image_list)
    print(batch_image_tensor.dtype)
    print(type(batch_image_tensor))
    print(batch_image_tensor.shape)


    mask_list = glob.glob('../data/masks/*')
    mask_list.sort()
    batch_mask_list = mask_list[:4]
    batch_mask_tensor = tensorize_mask(batch_mask_list, (224, 224), 2)


    print(batch_mask_list)
    print(batch_mask_tensor.dtype)
    print(type(batch_mask_tensor))
    print(batch_mask_tensor.shape)  