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


 
def lowlight(image_path):
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

	image_path = image_path.replace('test_data','result')
	result_path = image_path
	if not os.path.exists(image_path.replace('/'+image_path.split("/")[-1],'')):
		os.makedirs(image_path.replace('/'+image_path.split("/")[-1],''))

	torchvision.utils.save_image(enhanced_image, result_path)

if __name__ == '__main__':
# test_images
	with torch.no_grad():
		filePath = 'data/test_data/'
	
		file_list = os.listdir(filePath)

		print("Attempting to apply brightness to images through Zero DCE...")


		for file_name in file_list:
			test_list = glob.glob(filePath+file_name+"/*") 
			for image in tqdm(test_list, desc="Adjusting brightness", colour="green"):
				lowlight(image)
		
		print("Brightness images are saved succesfully!")

		

