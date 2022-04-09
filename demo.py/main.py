#Importing important libraries
import numpy as np
from np import asarray
import pandas as pd
from PIL import Image
import random as rng
from google.colab.patches import cv2_imshow
import cv2
import os
import json
import sys

from util import polygon, bb

#Taking input data
if(len(sys.argv) == 0):
    image_path = 'Assignment/Data Visualization/images/3.jpg'
    meta_data_json_path = 'Assignment/Data Visualization/data/3.json'
    opacity = 0.2
elif(len(sys.argv) == 2):
    image_path  = sys.argv[1]
    meta_data_json_path = sys.argv[2]
    opacity = 0.2
elif(len(sys.argv) == 3):
    image_path  = sys.argv[1]
    meta_data_json_path = sys.argv[2]
    opacity = sys.argv[3]
else:
    print("INCORRECT NUMBER OF ARGUMENTS PASSED.\nEXITING NOW...")
    exit()

try:
    with open(meta_data_json_path) as f:
        data = json.load(f)
except:
    print("DATA FILE NOT FOUND.")

try:
    image =  image = cv2.imread(image_path)
except:
    print("IMAGE FILE NOT FOUND.")


pts = list()
start = list()
end = list()
label = list()
top = list()
bottom = list()

num = 0

for d in data:
    if(d['type'] == 'polygonlabels'):
        num = num + 1

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


polygon(image_path, data)

bb(image_path, data)
