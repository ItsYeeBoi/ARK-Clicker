__author__ = "itsyeboi"
__version__ = "0.0.1"

import time
import json
import os
import threading
from ahk import AHK

ahk = AHK()


def startup():
    print(f"ARK Clicker v{__version__}")
    print(f"Press {config['start/stop_keybind']} to start/stop clicking")
    print(f"Press {config['exit_keybind']} to exit")


config_file = open("config.json")
config = json.load(config_file)
values = []
for key, value in config["window_names"].items():
    win = ahk.win_get(title=value)
    if win:
        print(f"Window selected: {value}")
        break
else:
    print("Window not found\nExiting...")
    exit()

is_click_enabled = False
key_press_thread = None


def force_quit():
    print("Exiting...")
    os._exit(1)


def press_keys():
    while True:
        if is_click_enabled == True:
            time.sleep(config["food_and_water_timer"])
            win.send(str(config["food_slot"]))
            win.send(str(config["water_slot"]))
            print("Food and Water done")
        elif is_click_enabled == False:
            break


def clicker(click_length, pause_length):
    global is_click_enabled, key_press_thread
    start_time = time.time()

    if key_press_thread is None or not key_press_thread.is_alive():
        key_press_thread = threading.Thread(target=press_keys)
        key_press_thread.start()

    while is_click_enabled == True and time.time() - start_time < click_length:
        win.click(x=965, y=452, click_count=2)
        time.sleep(1)
    time.sleep(pause_length)
    if is_click_enabled:
        clicker(config["click_length"], config["pause_length"])


def toggle_click():
    global is_click_enabled
    is_click_enabled = not is_click_enabled
    clicking_value = is_click_enabled
    if is_click_enabled == True:
        clicking_value = "enabled"
    elif is_click_enabled == False:
        clicking_value = "disabled"
    print(f"Clicking {clicking_value}")
    if config["start/stop_keybind"]:
        clicker(config["click_length"], config["pause_length"])
    elif config["start/stop_keybind"] == False:
        print("Clicking is disabled")


if __name__ == "__main__":
    startup()
    ahk.add_hotkey(config["exit_keybind"], callback=force_quit)
    ahk.add_hotkey(config["start/stop_keybind"], callback=toggle_click)
    config_file.close()
    ahk.start_hotkeys()
    ahk.block_forever()
