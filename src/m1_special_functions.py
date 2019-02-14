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
            time.sleep(initial_rate)
        elif current_distance > initial_distance:
            initial_rate = initial_rate + increase_rate
            initial_distance = current_distance
            time.sleep(initial_rate)
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
            time.sleep(initial_rate)
        elif current_distance > initial_distance:
            initial_rate = initial_rate + increase_rate
            initial_distance = current_distance
            time.sleep(initial_rate)
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