# Data Augmentation to Improve Underwater SLAM Performance

## Overview 
This repository contains our code for our final project for EECS 568: Mobile Robotics during the Winter 2024 Semester at the University of Michigan. Our team is made up of:
* Christopher Okumura (cokumura@umich.edu): ECE Master's (Specialization: Robotics).
* Tiffany Parise (tparise@umich.edu): ECE Master's (Specialization: Computer Vision).
* Daphne Tsai (dvtsai@umich.edu): CSE Master's student.

## Relevant Links
* Paper
* Video
* Presentation
* Poster

## Download the AQUALOC Datset
The AQUALOC dataset can be found [here](https://www.lirmm.fr/aqualoc/). Please download the appropiate files.

## Data Augmentation 
We will perform two data augmentations on the AQUALOC dataset: contrast and brightness. Below are the directions to perform the augmentations. It is recommended to set up a virtual environment for each of these tasks, such as Conda. Please see the Conda [documentation](https://docs.conda.io/en/latest/) for more information. Create a Conda environment as follows:
```
conda create -n <new_name>
conda activate <new_name>
```
where <new_name> is the name of your Conda environment. Remember to exit the environment after you are done as follows:
```
conda deactivate <new_name>
```

### Contrast
Please see the code for contrast.py. You will need to speficy the command line arguments as follows:
- --imgDir: path to the image folder that contrast adjustment will be performed on.
- --imgContrast: the contrast factor to be applied to the images in --imgDir.
- --rgbPath: the path to the directory to store the RGB contrasted images.
- --bwPath: the path to the directory to store the grayscale contrasted images. 

### Brightness
We will use two different deep learning models for brightness enhancement. The directions are as follows:

#### EnlightenGAN
The original work of EnlightenGAN can be found [here](https://github.com/VITA-Group/EnlightenGAN).
##### Step 1: Activate the Conda environment
- Please see the instructions above.
##### Step 2: Install the EnlightenGAN inference wrapper [repository](https://github.com/arsenyinfo/EnlightenGAN-inference)
```
pip3 install git+https://github.com/arsenyinfo/EnlightenGAN-inference
```
##### Step 3: Run EnlightenGAN on AQUALOC
To run EnlightenGAN, please see the code for brightness.py. You will need to specify command line arguments as follows:
- --imgDir: path to the image folder that EnlightenGAN will be run on.
- --output: name of the output folder where EnlightenGAN will store results. 
An example command looks like:
```
python3 brightness.py -i /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/temp_folder -o /home/daphne/Data-Augmenting-For-Submerged-SLAM/image_augmentation/brightness_images
```
**Note:** You will need onnxruntime to use the EnlightenGAN inference wrapper, which relies on the use of CUDA. If you want to switch to the CPU, make sure to specify this as the execution provider in brightness.py:
```
model = EnlightenOnnxModel(providers = ["CPUExecutionProvider"])
```
If you leave the providers blank, the model will default to CUDA. 

#### Zero-DCE
The original work of Zero-DCE can be found [here](https://github.com/Li-Chongyi/Zero-DCE). 
##### Step 1: Activate the Conda environment
There are different dependencies needed between EnlightenGAN and Zero-DCE. Therefore, it is recommended to have different environments for the two models to avoid any dependency conflicts. Please see the instructions above. 
##### Step 2: Clone the Zero-DCE [repository](https://github.com/Li-Chongyi/Zero-DCE)
```
git clone https://github.com/Li-Chongyi/Zero-DCE.git
```
##### Step 3: Run Zero-DCE on AQUALOC 
To run Zero-DCE, please see the code for lowlight_test.py within the Zero-DCE_code folder. An example command looks like:
```
python3 lowlight_test.py
```
**Note:** Zero-DCE was developed for RGB images. However, the images in the AQUALOC dataset are grayscale. Therefore, we modified the Zero-DCE code to take in grayscale images. 

## ORB-SLAM 3


