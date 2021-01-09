# -*- coding: utf-8 -*-

'''
@program: generate.py

@description: 

@author: doubleZ

@create: 2021/01/09 
'''

import argparse
from PIL import Image
import numpy as np

import util


def generate_photo_wall_gallery(imgUrls, targetSize=(400,400), blur_level=6, resultUrl='img/result/result.png'):
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

    blur_joint = joint if blur_level ==0 else util.blur(np.array(joint), util.map_level(blur_level))

    blur_joint.save(resultUrl)
    print("Photo Wall Gallery done!!!🎉")



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="Target size using for resize and uniform picture(400*400 as default) [e.g. (300,400)]",
                        type=int, default=(400,400), nargs='+')
    parser.add_argument("-b", "--blur", help="Blur level for result image(0~10, 6 as default) [e.g. 6]",
                        type=str, choices=[str(_) for _ in range(11)], default='6')
    args = parser.parse_args()

    if args.size and args.blur:
        path = 'img/'  # 图片文件夹路径
        imgUrls = util.get_all_images(path)
        generate_photo_wall_gallery(imgUrls, targetSize=tuple(args.size), blur_level=int(args.blur))
    else:
        print(args.size, args.blur)
        print("args maybe wrong, please try another time")
