from PIL import ImageEnhance
import random

def add_brightness(image):
    '''
    sets the brightness of the image to the desired value
    '''
    #image brightness enhancer
    value = random.uniform(0.4, 1.4)
    enhancer = ImageEnhance.Brightness(image)
    im_output = enhancer.enhance(value)
    return im_output