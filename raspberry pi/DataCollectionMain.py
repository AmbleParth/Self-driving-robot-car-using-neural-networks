import DataCollectionModule as dcM
import JoyStickModule as jsM
import MotorModule as mM
import picamera
import cv2
from time import sleep

maxThrottle = 0.3
motor = mM.Motor(2, 3, 4, 17, 22, 27)

record = 0

# Initialize the PiCamera
camera = picamera.PiCamera()
camera.resolution = (480, 240)

while True:
    joyVal = jsM.getJS()
    steering = joyVal['axis1'] 
    throttle = joyVal['A'] * maxThrottle
    if joyVal['Y'] == 1:
        if record == 0:
            print('Recording Started ...')
        record += 1
        sleep(0.300)
    if record == 1:
        img = dcM.captureImage(camera, True)
        dcM.saveData(img, steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle, steering)
    cv2.waitKey(1)
'''
import WebcamModule as wM
import DataCollectionModule as dcM
import JoyStickModule as jsM
import MotorModule as mM
import cv2
from time import sleep

maxThrottle = 0.25
motor = mM.Motor(2, 3, 4, 17, 22, 27)

record = 0
while True:
    # Check for key events
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed, break from the loop
    if key == ord('q'):
        break

    # Update steering based on arrow keys
    if key == ord('a'):
        steering = -1.0  # Turn left
    elif key == ord('d'):
        steering = 1.0   # Turn right
    else:
        steering = 0.0   # No steering input

    # Throttle control using 'w' and 's' keys
    throttle = 0.0
    if key == ord('w'):
        throttle = maxThrottle
    elif key == ord('s'):
        throttle = -maxThrottle

    if key == ord(' '):  # Space key to start/stop recording
        if record == 0:
            print('Recording Started ...')
        record += 1
        sleep(0.300)

    if record == 1:
        img = wM.getImg(True, size=[240, 120])
        dcM.saveData(img, steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle, -steering)

cv2.destroyAllWindows()

'''