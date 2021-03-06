"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Kirsten Rockey.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    d = Laptop_Delegate()
    mqtt_sender = com.MqttClient(d)
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    # main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    # main_frame.grid()
    butler_window = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    butler_window.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    # teleop_frame, arm_frame, control_frame, special_frame, sound_frame = get_shared_frames(main_frame, mqtt_sender)
    teleop_frame = shared_gui.get_teleoperation_frame(butler_window, mqtt_sender)
    basic_frame = get_basic_frame(butler_window, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)
    # proximity_frame = get_proximity_frame(main_frame, mqtt_sender)
    butler_frame = get_butler_frame(butler_window, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, special_frame, sound_frame, proximity_frame)
    teleop_frame.grid(row=1, column=0)
    basic_frame.grid(row=0, column=0)
    butler_frame.grid(row=0, column=1)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    special_frame = shared_gui.get_special_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.sound_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, special_frame, sound_frame


def grid_frames(teleop_frame, arm_frame, control_frame, special_frame, sound_frame, proximity_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    special_frame.grid(row=0, column=1)
    sound_frame.grid(row=1, column=1)
    proximity_frame.grid(row=2, column=1)

def get_proximity_frame(window, mqtt_sender):
    #Construct labels, entry boxes and buttons
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Proximity Controls")
    initial_rate_label = ttk.Label(frame, text="Initial Rate")
    increase_rate_label = ttk.Label(frame, text="Rate of Increase")
    frequency_label = ttk.Label(frame, text="Initial Frequency")

    initial_rate_entry = ttk.Entry(frame, width=8)
    increase_rate_entry = ttk.Entry(frame, width=8)
    frequency_entry = ttk.Entry(frame, width=8)

    fast_beep_button = ttk.Button(frame, text="Beep proximity")
    frequency_button = ttk.Button(frame, text="Frequency proximity")
    LED_button = ttk.Button(frame, text="LED proximity")

    #Grid constructions
    frame_label.grid(row=0, column=1)
    initial_rate_label.grid(row=1, column=0)
    initial_rate_entry.grid(row=2, column=0)
    increase_rate_label.grid(row=3, column=0)
    increase_rate_entry.grid(row=4, column=0)
    frequency_label.grid(row=5, column=0)
    frequency_entry.grid(row=6, column=0)
    fast_beep_button.grid(row=2, column=3)
    frequency_button.grid(row=3, column=3)
    LED_button.grid(row=4, column=3)

    # Set the button callbacks:
    fast_beep_button["command"] = lambda: handle_fast_beep(
        initial_rate_entry, increase_rate_entry, mqtt_sender)
    frequency_button["command"] = lambda: handle_frequency(
        frequency_entry, increase_rate_entry, mqtt_sender)
    LED_button["command"] = lambda: handle_LED(
        initial_rate_entry, increase_rate_entry, mqtt_sender)

    return frame


def handle_fast_beep(initial_rate_entry, increase_rate_entry, mqtt_sender):
    print('Fast Beep Proximity', 'initial value:', initial_rate_entry.get(), 'rate:', increase_rate_entry.get())
    mqtt_sender.send_message("fast_beep_prox", [initial_rate_entry.get(), increase_rate_entry.get()])

def handle_LED(initial_rate_entry, increase_rate_entry, mqtt_sender):
    print('LED Proximity', 'initial value:', initial_rate_entry.get(), 'rate:', increase_rate_entry.get())
    mqtt_sender.send_message("led_prox", [initial_rate_entry.get(), increase_rate_entry.get()])

def handle_frequency(frequency_entry, increase_rate_entry, mqtt_sender):
    print('Frequency Proximity', 'initial value:', frequency_entry.get(), 'rate:', increase_rate_entry.get())
    mqtt_sender.send_message("frequency_prox", [frequency_entry.get(), increase_rate_entry.get()])


def get_butler_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Butler Commands")
    trash_button = ttk.Button(frame, text="Clean Up")
    greetings_button = ttk.Button(frame, text='Greetings')
    follow_button = ttk.Button(frame, text='Come to Me')

    frame_label.grid(row=0, column=1)
    trash_button.grid(row=1, column=0)
    greetings_button.grid(row=1, column=1)
    follow_button.grid(row=1, column=2)

    trash_button["command"] = lambda: handle_trash(mqtt_sender)
    greetings_button["command"] = lambda: handle_greeting(mqtt_sender)
    follow_button["command"] = lambda: handle_follow(mqtt_sender)

    return frame


def handle_trash(mqtt_sender):
    print('Looking for trash')
    mqtt_sender.send_message('find_trash')

def handle_greeting(mqtt_sender):
    print('Good day!')
    mqtt_sender.send_message('butler_greeting')

def handle_follow(mqtt_sender):
    print('What do you need?')
    mqtt_sender.send_message('butler_come_to_me')


def get_basic_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='Basic Commands')
    stop_button = ttk.Button(frame, text="Stop")
    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    quit_robot_button = ttk.Button(frame, text="Quit")
    exit_button = ttk.Button(frame, text="Exit")

    stop_button["command"] = lambda: shared_gui.handle_stop(mqtt_sender)
    raise_arm_button["command"] = lambda: shared_gui.handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: shared_gui.handle_lower_arm(mqtt_sender)
    quit_robot_button["command"] = lambda: shared_gui.handle_quit(mqtt_sender)
    exit_button["command"] = lambda: shared_gui.handle_exit(mqtt_sender)

    frame_label.grid(row=0, column=1)
    raise_arm_button.grid(row=1, column=1)
    stop_button.grid(row=2, column=1)
    lower_arm_button.grid(row=3, column=1)
    quit_robot_button.grid(row=4, column=0)
    exit_button.grid(row=4, column=2)

    return frame


class Laptop_Delegate(object):

    def found_trash(self):
        print('piece of trash found')

    def moving_trash(self):
        print('moving trash to trash can')

    def throw_away(self):
        print('throwing trash away')

    def no_trash(self):
        print('no trash to be found')
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()