# -*- coding: utf-8 -*-

'''
@program: generate.py

@description: 

@author: doubleZ

@create: 2021/01/09 
'''

import util
from PIL import Image
import numpy as np


def generate_photo_wall_gallery(imgUrls, resultUrl, targetSize, blur_level):
    w, h = util.crack(len(imgUrls))

    imgs = []
    for imgUrl in imgUrls:
        img = Image.open(imgUrl).resize(targetSize)
        imgs.append(img)

    joint = Image.new('RGB', (targetSize[0]*h, targetSize[1]*w))
    for i in range(w):
        for j in range(h):
            index = i * h + j
            loc = (targetSize[0] * j, targetSize[1] * i)
            joint.paste(imgs[index], loc)
    blur_joint = util.blur(np.array(joint), util.map_level(blur_level))
    blur_joint.save(resultUrl)



if __name__ == '__main__':

    path = 'img/'              # 图片文件夹路径

    imgUrls = util.get_all_images(path)

    generate_photo_wall_gallery(imgUrls, resultUrl='img/result.png', targetSize=(400, 300), blur_level=6)

