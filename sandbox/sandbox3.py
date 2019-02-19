# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.


teleop_frame.grid(row=0, column=0)
arm_frame.grid(row=1, column=0)
control_frame.grid(row=2, column=0)
special_frame.grid(row=0, column=1)
sound_frame.grid(row=3, column=0)
spin_frame.grid(row=1, column=1)

teleop_frame, arm_frame, control_frame, special_frame, sound_frame, spin_frame,

teleop_frame, arm_frame, control_frame, special_frame, sound_frame, spin_frame,

teleop_frame, arm_frame, control_frame, special_frame, sound_frame = get_shared_frames(main_frame,
                                                                                       mqtt_sender)


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    special_frame = shared_gui.get_special_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.sound_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, special_frame, sound_frame


spin_frame = get_spin_frame(main_frame, mqtt_sender)
