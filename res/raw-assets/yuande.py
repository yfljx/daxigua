# -*- encoding: utf-8 -*-
# @Author：lijinxi
# @Time ：2021/1/31 16:54
# @File：yuande.py
import os

from PIL import Image, ImageDraw, ImageFilter

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)
    return result

files=[]
for i in os.listdir('imgs'):
    if os.path.isdir(i):
        files.append(os.path.join('imgs',i))
for file in files:
    for i in os.listdir(file):
        f=os.path.join(file,i)


        markImg = Image.open(f)
        thumb_width = markImg.size[0]

        im_square = crop_max_square(markImg).resize((thumb_width, thumb_width), Image.LANCZOS)
        im_thumb = mask_circle_transparent(im_square, 0)
        im_thumb.save(f)