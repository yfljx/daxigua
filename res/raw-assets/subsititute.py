# -*- encoding: utf-8 -*-
# @Author：lijinxi
# @Time ：2021/1/31 15:57
# @File：substitute.py
import os

from PIL import Image

_map = {
    'ad': 52,
    '0c': 80,
    'd0': 108,
    '74': 119,
    '13': 153,
    '03': 183,
    '66': 193,
    '84': 258,
    '5f': 308,
    '56': 308,
    '50': 408,
}

imgs=[]
for img in os.listdir('imgs'):
    imgs.append(os.path.join('imgs',img))
print(len(imgs))
print(imgs)

i=0
for key in _map.keys():
    os.makedirs(os.path.join('imgs',key))
    img=Image.open(imgs[i])
    w,h=img.size
    print(img.size)
    if h<w:
        img=img.crop(((w-h)//2,0,w-(w-h)//2,h))
    else:
        img=img.crop((0,(h-w)//2,w,h-(h-w)//2))
    imms=[]
    i+=1
    for _i in os.listdir(key):
        imms.append(_i)
    img=img.resize((_map[key],_map[key]))
    img.save(os.path.join('imgs',key,imms[0]))
