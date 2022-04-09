#Importing important libraries
import numpy as np
from numpy import asarray
import pandas as pd
from PIL import Image
import random as rng
import cv2
import os
import json
import sys

from util import denorm_and_bound, polygon, bb

#Taking input data
if(len(sys.argv) == 3):
    image_path  = sys.argv[1]
    meta_data_json_path = sys.argv[2]
    opacity = 0.2
elif(len(sys.argv) == 4):
    image_path  = sys.argv[1]
    meta_data_json_path = sys.argv[2]
    opacity = int(float(sys.argv[3]))

else:
    print('INCORRECT INPUT\n Default Code Running...')
    image_path = 'Assignment/Data Visualization/images/3.jpg'
    meta_data_json_path = 'Assignment/Data Visualization/data/3.json'
    opacity = 0.2

try:
    with open(meta_data_json_path) as f:
        data = json.load(f)
except:
    print("DATA FILE NOT FOUND.")

try:
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
except:
    print("IMAGE FILE NOT FOUND.")

denorm_and_bound(image_path, data)

polygon(image_path, data, opacity)

bb(image_path, data)
