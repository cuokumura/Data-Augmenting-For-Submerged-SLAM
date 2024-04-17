# Zero-DCE 
This adjusts the contrast of an image using the Zero-DCE model. Starter code for brightness.py has been pulled from the official [repo](https://github.com/Li-Chongyi/Zero-DCE)

## Work Done
- Modified code to accept grayscale images. AQUALOC images are grayscale but Zero-DCE was set up to take RGB images as input.
- Added argument parser to accept command line arguments to reduce copies of the AQUALOC dataset.
- Added a progress bar. 

## Notes
- There is commented out code that if uncommented, will display the brightened image on the screen for the user. 