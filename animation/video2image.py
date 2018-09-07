#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy

frame = 10
def get_image(video_path, image_path):
    try:
        os.system('ffmpeg -i  {0} -r {1} -f image2 {2}\%05d.png'.format(video_path, frame, image_path))
    except:
        print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')