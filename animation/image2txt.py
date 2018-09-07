#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy
def image_to_txt(image_path, txt_path):
    txt_count = 1
    fileList = os.listdir(image_path)
    for file in fileList:
        img = Image.open(image_path + '\\'+ file).convert('L')
        charWidth = 140
        img = img.resize((charWidth, 40))
        target_width, target_height = img.size
        data = numpy.array(img)[:target_height, :target_width]
        # 使用numpy库，将图像转化为数组
        with open(txt_path + '\\' + str(txt_count) + '.txt', 'w') as f:
            txt_count += 1
            for row in data:
                for pixel in row:
                    if pixel < 127:
                        f.write('*')
                    else:
                        f.write(' ')
                f.write('\n')