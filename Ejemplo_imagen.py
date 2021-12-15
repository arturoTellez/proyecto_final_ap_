# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:14:07 2021

@author: jorge
"""
from PIL import Image
import matplotlib.pyplot as plt
im1 = Image.open('D:/jorge/Documents/ISPRS/Potsdam/1_DSM/dsm_potsdam_02_10.tif')

width = 2560
height = 2560

im2 = im1.resize((width, height), Image.NEAREST)      
im3 = im1.resize((width, height), Image.BILINEAR)     
im4 = im1.resize((width, height), Image.BICUBIC)      
im5 = im1.resize((width, height), Image.ANTIALIAS)

plt.imshow(im1)