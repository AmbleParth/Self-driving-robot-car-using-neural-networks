import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

# GET CURRENT DIRECTORY PATH
myDirectory = os.path.join(os.getcwd(), 'DataCollected')
print(myDirectory)

# CREATE A NEW FOLDER BASED ON THE PREVIOUS FOLDER COUNT
while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')):
    countFolder += 1
newPath = myDirectory + "/IMG" + str(countFolder)
os.makedirs(newPath)

# SAVE IMAGES IN THE FOLDER
def captureImage(camera, display=False):
    timestamp = str(int(datetime.timestamp(datetime.now())))
    fileName = os.path.join(newPath, f'Image_{timestamp}.jpg')
    camera.capture(fileName)
    if display:
        img = cv2.imread(fileName)
        #cv2.imshow("Image", img)
    return fileName

def saveData(img, steering):
    global imgList, steeringList
    imgList.append(img)
    steeringList.append(steering)

# SAVE LOG FILE WHEN THE SESSION ENDS
def saveLog():
    global imgList, steeringList
    rawData = {'Image': imgList, 'Steering': steeringList}
    df = pd.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory, f'log_{str(countFolder)}.csv'), index=False, header=False)
    print('Log Saved')
    print('Total Images: ', len(imgList))
