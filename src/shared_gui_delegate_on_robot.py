"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Alex Hinojosa, Jack Wilson, and Kirsten Rockey.
  Winter term, 2018-2019.
"""
import m1_special_functions as m1
import m3_special_functions as m3



class DelegateThatReceives(object):
    def __init__(self, robot):
        """ :type   robot = rosebot.RoseBot  """
        self.robot = robot
        self.is_time_to_stop = False

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
        self.robot.drive_system.go(int(left_speed),
                                   -int(right_speed))

    def right(self, left_speed, right_speed):
        print('right message received')
        self.robot.drive_system.go(-int(left_speed),
                                   int(right_speed))

    def stop(self):
        print('stop message received')
        self.robot.drive_system.stop()

    def raise_arm(self):
        print('raise arm message received')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('lower arm message received')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('calibrate arm message received')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        print('move arm to position message received')
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    def quit(self):
        print('quit message received')
        self.is_time_to_stop = True

    def exit(self):
        print('exit message received')
        self.exit()

    def go_straight_for_seconds(self, seconds_entry, speed_entry):
        print('go straight for seconds message received')
        self.robot.drive_system.go_straight_for_seconds(int(seconds_entry), int(speed_entry))

    def go_straight_for_inches_using_time(self, inches_entry, speed_entry):
        print('go straight for inches using time message received')
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches_entry), int(speed_entry))

    def go_straight_for_inches_using_encoder(self, inches_entry, speed_entry):
        print('go straight for inches using encoder message received')
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches_entry), int(speed_entry))

    def beep(self, beep_entry):
        print('beep message received')
        for _ in range(int(beep_entry)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, tone_entry, time_entry):
        print('tone message received')
        self.robot.sound_system.tone_maker.play_tone(int(tone_entry), int(time_entry))

    def speak(self, speak_entry):
        print('speak messgae received')
        self.robot.sound_system.speech_maker.speak(str(speak_entry))

    def fast_beep_prox(self, initial_rate, increase_rate):
        print('fast beep proximity message received')
        m1.fast_beep_prox(self.robot, float(initial_rate), float(increase_rate))

    def frequency_prox(self, initial_frequency, increase_rate):
        print('frequency proximity message received')
        m1.frequency_prox(self.robot, float(initial_frequency), float(increase_rate))

    def led_prox(self, initial_rate, increase_rate):
        print('LED proximity message received')
        m1.led_prox(self.robot, float(initial_rate), float(increase_rate))

    def spin_clockwise_until_sees_object(self, speed, area):
        print('Spin Clockwise message received')
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_sees_object(self, speed, area):
        print('Spin Counterclockwise message received')
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))
