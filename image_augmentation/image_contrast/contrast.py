import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
import os
import argparse
import numpy as np 
from tqdm import tqdm

# sample command: 
# python contrast.py -i C:\Users\daphn\Desktop\Data-Augmenting-For-Submerged-SLAM\image_augmentation\images -c 1.0 -r C:\Users\daphn\Desktop\Data-Augmenting-For-Submerged-SLAM\image_augmentation\contrast_images_rgb\ -b C:\Users\daphn\Desktop\Data-Augmenting-For-Submerged-SLAM\image_augmentation\contrast_images_bw\
# python3 contrast.py -i /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/temp_folder -c 1.0 -r /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/contrast_images_rgb/ -b /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/contrast_images_bw/

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

def save_rgb(rgb_dir, image_name, image):
    output_path_rgb = os.path.join(rgb_dir, image_name)
    plt.imsave(output_path_rgb, image) 

def save_bw(bw_dir, image_name, image):
    os.chdir(bw_dir)
    image.save(image_name)

print("Attempting to apply contrasts to images...")

for imgName in tqdm(os.listdir(imgDir), desc="Applying contrasts", colour="green"):
    imgPath = imgDir + '/' + imgName
    image = Image.open(imgPath)
    # Convert the image to a PyTorch tensor
    tensor_image = transforms.ToTensor()(image)

    # contrast_factor = 1.0
    adjusted_tensor_image = adjust_contrast(tensor_image, contrast_factor)  

    adjusted_image = transforms.ToPILImage()(adjusted_tensor_image)

    # NOTE: uncomment this to show rgb contrast image 
    # plt.imshow(adjusted_image)
    # plt.axis('off')  # Hide the axis
    # plt.show()  

    # save into rgb
    save_rgb(output_directory_rgb, imgName, adjusted_image)

    save_bw(output_directory_bw, imgName, adjusted_image)

print("Contrasted images in RGB and BW are saved succesfully!")