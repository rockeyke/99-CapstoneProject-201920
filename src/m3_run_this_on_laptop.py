"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Alex Hinojosa.
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
    root.title('Alex CSSE 120 WINTER 18-19 CAPSTONE')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, special_frame, sound_frame = get_shared_frames(main_frame,
                                                                                           mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)
    spin_frame = get_spin_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, special_frame, sound_frame, spin_frame)

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


def grid_frames(teleop_frame, arm_frame, control_frame, special_frame, sound_frame, spin_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    special_frame.grid(row=0, column=1)
    sound_frame.grid(row=3, column=0)
    spin_frame.grid(row=1, column=1)


def get_spin_frame(window, mqtt_sender):
    # Construct labels, entry boxes and buttons
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Spin Until Object Controls")
    speed_label = ttk.Label(frame, text="Speed of Spin")
    area_label = ttk.Label(frame, text="Area of Object to Stop at")

    speed_entry = ttk.Entry(frame, width=10)
    area_entry = ttk.Entry(frame, width=10)

    ccw_spin_button = ttk.Button(frame, text="Spin CounterClockwise")
    cw_spin_button = ttk.Button(frame, text="Spin Clockwise")

    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=0)
    area_label.grid(row=1, column=1)
    speed_entry.grid(row=2, column=0)
    area_entry.grid(row=2, column=1)
    ccw_spin_button.grid(row=3, column=0)
    cw_spin_button.grid(row=3, column=1)

    cw_spin_button["command"] = lambda: handle_spincw(
        speed_entry, area_entry, mqtt_sender)
    ccw_spin_button["command"] = lambda: handle_spinccw(
        speed_entry, area_entry, mqtt_sender)

    return frame


def handle_spincw(speed_entry, area_entry, mqtt_sender):
    print('Clockwise Spin: ''Speed', speed_entry.get(), 'Area', area_entry.get())
    mqtt_sender.send_message("spin_clockwise_until_sees_object", [speed_entry.get(), area_entry.get()])


def handle_spinccw(speed_entry, area_entry, mqtt_sender):
    print('Counterclockwise Spin: ''Speed', speed_entry.get(), 'Area', area_entry.get())
    mqtt_sender.send_message("spin_counterclockwise_until_sees_object", [speed_entry.get(), area_entry.get()])



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()