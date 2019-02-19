import time


def dance(robot):
    robot.drive_system.go(50, 100)
    robot.arm_and_claw.raise_arm().wait()
    robot.arm_and_claw.lower_arm().wait()
