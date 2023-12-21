# ARK Clicker
 ARK AFK Clicker

Requires Python 3.8+

# Installation

**Install Python Here:** [Python](https://www.python.org/downloads/)

```
pip install -r requirements.txt
```

Example config file
-----------------
```
{
    "start/stop_keybind": "F3", # Keybind you want to start/stop the clicker
    "exit_keybind": "F9", # Keybind to kill the script
    "click_length": 60, # How long you want it to click for (Seconds)
    "pause_length": 10, # How long you want it to pause for (Seconds)
    "food_and_water_timer": 3600, # How long 
    "food_slot": 6, # The slot food is in
    "water_slot": 7, # The slot water is in
    "window_names": { # If your games title isnt there you can add it on
            "1": "ArkAscended",
            "2": "ARK: Survival Ascended on GeForce NOW",
            "3": "Add your games title here"
        }
}
```

Dependencies
============

- [ahk](https://github.com/spyoungtech/ahk)