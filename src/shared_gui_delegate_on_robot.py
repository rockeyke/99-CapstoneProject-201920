"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Alex Hinojosa, Jack Wilson, and Kirsten Rockey.
  Winter term, 2018-2019.
"""


class DelegateThatReceives(object):
    def __init__(self, robot):
        """ :type   robot = rosebot.RoseBot  """
        self.robot = robot

    def forward(self, left_speed, right_speed):
        print('forward message received')
        self.robot.drive_system.go(int(left_speed),
                                   int(right_speed))

    def backward(self, left_speed, right_speed):
        print('backward message received')
        self.robot.drive_system.go(int(left_speed),
                                   int(right_speed))

    def left(self, left_speed, right_speed):
        print('left message received')
        self.robot.drive_system.go(-int(left_speed),
                                   int(right_speed))

    def right(self, left_speed, right_speed):
        print('right message received')
        self.robot.drive_system.go(int(left_speed),
                                   -int(right_speed))

    def stop(self):
        print('stop message received')
        self.robot.drive_system.stop()

    def raise_arm(self):
        print('raise arm message received')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('lower arm message received')
        self.robot.arm_and_claw.lower_arm()
