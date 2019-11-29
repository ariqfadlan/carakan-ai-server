#!/usr/bin/env python
import cv2
import numpy as np

from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array

class Gambar:
    def __init__(self, img_path):
        self.arr_img = np.empty((32,32,1), dtype=np.float32)
        self.img_path = img_path

    def resize(self):
        size = 32
        color = [0,0,0]

        #img = cv2.imread(self.img_path)
        npimg = np.fromstring(self.img_path, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        _, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

        kernel = np.ones((3,3), np.uint8)

        dila = cv2.dilate(thresh, kernel, iterations=3)
        cntrs, _ = cv2.findContours(dila.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        areas = [cv2.contourArea(c) for c in cntrs]
        max_index = np.argmax(areas)
        cntr=cntrs[max_index]

        x,y,w,h = cv2.boundingRect(cntr)

        region = thresh[y:y+h, x:x+w]

        cv2.rectangle(img,(x,y),( x + w, y + h ),(0,255,0),2)

        old_size = region.shape[:2]
        ratio = float(size)/max(old_size)
        final_size = tuple([int(k*ratio) for k in old_size])
        new_img = cv2.resize(region, (final_size[1], final_size[0]))
        delta_w = size - final_size[1]
        delta_h = size - final_size[0]

        t, b = delta_h//2, delta_h-(delta_h//2)
        l, r = delta_w//2, delta_w-(delta_w//2)

        resized_img = cv2.copyMakeBorder(new_img, t, b, l, r, cv2.BORDER_CONSTANT,
            value=color)
        #final_image = resized_image[...,::-1].astype(np.float32)

        return resized_img

    def load(self):
        pict = self.resize()
        pil_img = Image.fromarray(pict)
        self.arr_img = img_to_array(pil_img)

    def shape(self):
        return self.arr_img.reshape(1,32,32,1)
