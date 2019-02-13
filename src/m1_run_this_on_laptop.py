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
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, special_frame, sound_frame = get_shared_frames(main_frame, mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)
    proximity_frame = get_proximity_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, special_frame, sound_frame, proximity_frame)


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
    fast_beep_button["command"] = lambda: handle_LED(
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


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()