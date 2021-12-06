import numpy as np
import random

def get_random_crop(image):
    '''
    Randomly crops a portion of the image
    '''
    width = image.size[0]
    height = image.size[1]

    crop_height_up = random.randint(0,8)
    crop_height_down = random.randint(0,8)
    crop_width_left = random.randint(0,7)
    crop_width_right = random.randint(0,7)

    
    area = (crop_width_left, crop_height_up, width - crop_width_right, height-crop_height_down)
    crop = image.crop(area)

    return crop