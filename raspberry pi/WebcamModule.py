import cv2
import os

# Redirect OpenCV error messages to a null device to suppress warnings
os.environ['OPENCV_LOG_PATH'] = '/dev/null'

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Create a directory to save the collected data if it doesn't exist
if not os.path.exists('DataCollected'):
    os.makedirs('DataCollected')

def getImg(display=False, size=(480, 240), counter=[0]):
    _, img = cap.read()

    # Check if the captured frame is valid (not empty)
    if img is not None and not img.size == 0:
        # Resize the image to the specified size
        img = cv2.resize(img, size)
        # Convert the image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if display:
            cv2.imshow('IMG', img)

        # Save the captured image with an increasing file name
        file_name = f'DataCollected/img{counter[0]}.png'
        cv2.imwrite(file_name, img)
        counter[0] += 1
    else:
        print("Error: Unable to capture frame")

if __name__ == '__main__':
    counter = [0]  # Initialize the counter
    while True:
        getImg(True, counter=counter)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close all OpenCV windows properly
cap.release()
cv2.destroyAllWindows()
