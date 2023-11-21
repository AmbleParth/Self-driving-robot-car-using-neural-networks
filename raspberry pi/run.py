import cv2
import numpy as np
from tensorflow.keras.models import load_model
import picamera
import picamera.array
import MotorModule as mM

# Initialize the PiCamera
camera = picamera.PiCamera()
camera.resolution = (240, 120)  # Adjust the resolution as needed

#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.8  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 27)  # Pin Numbers
model = load_model('/home/parth/Desktop/Project/model.h5')
######################################

def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

while True:
    output = picamera.array.PiRGBArray(camera)
    camera.capture(output, format='bgr')
    img = output.array

    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    print(steering * steeringSen)
    motor.move(maxThrottle, -steering * steeringSen)
    cv2.waitKey(1)
