import torch
import torch.nn as nn
import torchvision
import torch.backends.cudnn as cudnn
import torch.optim
import os
import sys
import argparse
import time
import dataloader
import model
import numpy as np
from torchvision import transforms
from PIL import Image
import glob
import time
from tqdm import tqdm

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imgDir", required=True,
	help="path to image folder to be analyzed")
ap.add_argument("-o", "--output", required=True,
	help="output folder name")

args = vars(ap.parse_args())

imgDir=args["imgDir"]
output_directory = args["output"]

os.makedirs(output_directory, exist_ok=True)


 
def infer(image_path):
	os.environ['CUDA_VISIBLE_DEVICES']='0'
	data_lowlight = Image.open(image_path)

	data_lowlight = (np.asarray(data_lowlight)/255.0)

	data_lowlight = torch.from_numpy(data_lowlight).float()

	# Add a conditional to handle grayscale images by adding a channel dimension
	if data_lowlight.ndim == 2:
        # Adds a channel dimension
		data_lowlight = data_lowlight.unsqueeze(0)
	else:
		data_lowlight = data_lowlight.permute(2,0,1)
	
	# If the image is grayscale (now has 1 channel after unsqueeze), repeat the channel 3 times
	if data_lowlight.size(0) == 1:  # Checking the channel dimension
		data_lowlight = data_lowlight.repeat(3, 1, 1)
	
	data_lowlight = data_lowlight.cuda().unsqueeze(0)

	DCE_net = model.enhance_net_nopool().cuda()
	DCE_net.load_state_dict(torch.load('snapshots/Epoch99.pth'))
	_,enhanced_image,_ = DCE_net(data_lowlight)

	return enhanced_image


with torch.no_grad():
	print("Attempting to apply brightness to images through Zero DCE...")
 
	for image in tqdm(os.listdir(imgDir), desc="Adjusting brightness", colour="green"):
		img = infer(image)
		torchvision.utils.save_image(img, output_directory)
		
	print("Brightness images are saved succesfully!")

		

