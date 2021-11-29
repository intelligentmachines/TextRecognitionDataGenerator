from PIL import ImageEnhance


def add_brightness(image,value):
    '''
    sets the brightness of the image to the desired value
    '''
    #image brightness enhancer
    enhancer = ImageEnhance.Brightness(image)
    im_output = enhancer.enhance(value)
    return im_output