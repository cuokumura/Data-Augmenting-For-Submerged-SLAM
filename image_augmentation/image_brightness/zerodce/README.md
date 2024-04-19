# Zero-DCE 
This adjusts the contrast of an image using the Zero-DCE model. You can read more about the model at the official [repo](https://github.com/Li-Chongyi/Zero-DCE). Please make sure you have all of the requirements and dependencies installed.

## Description
- Code now accepts grayscale images. AQUALOC images are grayscale but Zero-DCE was set up to take RGB images as input.
- Argument parser to accept command line arguments to reduce copies of the AQUALOC dataset. Please look at the main README and/or code to see what arguments are required.
- Progress bar. 

## Notes
- There is commented out code that if uncommented, will display the brightened image on the screen for the user. 