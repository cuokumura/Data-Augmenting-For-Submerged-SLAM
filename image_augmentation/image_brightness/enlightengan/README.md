# EnlightenGAN 
This adjusts the contrast of an image using the EnlightenGAN model. You can read more about the model at the official [repo](https://github.com/VITA-Group/EnlightenGAN/tree/master). Please make sure you have all of the requirements and dependencies installed.

## Description 
- Code can customize the model's execution provider. It is recommended to run inference on a GPU. If your system doesn't have a compatible version of onnxruntime, please switch the model to the CPU. Please check the official onnxruntime documentation [here](https://onnxruntime.ai/) to read more about compatability. 
- Argument parser to accept command line arguments. Please look at the main README and/or code to see what arguments are required.
- Progress bar. 

## Notes
- There is commented out code that if uncommented, will display the brightened image on the screen for the user. 