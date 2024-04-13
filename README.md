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

## ORB-SLAM 3

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

### Brightness
We will use two different deep learning models for brightness enhancement. The directions are as follows:

#### EnlightenGAN
##### Step 1: Activate the Conda environment
- Please see the instructions above.
#### Step 2: Install the EnlightenGAN inference wrapper [repository](https://github.com/arsenyinfo/EnlightenGAN-inference)
```
pip3 install git+https://github.com/arsenyinfo/EnlightenGAN-inference
```

#### Zero-DCE
