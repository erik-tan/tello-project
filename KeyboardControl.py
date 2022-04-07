import cv2
from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()


def getKeyboardInput():
    lr, fb, us, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = -speed
    elif kp.getKey("DOWN"): fb = speed

    if kp.getKey("w"): us = -speed
    elif kp.getKey("s"): us = speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("9"): drone.takeoff()
    if kp.getKey("0"): drone.land()

    return [lr, fb, us, yv]
    

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360,240))

    cv2.imshow("Image",img)
    cv2.waitKey(1)