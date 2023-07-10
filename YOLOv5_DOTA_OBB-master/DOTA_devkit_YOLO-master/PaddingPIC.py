import cv2
import numpy as np
from numpy.lib.arraypad import pad
import os
for filepath,dirnames,filenames in os.walk('DOTA_demo/images'):
     for filename in filenames:
        img=cv2.imread(os.path.join(filepath,filename))
        (h,w,c)=img.shape
        max_w_h=max(h,w)

        pad_pic=np.zeros((max_w_h,max_w_h,c), np.uint8)
        pad_pic[0:h,0:w]=img
        
        cv2.imwrite(os.path.join(filepath,filename),pad_pic)

print('finished')