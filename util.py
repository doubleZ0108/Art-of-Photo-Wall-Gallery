# -*- coding: utf-8 -*-

'''
@program: util.py

@description: 

@author: doubleZ

@create: 2021/01/09 
'''
import os
import cv2
from PIL import Image
import numpy as np

def crack(integer):
    start = int(integer ** 0.5)
    factor = integer / start
    while int(factor) != factor:
        start += 1
        factor = integer / start
    return start, int(factor)       # start <= factor


def get_all_images(path):
    result = []
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isfile(os.path.join(path, file)):
            if file[-3:] in ('jpg', 'png'):
                result.append(os.path.join(path, file))
    result.sort()
    return result

def map_level(level):
    level *= 5
    return level if level%2!=0 else level + 1
'''
_blur
    高斯模糊
    Gaussian Blur
'''
def blur(img, kernel):
    '''

    :param img:
    :param kernel: must be odd number
    :return:
    '''
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

    kernel_size = (kernel, kernel)
    blur_img = cv2.GaussianBlur(img,kernel_size,0)

    return Image.fromarray(cv2.cvtColor(blur_img,cv2.COLOR_BGR2RGB))