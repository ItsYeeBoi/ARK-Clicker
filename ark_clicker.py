import time
import json
from ahk import AHK

ahk = AHK()

win = ahk.win_get(title="ARK: Survival Ascended on GeForce NOW")

is_click_enabled = False
count = 0


def test_click():
    global is_click_enabled, count
    start_time = time.time()
    while is_click_enabled and time.time() - start_time < 60:
        print(f"Current Timer: {count} seconds")
        win.click(x=965, y=452, click_count=2)
        time.sleep(1)
        count += 1
    time.sleep(10)
    if is_click_enabled:
        test_click()  # Loop the code again after sleeping for 10 seconds


def toggle_click():
    global is_click_enabled, count
    count = 0
    is_click_enabled = not is_click_enabled
    print(f"Clicking {is_click_enabled}")
    test_click()


config = json.load(open("config.json"))
ahk.add_hotkey(config["start/stop_keybind"], callback=toggle_click)
ahk.start_hotkeys()
ahk.block_forever()
