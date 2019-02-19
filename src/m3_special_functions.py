import time
import rosebot


def dance(robot):
    robot = rosebot.RoseBot()
    robot.drive_system.left_motor.reset_position()
    while True:
        robot.drive_system.go(50, 100)
        if robot.drive_system.left_motor.get_position() >= robot.drive_system.wheel_circumference:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.calibrate_arm()


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
    robot.sound_system.speech_maker.speak('Enemy Spotted on my Location')


def you_won(robot):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speech_maker.speak('Congratulations, lets do it again!')


def you_lost(robot):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()
    robot.sound_system.speech_maker.speak('Mission Failed, We will get them next time')
