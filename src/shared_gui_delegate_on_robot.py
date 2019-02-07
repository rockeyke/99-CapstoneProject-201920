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
        self.robot.drive_system.go(int(left_speed),
                                   int(right_speed))
