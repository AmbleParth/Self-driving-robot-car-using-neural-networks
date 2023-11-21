import pygame
from gpiozero import Robot

robot = Robot(left=(2,3, 4), right=(17, 22, 27))
pygame.init()

done = False
movement_active = False  # Flag to track if movement keys are pressed

try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                movement_active = True  # A key is pressed, enable movement
                if event.key == pygame.K_w:
                    robot.backward()
                    print("Moving forward")
                if event.key == pygame.K_s:
                    robot.forward()
                    print("Moving backward")
                if event.key == pygame.K_a:
                    robot.right()
                    print("Turning left")
                if event.key == pygame.K_d:
                    robot.left()
                    print("Turning right")
                if event.key == pygame.K_x:
                    robot.stop()
                    print("Stopping")

            elif event.type == pygame.KEYUP:
                movement_active = False  # No key is pressed, disable movement
                robot.stop()  # Stop the robot when no keys are pressed
                print("Stopped")

        if not movement_active:
            robot.stop()  # Stop the robot if no movement keys are active

except KeyboardInterrupt:
    pass
finally:
    pygame.quit()

