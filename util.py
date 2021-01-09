# -*- coding: utf-8 -*-

'''
@program: util.py

@description: useful utils for auxiliary generating

@author: doubleZ

@create: 2021/01/09 
'''
import os
import cv2
from PIL import Image
import numpy as np


def crack(integer):
    '''
    divide an integer into two closest number ($1 * $2)
    :param integer: integer waiting for divide
    :return: two factor of this integer, $1 <= $2
    '''
    start = int(integer ** 0.5)
    factor = integer / start
    while int(factor) != factor:    # if it's an integer
        start += 1
        factor = integer / start
    return start, int(factor)  # start <= factor


def get_all_images(path):
    '''
    get all images in this path ending with .jpg or .png
    :param path: path of the image folder
    :return: a list of images url
    '''
    result = []
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isfile(os.path.join(path, file)):
            if file[-4:] in ('.jpg', '.png'):
                result.append(os.path.join(path, file))
    result.sort()
    return result


def map_level(level, factor=15):
    '''
    map the origin level for magnifying effect
    :param level: bluring level
    :param factor: factor for magnifying effect
    :return: refactor level
    '''
    level *= factor
    return level if level % 2 != 0 else level + 1


def blur(img, kernel=91):
    '''
    use Gaussian Function to blur an image
    :param img: origin image in np.array format
    :param kernel: size of the Gaussian kernel(must be odd number)
    :return: blured image in PIL.Image format
    '''
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    kernel_size = (kernel, kernel)
    blur_img = cv2.GaussianBlur(img, kernel_size, 0)

    return Image.fromarray(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
