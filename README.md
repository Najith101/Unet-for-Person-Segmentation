# Unet-for-Person-Segmentation
## Objective

The project was created to do human segmentation in real time.

### Methods Used

* Machine Learning
* Deep Learning
* Transfer Learning

### Technologies Used

* Python
* Numpy/ jupyter/ Colab
* OpenCV
* Tensorflow

## Project Descrition

The [dataset](https://www.kaggle.com/dataset/b9d4e32be2f57c2901fc9c5cd5f6633be7075f4b32d73348a6d5db245f2c1934) for the project was taken from kaggle.
Data set consists of 5768 RGB images in a folder called images and masks for those images are given in a seperate folder. 
Here for the model we are using the UNet to perform the segmentation. It follows an encoder-decoder approach. During video feed the frame is preprocessed and is fed to the model diretly where we 
combine both the mask obtained with the frame and the output is displayed.

## Installation
All the installations required are given in the requirement.txt

## Usage
Step 1: Use the ipynb file to train and save the model.

Step 2: Use the py file to load the model and preprocess the frame and get the output.

Step 3: The py file will run the camera in the laptop(if its run on a laptop) and will show the result which can then be saved.


## Project status
The project is COMPLETED as all the requirements for this project is completed. For people who wants to add any new feature or attribute for this project, you may submit a request
to this project maintainers.
