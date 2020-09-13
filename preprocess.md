## INTRODUCTION

In order to accomplish preprocessing task, main intuition should be understood well.

We need to prepare the data in order to feed the network. In this task, you should have - `data/masks, data/images` - directories where your prepared masks and input images located, respectively.

You need to write two functions in `src/preprocess.py`, one for image reading and preparing, the other for mask reading and preparing.

1. Image Reading and Preparing

    tensorize_image(image_path, output_shape):

    - image_path, list of strings (paths: ["data/images/img1.png", .., "data/images/imgn.png"] corresponds to n images to be trained each step)
    - output_shape, list of integers (shape = (n1, n2): n1, n2 is width and height of the DNN model's input)

    In a for loop you need to read the images, reshape them for the model and you need to append them in batch_images (list). Lastly, you need to convert the batch_images into torch tensor.

    The tensor should be in [batch_size, output_shape[0], output_shape[1], 3] shape.


2. Mask Reading and preparing

    tensorize_mask(mask_path, output_shape):
    
    - mask_path, list of strings (paths: ["data/masks/mask1.png", .., "data/masks/maskn.png"] corresponds to n masks to be used as labels for each step)
    - output_shape, list of integers (shape = (n1, n2): n1, n2 is width and height of the DNN model's input)

    In a for loop you need to read the images with one channel (not with the shape as HxWx3 but as HxW) reshape them for the model, one-hot encode them (google it) and you need to append them in batch_masks (list). Lastly, you need to convert the batch_images into torch tensor.

    The tensor should be in [batch_size, output_shape[0], output_shape[1], 2] shape.

Your model will accept the input with [batch_size, output_shape[0], output_shape[1], 3] shape and the label with [batch_size, output_shape[0], output_shape[1], 2] shape. 

That means after the task, your data will be ready to the model. Then, we will be proceeding to building the model.