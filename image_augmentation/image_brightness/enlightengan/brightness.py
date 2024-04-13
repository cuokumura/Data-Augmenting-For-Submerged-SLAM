from enlighten_inference import EnlightenOnnxModel
import cv2
# import torch
# import torchvision.transforms as transforms
# from PIL import Image
# import matplotlib.pyplot as plt
import os
import argparse
import numpy as np 
from tqdm import tqdm

# sample command: 
# python3 brightness.py -i /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/temp_folder -o /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/brightness_images

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imgDir", required=True,
	help="path to image folder to be analyzed")
ap.add_argument("-o", "--output", required=True,
	help="output folder name")

args = vars(ap.parse_args())

imgDir=args["imgDir"]
output_directory = args["output"]

os.makedirs(output_directory, exist_ok=True)

# by default, CUDAExecutionProvider is used
# model = EnlightenOnnxModel()
# however, one can choose the providers priority, e.g.: 
# this would probably be faster on CUDA but versions are ....
model = EnlightenOnnxModel(providers = ["CPUExecutionProvider"])

print("Attempting to apply brightness to images...")

for imgName in tqdm(os.listdir(imgDir), desc="Adjusting brightness", colour="green"):
    # changed to / for Linux. On windows, use \\
    imgPath = imgDir + '/' + imgName
    img = cv2.imread(imgPath)

    processed = model.predict(img)

    # NOTE: uncomment this to display the images

    # # Display the original image
    # cv2.imshow('Original Image', img)

    # # Display the processed image
    # cv2.imshow('Processed Image', processed)

    # # Wait for any key to be pressed before closing
    # cv2.waitKey(0)

    # # Destroy all the windows created by OpenCV
    # cv2.destroyAllWindows()

    os.chdir(output_directory)
    cv2.imwrite(imgName, processed)

print("Brightness images are saved succesfully!")