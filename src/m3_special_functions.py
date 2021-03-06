# Final Project Code
# Author: Alex Hinojosa
# Date: February 20th, 2019

import time
import rosebot


def dance(robot):
    robot = rosebot.RoseBot()
    robot.drive_system.left_motor.reset_position()
    while True:
        robot.drive_system.go(50, 100)
        if robot.drive_system.left_motor.get_position() >= 1000:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(100, -100)
    time.sleep(1.5)
    robot.drive_system.go(-100, 100)
    time.sleep(1.5)
    robot.drive_system.stop()


def find_enemy(robot):
    robot = rosebot.RoseBot()
    lws = 50
    rws = 50
    robot.drive_system.go(lws, rws)
    area = 500
    while True:
        b = robot.sensor_system.camera.get_biggest_blob()
        print(b)
        blobarea = b.get_area()
        print(blobarea)
        if blobarea >= area:
            break
    robot.drive_system.stop()
    robot.sound_system.speech_maker.speak('Enemy Spotted on my Location. Executing Order 66')
    time.sleep(5)
    attack()


def you_win(robot):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go(100, -100)
    time.sleep(5)
    robot.drive_system.stop()
    robot.sound_system.speech_maker.speak('Congratulations, lets do it again!')


def you_lost(robot):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()
    time.sleep(2)
    robot.drive_system.go(100, -100)
    time.sleep(0.5)
    robot.drive_system.go(-100, 100)
    time.sleep(0.5)
    robot.drive_system.stop()
    robot.sound_system.speech_maker.speak('Mission Failed, Well get them next time')


def attack():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()
    time.sleep(1)
    robot.drive_system.go(100, 100)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.stop()
