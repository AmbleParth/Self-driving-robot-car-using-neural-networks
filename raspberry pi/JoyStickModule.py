"""
-This module get the joystick values
and puts them in a single dictionary in realtime.
-The values can be accessed through the keys
-Tested on PS4 Bluetooth and wired controller
"""

import pygame
from time import sleep

pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()
buttons = {'A': 0, 'B': 0, 'X': 0, 'Y': 0,
           'LB': 0, 'RB': 0, 'LT': 0, 'RT': 0,
           'Back': 0, 'Start': 0,
           'LS_X': 0., 'LS_Y': 0., 'RS_X': 0., 'RS_Y': 0.}

axiss = [0., 0., 0., 0., 0., 0.]


def getJS(name=''):
    global buttons
    # retrieve any events ...
    for event in pygame.event.get():  # Analog Sticks
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value, 2)
        elif event.type == pygame.JOYBUTTONDOWN:  # When button pressed
            # print(event.dict, event.joy, event.button, 'PRESSED')
            for x, (key, val) in enumerate(buttons.items()):
                if x < 10:
                    if controller.get_button(x): buttons[key] = 1
        elif event.type == pygame.JOYBUTTONUP:  # When button released
            # print(event.dict, event.joy, event.button, 'released')
            for x, (key, val) in enumerate(buttons.items()):
                if x < 10:
                    if event.button == x: buttons[key] = 0

    # to remove element 2 since axis numbers are 0 1 3 4
    buttons['axis1'], buttons['axis2'], buttons['axis3'], buttons['axis4'] = [axiss[0], axiss[1], axiss[3], axiss[4]]
    if name == '':
        return buttons
    else:
        return buttons[name]


def main():
    # print(getJS()) # To get all values
    # sleep(0.05)
    a_button_status = getJS('A')  # Access the A button status
    print("A Button Status:", a_button_status)
  # To get a single value
    sleep(0.05)


if __name__ == '__main__':
    while True:
        main()
