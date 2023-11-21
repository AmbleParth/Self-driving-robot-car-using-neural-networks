import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import picamera
import picamera.array
import MotorModule as mM

# Initialize the PiCamera
camera = picamera.PiCamera()
camera.resolution = (240, 120)  # Adjust the resolution as needed

#######################################
steeringSen = 0.82  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 27)  # Pin Numbers
interpreter = tflite.Interpreter(model_path='/home/parth/Desktop/Project/model1.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
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
    img = np.array([img], dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    steering = interpreter.get_tensor(output_details[0]['index'])[0][0]
    print(steering * steeringSen)
    motor.move(maxThrottle, -steering * steeringSen)
    cv2.waitKey(1)

