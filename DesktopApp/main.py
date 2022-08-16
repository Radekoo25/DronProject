import tkinter as tk
import dron_client

HEIGHT = 600
WIDTH = 800


def exitWindow(window):
    window.destroy()

def OpenConfigurationWindow():
        configuration_window = tk.Tk()
        canvas_configuration_window = tk.Canvas(configuration_window, height=HEIGHT, width=WIDTH)
        canvas_configuration_window.pack()

        # Actual menu name
        label_configuration_menu = tk.Label(configuration_window, text='Configuration Menu')
        label_configuration_menu.config(font=('helvetica', 50))
        canvas_configuration_window.create_window((WIDTH / 2), 100, window=label_configuration_menu)

        # Yaw
        label_yaw = tk.Label(configuration_window, text='Yaw')
        label_yaw.config(font=('helvetica', 35), fg="red")
        canvas_configuration_window.create_window(WIDTH/4-120, 220, window=label_yaw)

        label_yaw_kp = tk.Label(configuration_window, text='KP:')
        label_yaw_kp.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(WIDTH/4-150, 300, window=label_yaw_kp)

        entry_yaw_kp = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(WIDTH/4-50, 300, window=entry_yaw_kp)

        label_yaw_ki = tk.Label(configuration_window, text='KI:')
        label_yaw_ki.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(WIDTH/4-150, 350, window=label_yaw_ki)

        entry_yaw_ki = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(WIDTH/4-50, 350, window=entry_yaw_ki)

        label_yaw_kd = tk.Label(configuration_window, text='KD:')
        label_yaw_kd.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(WIDTH/4-150, 400, window=label_yaw_kd)

        entry_yaw_kd = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(WIDTH/4-50, 400, window=entry_yaw_kd)

        # Pitch
        label_pitch = tk.Label(configuration_window, text='Pitch')
        label_pitch.config(font=('helvetica', 35), fg="red")
        canvas_configuration_window.create_window(2*WIDTH/4-120, 220, window=label_pitch)

        label_pitch_kp = tk.Label(configuration_window, text='KP:')
        label_pitch_kp.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(2*WIDTH / 4 - 150, 300, window=label_pitch_kp)

        entry_pitch_kp = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(2*WIDTH / 4 - 50, 300, window=entry_pitch_kp)

        label_pitch_ki = tk.Label(configuration_window, text='KI:')
        label_pitch_ki.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(2*WIDTH/4-150, 350, window=label_pitch_ki)

        entry_pitch_ki = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(2*WIDTH/4-50, 350, window=entry_pitch_ki)

        label_pitch_kd = tk.Label(configuration_window, text='KD:')
        label_pitch_kd.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(2*WIDTH/4-150, 400, window=label_pitch_kd)

        entry_pitch_kd = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(2*WIDTH/4-50, 400, window=entry_pitch_kd)

        # Roll
        label_roll = tk.Label(configuration_window, text='Roll')
        label_roll.config(font=('helvetica', 35), fg="red")
        canvas_configuration_window.create_window(3*WIDTH/4-120, 220, window=label_roll)

        label_roll_kp = tk.Label(configuration_window, text='KP:')
        label_roll_kp.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(3*WIDTH / 4 - 150, 300, window=label_roll_kp)

        entry_roll_kp = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(3*WIDTH / 4 - 50, 300, window=entry_roll_kp)

        label_roll_ki = tk.Label(configuration_window, text='KI:')
        label_roll_ki.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(3*WIDTH/4-150, 350, window=label_roll_ki)

        entry_roll_ki = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(3*WIDTH/4-50, 350, window=entry_roll_ki)

        label_roll_kd = tk.Label(configuration_window, text='KD:')
        label_roll_kd.config(font=('helvetica', 25))
        canvas_configuration_window.create_window(3*WIDTH/4-150, 400, window=label_roll_kd)

        entry_roll_kd = tk.Entry(configuration_window)
        canvas_configuration_window.create_window(3*WIDTH/4-50, 400, window=entry_roll_kd)

        def SendConfiguration():
            dron_client.setPID(dron_client.create_pid_configuration(
                int(entry_yaw_kp.get()), int(entry_yaw_ki.get()), int(entry_yaw_kd.get()),
                int(entry_pitch_kp.get()), int(entry_pitch_ki.get()), int(entry_pitch_kd.get()),
                int(entry_roll_kp.get()), int(entry_roll_ki.get()), int(entry_roll_kd.get())))

        # Send PID configuration
        button_send_configuration = tk.Button(configuration_window,
                                           text="Send configuration",
                                           font=(None, 15),
                                           bg='White',
                                           fg='Black',
                                           command=SendConfiguration)
        canvas_configuration_window.create_window((WIDTH/2-150), 500, window=button_send_configuration)

        # Back to main menu
        button_back_to_main_menu = tk.Button(configuration_window,
                                           text="Back",
                                           font=(None, 15),
                                           bg='White',
                                           fg='Black',
                                           command=lambda: [exitWindow(configuration_window)])
        canvas_configuration_window.create_window((WIDTH/2+150), 500, window=button_back_to_main_menu)


# Main window
def MainWindow():
    root = tk.Tk()

    root.title("DronDesktopApp")
    root.resizable(False, False)
    canvas_root = tk.Canvas(root, width=WIDTH, height=HEIGHT, relief='raised')
    canvas_root.pack()

    # Actual menu name
    label_main_menu = tk.Label(root, text='Main Menu')
    label_main_menu.config(font=('helvetica', 50))
    canvas_root.create_window((WIDTH/2), 100, window=label_main_menu)

    # Go to configuration menu
    button_go_to_configuration = tk.Button(root,
                                           text="Configuration",
                                           font=(None, 25),
                                           bg='White',
                                           fg='Black',
                                           command=lambda: [OpenConfigurationWindow()])
    canvas_root.create_window((WIDTH/2), 250, window=button_go_to_configuration)

    # Go to control menu
    button_go_to_control = tk.Button(root, text="Control", font=(None, 25), bg='White', fg='Black')
    canvas_root.create_window((WIDTH/2), 400, window=button_go_to_control)

    root.mainloop()

MainWindow()