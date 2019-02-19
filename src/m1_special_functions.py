import time

def fast_beep_prox(robot, initial_rate, increase_rate):
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
    robot.drive_system.go(50, 50)
    while True:
        robot.sound_system.beeper.beep().wait()
        current_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        print(current_distance)
        if current_distance < initial_distance:
            initial_rate = initial_rate-increase_rate
            initial_distance = current_distance
            if initial_rate < 0.05:
                time.sleep(0.05)
            else:
                time.sleep(initial_rate)
        elif current_distance > initial_distance:
            initial_rate = initial_rate + increase_rate
            initial_distance = current_distance
            if initial_rate < 0.05:
                time.sleep(0.05)
            else:
                time.sleep(initial_rate)
        else:
            if initial_rate < 0.05:
                time.sleep(0.05)
            else:
                time.sleep(initial_rate)

        if current_distance <= 5:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.raise_arm()


def led_prox(robot, initial_rate, increase_rate):
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
    robot.drive_system.go(50, 50)
    while True:
        robot.led_system.only_left_on()
        time.sleep(initial_rate)
        robot.led_system.only_right_on()
        time.sleep(initial_rate)
        robot.led_system.turn_both_leds_on()
        time.sleep(initial_rate)
        robot.led_system.turn_both_leds_off()
        time.sleep(initial_rate)
        current_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        print(current_distance)
        if current_distance < initial_distance:
            initial_rate = initial_rate-increase_rate
            initial_distance = current_distance
            if increase_rate < 0.05:
                time.sleep(0.05)
            else:
                time.sleep(increase_rate)
        elif current_distance > initial_distance:
            initial_rate = initial_rate + increase_rate
            initial_distance = current_distance
            if initial_rate < 0.05:
                time.sleep(0.05)
        else:
            time.sleep(initial_rate)

        if current_distance <= 5:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.raise_arm()


def frequency_prox(robot, initial_frequency, increase_rate):
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
    robot.drive_system.go(50, 50)
    while True:
        robot.sound_system.tone_maker.play_tone(initial_frequency, 500).wait()
        current_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        print(current_distance)
        if current_distance < initial_distance:
            initial_frequency = initial_frequency+increase_rate
            initial_distance = current_distance
        elif current_distance > initial_distance:
            initial_frequency = initial_frequency - increase_rate
            initial_distance = current_distance

        if current_distance <= 5:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.raise_arm()


def find_trash(robot):
    robot.drive_system.robot.drive_system.spin_counterclockwise_until_sees_object(25, 50)
    robot.sound_system.speech_maker.speak('I have found trash. Let me dispose of it.')
    frequency_prox(robot, 100, 50)
    robot.sound_system.speech_maker.speak('I have the trash.')
    follow_line(robot)
    robot.arm_and_claw.lower_arm()


def follow_line(robot):
    print("Going towards trash")
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_color() != 1:
            robot.drive_system.go(25, 50)
        else:
            robot.drive_system.go(50, 50)
        if robot.sensor_system.color_sensor.get_color() == 5:
            break


def butler_greeting(robot):
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.motor.reset_position()
    robot.sound_system.speech_maker.speak('Good day. I hope you are doing well.')
    robot.arm_and_claw.motor.turn_on(-100)
    while True:
        if abs(robot.motor.get_position()) >= (14.2 * 360):
            break
    robot.arm_and_claw.motor.turn_off()
    robot.arm_and_claw.motor.reset_position()
    robot.sound_system.speech_maker.speak('I am ready to serve.')


def butler_come_to_me(robot):
    robot.drive_system.go(50, -50)
    if robot.sensor_system.ir_proximity_sensor.get_distance() <= 100:
        robot.drive_system.stop()
        robot.drive_system.go_until_distance_is_within(0.5, 1, 50)

        robot.arm_and_claw.raise_arm()
        robot.sound_system.speech_maker.speak('How can I help you?')
        robot.arm_and_claw.lower_arm()