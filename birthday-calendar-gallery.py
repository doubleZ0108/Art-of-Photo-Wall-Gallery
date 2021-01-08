# -*- coding: utf-8 -*-

'''
@program: birthday-calendar-gallery.py

@description: Calendar gallery for my 21. Happy Birthday to myself.🎂

@author: doubleZ

@create: 2021/01/08 
'''

import os
from PIL import Image


def compress(imgs):
    for index, img in enumerate(imgs):
        refactor = Image.open(img).resize((img.size[0]/2, img.size[1]/2), Image.ANTIALIAS)
        refactor.save("compress" + str(index) + ".png")


def join(png1, png2):
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size  # 获取两张图片的大小

    joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
    loc1, loc2 = (0, 0), (0, size1[1])

    '''
    # horizontal
    joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))
    loc1, loc2 = (0, 0), (size1[0], 0)
    
    # vertical
    joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
    loc1, loc2 = (0, 0), (0, size1[1])
    '''

    joint.paste(img2, loc2)
    joint.paste(img1, loc1)
    joint.save(result)


def generate(items, first_path=None):
    try:
        if not first_path:
            path1, path2 = items[0], items[1]
            join(path1, path2)
            items.remove(path1)
            items.remove(path2)
            return generate(items, first_path=result)
        else:
            path2 = items[0]
            join(first_path, path2)
            items.remove(path2)
            return generate(items, first_path=result)
    except:
        pass


def get_all_images(path):
    result = []
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isfile(os.path.join(path, file)):
            if file[-3:] in ('jpg', 'png'):
                result.append(os.path.join(path, file))
    result.sort()
    return result


if __name__ == '__main__':
    path = 'img/'
    result = 'img/result.png'
    imgs = get_all_images(path)
    compress(imgs)
    generate(imgs)



