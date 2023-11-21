import pygame
from MotorModule import Motor
import os
#import WebcamModule as wM
import cv2

cap = cv2.VideoCapture(0)
# Initialize Pygame
pygame.init()

# Initialize the motor instance
motor = Motor(2, 3, 4, 17, 22, 27)

# Create directories to save collected data for UP, RIGHT, and LEFT
if not os.path.exists('DataCollected/UP'):
    os.makedirs('DataCollected/UP')
if not os.path.exists('DataCollected/RIGHT'):
    os.makedirs('DataCollected/RIGHT')
if not os.path.exists('DataCollected/LEFT'):
    os.makedirs('DataCollected/LEFT')

def getKey():
    keyInput = pygame.key.get_pressed()
    
    if keyInput[pygame.K_UP]:
        return 'UP'
    elif keyInput[pygame.K_DOWN]:
        return 'DOWN'
    elif keyInput[pygame.K_LEFT]:
        return 'LEFT'
    elif keyInput[pygame.K_RIGHT]:
        return 'RIGHT'
    elif keyInput[pygame.K_r]:
        return 'R'
    else:
        return None
def init():
    win = pygame.display.set_mode((100, 100))

def main():
    key = getKey()
    _, img = cap.read()
    size=(480, 240)
    if key:
        print(f'Key {key} was pressed')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Quit Pygame when closing the window
    
    keyInput = pygame.key.get_pressed()
    
    if keyInput[pygame.K_UP]:
        motor.move(0.6, 0, 0.1)
    elif keyInput[pygame.K_DOWN]:
        motor.move(-0.6, 0, 0.1)
    elif keyInput[pygame.K_LEFT]:
        motor.move(0.5, -0.3, 0.1)
    elif keyInput[pygame.K_RIGHT]:
        motor.move(0.5, 0.3, 0.1)
    else:
        motor.stop(0.1)
    
    if key == 'UP':
        # Capture and save the image using the WebcamModule
        #img = wM.getImg(display=True, size=(480, 240))
        folder = 'UP'
        if img is not None and not img.size == 0:
            # Resize the image to the specified size
            img = cv2.resize(img, size)
            # Convert the image to grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            file_name = f'DataCollected/{folder}/img{counter[folder]}.png'
            cv2.imwrite(file_name, img)
            counter[folder] += 1
        else:
            print("Error: Unable to capture frame")
    elif key == 'RIGHT':
        # Capture and save the image using the WebcamModule
        #img = wM.getImg(display=True, size=(480, 240))
        folder = 'RIGHT'
        if img is not None and not img.size == 0:
            # Resize the image to the specified size
            img = cv2.resize(img, size)
            # Convert the image to grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            file_name = f'DataCollected/{folder}/img{counter[folder]}.png'
            cv2.imwrite(file_name, img)
            counter[folder] += 1
        else:
            print("Error: Unable to capture frame")
    elif key == 'LEFT':
        # Capture and save the image using the WebcamModule
        #img = wM.getImg(display=True, size=(480, 240))
        folder = 'LEFT'
        if img is not None and not img.size == 0:
            # Resize the image to the specified size
            img = cv2.resize(img, size)
            # Convert the image to grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            file_name = f'DataCollected/{folder}/img{counter[folder]}.png'
            cv2.imwrite(file_name, img)
            counter[folder] += 1
        else:
            print("Error: Unable to capture frame")
    elif key == '':
        cap.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    init()
    counter = {'UP': 0, 'RIGHT': 0, 'LEFT': 0}
    while True:
        main()
