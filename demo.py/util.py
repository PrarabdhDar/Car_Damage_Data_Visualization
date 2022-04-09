import numpy as np
from numpy import asarray
import pandas as pd
from PIL import Image
import random as rng
import cv2
import os
import json
import sys


pts = list()
start = list()
end = list()
label = list()
top = list()
bottom = list()
output = list()

def denorm_and_bound(image_path, data):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    for d in data:
        if(d['type'] == 'polygonlabels'):
            x_min = sys.maxsize
            y_max = -sys.maxsize + 1
            x_max = -sys.maxsize + 1
            y_min = sys.maxsize

            label.append(d['value']['polygonlabels'][0])

            curr_pts = np.array(d['value']['points'])
            for c in curr_pts:
                c[0] = int((c[0]*width)/100)
                c[1] = int((c[1]*height)/100)

                x_min = min(c[0], x_min)
                y_max = max(c[1], y_max)
                x_max = max(c[0], x_max)
                y_min = min(c[1], y_min)

            pts.append(curr_pts)
            start.append((int(x_min), int(y_max)))
            end.append((int(x_max), int(y_min)))
            top.append((int(x_min), int(y_min)))


def polygon(image_path, data, opacity):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))

    overlay = image.copy()

    for p in pts:
        image = cv2.polylines(image, np.int32([p]),
                            True, color, 3)
        cv2.fillPoly(overlay, np.int32([p]), color)
        poly_image = cv2.addWeighted(overlay, opacity, image, 1-opacity, 0)

        window_name = 'image'
    output.append(poly_image)

#Second Image Visualization function
def bb(image_path, data):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    i=0

    for p in pts:

        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.rectangle(image, start[i], end[i], color, 2)
        bottom.append((top[i][0] + 10*len(label[i]), top[i][1]))
        cv2.rectangle(image, (top[i][0], top[i][1] - 15), bottom[i], (0,0,0), -1)
        cv2.putText(image, label[i], top[i], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        i = i + 1

    window_name = 'image'
    output.append(image)
    return output
