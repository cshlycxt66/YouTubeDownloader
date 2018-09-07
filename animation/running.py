#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from animation import image2txt
from animation import video2image
def run(txt_path):
    fileList = os.listdir(txt_path)
    for i in range(1, len(fileList)+1):
        try:
            os.system('type ' + txt_path + '\\' + str(i) + '.txt')
            os.system('cls')
        except:
            print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def start():
        #video_path = r'C:\Users\Hitsme\Desktop\ezgif-4-01a7a321ae.mp4'
        image_path = r'G:\pycharmWorkspace\WeChatPublicPlatform_Spider\animation\image'
        txt_path = r'G:\pycharmWorkspace\WeChatPublicPlatform_Spider\animation\txt'
        #video2image.get_image(video_path, image_path)
        image2txt.image_to_txt(image_path, txt_path)
        run(txt_path)