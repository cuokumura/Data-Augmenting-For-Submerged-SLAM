import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
import os
import argparse
import numpy as np 
from tqdm import tqdm

# Daphne Tsai (dvtsai@umich.edu)
# EECS 568: Mobile Robotics, Winter 2024 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imgDir", required=True,
	help="path to image folder to be analyzed")
ap.add_argument("-c", "--imgContrast", type=float, required=True,
	help="contrast factor to apply to image")
ap.add_argument("-r", "--rgbPath", required=True,
	help="path to rgb contrast output")
ap.add_argument("-b", "--bwPath", required=True,
	help="path to bw contrast output")
args = vars(ap.parse_args())

imgDir=args["imgDir"]
contrast_factor = args["imgContrast"]
output_directory_rgb = args["rgbPath"]
output_directory_bw = args["bwPath"]

os.makedirs(output_directory_rgb, exist_ok=True)
os.makedirs(output_directory_bw, exist_ok=True)

# Define the function to adjust contrast and apply it
def adjust_contrast(input_image, contrast_factor):
    return transforms.functional.adjust_contrast(input_image, contrast_factor)

# Save RGB contrasted images 
def save_rgb(rgb_dir, image_name, image):
    output_path_rgb = os.path.join(rgb_dir, image_name)
    plt.imsave(output_path_rgb, image) 

# Save grayscale contrasted images
def save_bw(bw_dir, image_name, image):
    os.chdir(bw_dir)
    image.save(image_name)

print("Attempting to apply contrasts to images...")

for imgName in tqdm(os.listdir(imgDir), desc="Applying contrasts", colour="green"):
    imgPath = imgDir + '/' + imgName
    image = Image.open(imgPath)
    # Convert the image to a PyTorch tensor
    tensor_image = transforms.ToTensor()(image)

    adjusted_tensor_image = adjust_contrast(tensor_image, contrast_factor)  

    adjusted_image = transforms.ToPILImage()(adjusted_tensor_image)

    # NOTE: uncomment this to show contrasted image on screen. You can use this if you 
    # want to make sure the contrast is being applied correctly to the images.
    # plt.imshow(adjusted_image)
    # plt.axis('off')
    # plt.show()  

    # Save images into directory 
    save_rgb(output_directory_rgb, imgName, adjusted_image)

    save_bw(output_directory_bw, imgName, adjusted_image)

print("Contrasted images in RGB and BW are saved succesfully!")