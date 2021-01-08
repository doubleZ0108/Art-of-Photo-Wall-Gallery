# -*- coding: utf-8 -*-

'''
@program: main.py

@description: 

@author: doubleZ

@create: 2021/01/07 
'''


import os
from PIL import Image

def compress(imgs):
    for index, img in enumerate(imgs):
        refactor = Image.open(img).resize((10080, 858), Image.ANTIALIAS)
        refactor.save("refactor" + str(index) + ".png")

# def join_save(png1, png2):
#     img1, img2 = Image.open(png1).resize((myresize['x'], myresize['y']), Image.ANTIALIAS), Image.open(png2).resize((myresize['x'], myresize['y']), Image.ANTIALIAS)
#     size1, size2 = img1.size, img2.size  # 获取两张图片的大小
#     joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
#     # 新建一张新的图片
#     # 因为拼接的图片的宽都是一样，所以宽为固定值
#     loc1, loc2 = (0, 0), (0, size1[1])
#     # 两张图片的位置
#     # a-------------
#     # |            |
#     # |            |
#     # |            |
#     # |            |
#     # |            |
#     # b------------|
#     # |            |
#     # |            |
#     # |            |
#     # |            |
#     # |------------|
#
#     # 位置都是以该图片的左上角的坐标决定
#     # 第一张图片的左上角为a点，a的坐标为(0,0)
#     # 第二张图片的左上角为b点，a的横坐标为0，纵坐标为第一张图片的纵坐标减去第二张图片上移的size: (0, size[1]-size)
#
#     joint.paste(img2, loc2)
#     joint.paste(img1, loc1)
#     # 因为需要让第一张图片放置在图层的最上面,所以让第一张图片最后最后附着上图片上
#     joint.save(result)

def join_horizontal(png1, png2):
    img1, img2 = Image.open(png1), Image.open(png2)

    size1, size2 = img1.size, img2.size  # 获取两张图片的大小
    joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))

    loc1, loc2 = (0, 0), (size1[0], 0)

    joint.paste(img2, loc2)
    joint.paste(img1, loc1)
    joint.save(result)

def join_vertical(png1, png2):
    img1, img2 = Image.open(png1), Image.open(png2)

    size1, size2 = img1.size, img2.size  # 获取两张图片的大小
    joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))

    loc1, loc2 = (0, 0), (0, size1[1])

    joint.paste(img2, loc2)
    joint.paste(img1, loc1)
    joint.save(result)

def start(items, first_path=None):
    # 当first为None时,默认将第一张图片设置为图片列表的第一张图片,第二张图片设置为图片列表的第二张
    # 当这两张图片合成后，将图片列表的已经合成的图片元素移除
    # 然后将合成的图片设置为第一张图片,将剩余的没有合成的图片列表继续操作
    # 当first_path不为None,将第一张图片设置为first_path，第二张图片设置为传进来的列表的第一个元素
    # 合成之后，将刚刚使用的列表的元素删除
    # 最后递归函数，知道列表为空
    try:
        if not first_path:
            path1, path2 = items[0], items[1]
            join_vertical(path1, path2)
            items.remove(path1)
            items.remove(path2)
            return start(items, first_path=result)
        else:
            path2 = items[0]
            join_vertical(first_path, path2)
            items.remove(path2)
            return start(items, first_path=result)
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

    path = 'img/'  # 图片文件夹路径

    result = 'img/result.png'  # 图片保存路径


    imgs = get_all_images(path)

    start(imgs)
    print('最后图片尺寸--->', Image.open(result).size)