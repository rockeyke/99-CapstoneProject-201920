"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Alex Hinojosa.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
    introduction()
    real_thing()

    ##run_test_camera()


def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()
    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            break


def run_test_camera():
    robot = rosebot.RoseBot()

    robot.drive_system.display_camera_data()
    robot.drive_system.spin_counterclockwise_until_sees_object(100, 500)
    time.sleep(2)
    robot.drive_system.spin_clockwise_until_sees_object(50, 500)


def introduction():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speech_maker.speak('Hey Guys, my name is VR bot, I am here to help you!')


main()