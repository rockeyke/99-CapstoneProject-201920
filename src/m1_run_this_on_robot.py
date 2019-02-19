"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Kirsten Rockey.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot
import m1_special_functions as m1


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # run_test_arm()
    # run_test_drive()
    # run_proximity_test()
    real_thing()


def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.move_arm_to_position(10*360)
    robot.arm_and_claw.move_arm_to_position(3*360)
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.lower_arm()


def run_test_drive():
    robot = rosebot.RoseBot()
    # robot.drive_system.go_straight_for_seconds(5, 100)
    # robot.drive_system.go_straight_for_seconds(2, 50)
    # robot.drive_system.go_straight_for_seconds(10, 25)

    robot.drive_system.go_straight_for_inches_using_time(10, 100)
    robot.drive_system.go_straight_for_inches_using_time(10, 50)
    time.sleep(3)
    robot.drive_system.go_straight_for_inches_using_time(5, 50)

    robot.drive_system.go_straight_for_inches_using_encoder(12, 100)


def real_thing():
    robot = rosebot.RoseBot()
    print("calibrating arm")
    robot.arm_and_claw.calibrate_arm()

    receiver_delegate = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(receiver_delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if receiver_delegate.is_time_to_stop:
            break

def real_butler():
    michaelis = rosebot.RoseBot()
    m1.butler_greeting(michaelis)

    receiver_delegate = shared_gui_delegate_on_robot.DelegateThatReceives(michaelis)
    mqtt_receiver = com.MqttClient(receiver_delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if receiver_delegate.is_time_to_stop:
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()