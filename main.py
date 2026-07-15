from src.chassis import ChassisController as Chassis
import time
import robomaster
from robomaster import robot
import csv
import os


    



ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")

chassis = Chassis(ep_robot)
start_time = time.time()



v = 0.7
degree = 91
chassis.move_forward(0.6, v)
time.sleep(2)
chassis.move_turnRight(degree, 1)
time.sleep(1)


chassis.move_forward(0.6, v)
time.sleep(2)
chassis.move_turnRight(degree, 1)
time.sleep(1)

chassis.move_forward(0.6, v)
time.sleep(2)
chassis.move_turnRight(degree, 1)
time.sleep(1)

chassis.move_forward(0.6, v)
time.sleep(2)
chassis.move_turnRight(degree, 1)



ep_robot.close()
