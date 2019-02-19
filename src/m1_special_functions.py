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


def find_trash(robot, mqtt_sender):
    robot.drive_system.spin_counterclockwise_until_sees_object(25, -25)
    mqtt_sender.send_message('found_trash')
    robot.sound_system.speech_maker.speak('I have found trash. Let me dispose of it.').wait()

    frequency_prox(robot, 100, 50)
    mqtt_sender.send_message('moving_trash')
    robot.sound_system.speech_maker.speak('I have the trash.').wait()
    follow_line(robot)

    robot.arm_and_claw.lower_arm()
    mqtt_sender.send_message('throw_away')
    robot.sound_system.speech_maker.speak('Trash disposed.').wait()

    time.sleep(10)
    mqtt_sender.send_message('no_trash')


def follow_line(robot):
    print("Going towards trash")
    while True:
        if robot.sensor_system.color_sensor.get_color() != 1:
            robot.drive_system.go(25, 50)
        else:
            robot.drive_system.go(50, 25)
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drive_system.stop()
            break


def butler_greeting(robot):
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.motor.reset_position()
    robot.sound_system.speech_maker.speak('Good day. I hope you are doing well.').wait()
    robot.arm_and_claw.motor.turn_on(-100)
    while True:
        if abs(robot.arm_and_claw.motor.get_position()) >= (14.2 * 360):
            break
    robot.arm_and_claw.motor.turn_off()
    robot.arm_and_claw.motor.reset_position()
    robot.sound_system.speech_maker.speak('I am ready to serve.').wait()


def butler_come_to_me(robot):
    robot.drive_system.go(25, -25)
    while True:
        print(robot.sensor_system.ir_proximity_sensor.get_distance())
        if robot.sensor_system.ir_proximity_sensor.get_distance() <= 50:
            robot.drive_system.stop()
            break
    robot.drive_system.go_forward_until_distance_is_less_than(5, 50)
    robot.arm_and_claw.raise_arm()
    robot.sound_system.speech_maker.speak('How can I help you?').wait()
    robot.arm_and_claw.lower_arm()
