# EnlightenGAN 
This adjusts the contrast of an image using the EnlightenGAN model. Starter code for brightness.py has been pulled from the official [repo](https://github.com/VITA-Group/EnlightenGAN/tree/master)

## Work Done
- Modified code to customize the model's execution provider. It is recommended to run inference on a GPU. If your system doesn't have a compatible version of onnxruntime, please switch the model to the CPU.
- Added argument parser to accept command line arguments.
- Added a progress bar. 

## Notes
- There is commented out code that if uncommented, will display the brightened image on the screen for the user. 