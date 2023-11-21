# Self-driving-robot-car-using-neural-networks

Final year project

Requirements for this project :

Hardware --> Raspberry pi-4, L298n motor driver, 4wd car chasis, DC motors, jumper cables, switch, xbox/ ps4 controller, raspberry pi camera module.

Software --> python 3.5 or any version above 3.5, libraries numpy , tensorlfow, picamera, pygame.


How to execute

 (1)Run the code file DataCollectionMain.py on raspberry pi via SSH on cmd and collect data using a controller or keyboard(both codes provided).
 
 (2)For sample 10 images will be saved. The images are saved in timestamp.jpg format and a corresponding log file is saved which has steering angle associated with 
  each image.
  
 (3)After sufficient data is collected transfer the data to computer using scp command.
 
 (4)Run the file train.py , the model will take some time to get train and post completion a model.h5 file will be saved. If you are not able to install tensorflow 
 on your raspberry pi then I have added a code to convert model.h5 to tensorflow lite format.
 
 (5)Run the file run.py on raspberry pi and model will start giving predictions.
 
 (6)Test the predictions on pre trained track.

![lateral](https://github.com/AmbleParth/Self-driving-robot-car-using-neural-networks/assets/94055399/0f4bb285-a1af-4120-9947-b5349719769f) 
Robot



