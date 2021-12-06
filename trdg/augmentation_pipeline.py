import os
import random as rnd
import cv2
import numpy as np
from PIL import ImageEnhance
from PIL import Image


def noisy(image):
    '''Adds extra noise to image
    image (nd array) : input image
    '''
    types = ['gauss', 'poisson', 's&p']
    noise_typ = rnd.choice(types)
    
    if noise_typ == "gauss":
        row,col= image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col))
        gauss = gauss.reshape(row,col)
        noisy = np.uint8(image + gauss)
        return noisy
    
    elif noise_typ == "s&p":
        s_vs_p = 0.5
        amount = 0.06  ## make random
        out = np.copy(image)

        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 0.5

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0.8
        return out
    
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy

def gradient(image):
    '''Applies gradient in random direction
    image (nd array): input image
    '''
    # direction is specified here
    directions = [1, 2]
    direction = rnd.choice(directions)

    # gradient colour thresholds are specified here
    threshold1 = rnd.uniform(0.3, 1)
    threshold2 = rnd.uniform(0.3, 1)

    if direction == 1:
        mask = np.tile(np.linspace(threshold1, threshold2, image.shape[1]), (image.shape[0], 1))
    elif direction == 2:
        mask = np.tile(np.linspace(threshold1, threshold2, image.shape[0]), (image.shape[1], 1)).T
    gradient_image = np.uint8(image * mask)
    return gradient_image

def add_brightness(image):
    '''
    sets the brightness of the image to the desired value
    '''
    #image brightness enhancer
    value = rnd.uniform(0.4, 1.4)
    enhancer = ImageEnhance.Brightness(Image.fromarray(image))
    im_output = enhancer.enhance(value)
    return im_output

def get_random_crop(image):
    '''
    Randomly crops a portion of the image
    '''
    # image = Image.fromarray(image)
    width = image.shape[1]
    height = image.shape[0]
    
    if width <= 16 or height <= 32:
        return image

    crop_height_up = rnd.randint(0,8)
    crop_height_down = rnd.randint(0,8)
    crop_width_left = rnd.randint(0,7)
    crop_width_right = rnd.randint(0,7)

    
    area = (crop_width_left, crop_height_up, width - crop_width_right, height-crop_height_down)
    crop = image.crop(area)

    return crop

def main(args):
    for filename in os.listdir(args.i):

        image = cv2.imread(filename, 0)

        output_path = args.o + filename.split('.')[0] + "_crop.jpg"

        output_image = get_random_crop(image)

        Image.fromarray(output_image).save(output_path)


    return

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input image dir")
    parser.add_argument("-o", "--o", type=str, default="out/vis", help="Image output dir")
    args = parser.parse_args()
    os.makedirs(args.o, exist_ok=True)
    main(args)

'''
python augmentation_pipeline.py \
--i /home/arowa/work/porichoy/trdg-output-images/bangla_dataset_v1/images \
--o /home/arowa/work/porichoy/trdg-output-images/bangla_dataset_v1/crop_img
'''