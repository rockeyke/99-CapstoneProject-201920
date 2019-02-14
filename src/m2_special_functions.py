"""
Capstone project.  Code to run on LAPTOP (not EV3 robot).

Contains special functions

Author: Jack Wilson
"""
from tkinter import ttk
import rosebot
import time

def color_sensor_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Color sensor frame")
    follow_line_button = ttk.Button(frame, text="Follow the black line")
    speed_label = ttk.Label(frame, text="Input desired speed here")
    speed_entry = ttk.Entry(frame, width=4)
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=1)
    speed_entry.grid(row=2, column=1)
    follow_line_button["command"] = lambda: follow_line(speed_entry.get(), mqtt_sender)
    follow_line_button.grid(row=3, column=1)
    return frame


def follow_line(speed, mqtt_sender):
    color_sensor = rosebot.ColorSensor("3")
    original = color_sensor.get_reflected_light_intensity()
    error = color_sensor.get_reflected_light_intensity() - original
    print("forward")
    mqtt_sender.send_message("forward", [speed, speed])
    mistakes = 0
    if error > 0:
        if mistakes % 2 == 0:
            v = speed - error
            print("turn")
            mqtt_sender.send_message("forward", [v, speed])
        else:
            v = speed - error
            print("turn")
            mqtt_sender.send_message("forward", [speed, v])


def move_object():
    arm = rosebot.ArmAndClaw()
    arm.raise_arm()


def turn_around(speed):
    