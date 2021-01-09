# -*- coding: utf-8 -*-

'''
@program: generate.py

@description: main function for generating photo wall gallery

@author: doubleZ

@create: 2021/01/09 
'''

import argparse
from PIL import Image
import numpy as np

import util


def generate_photo_wall_gallery(imgUrls, targetSize=(400,400), blur_level=6, resultUrl='img/result/result.png'):
    '''
    main function for generate photo wall gallery
    :param imgUrls: a list of images url
    :param targetSize: size for each small pictures in the joint(must be the same)
    :param blur_level: blur level for result image(0~10)
    :param resultUrl: url for result image
    '''
    w, h = util.crack(len(imgUrls))     # w and h are the two closest number that w*h=len(imgUrls)

    # read images and resize them
    imgs = []
    for imgUrl in imgUrls:
        img = Image.open(imgUrl).resize(targetSize)
        imgs.append(img)

    # joint result image
    joint_img = Image.new('RGB', (targetSize[0]*h, targetSize[1]*w))
    for i in range(w):
        for j in range(h):
            index = i * h + j
            loc = (targetSize[0] * j, targetSize[1] * i)
            joint_img.paste(imgs[index], loc)

    # blur the result image
    blur_joint_img = joint_img if blur_level ==0 else util.blur(np.array(joint_img), util.map_level(blur_level))

    blur_joint_img.save(resultUrl)
    print("Photo Wall Gallery done!!!🎉")



if __name__ == '__main__':

    path = 'img/'       # url for original images

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="Target size using for resize and uniform picture(400*400 as default) [e.g. (300,400)]",
                        type=int, default=(400,400), nargs='+')
    parser.add_argument("-b", "--blur", help="Blur level for result image(0~10, 6 as default) [e.g. 6]",
                        type=str, choices=[str(_) for _ in range(11)], default='6')
    args = parser.parse_args()

    if args.size and args.blur:
        imgUrls = util.get_all_images(path)
        generate_photo_wall_gallery(imgUrls, targetSize=tuple(args.size), blur_level=int(args.blur))
    else:
        print(args.size, args.blur)
        print("args maybe wrong, please try another time")
