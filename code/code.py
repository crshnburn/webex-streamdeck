import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keys = keypad.Keys((board.GP16, board.GP17, board.GP18),
                   value_when_pressed=True, pull=True)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    event = keys.events.get()
    # event will be None if nothing has happened.
    if event:
        if event.key_number == 0 and event.pressed:
            # (un)mute the call
            keyboard.press(Keycode.SHIFT, Keycode.COMMAND, Keycode.M)
            keyboard.release_all()
        if event.key_number == 1 and event.pressed:
            # start/stop video
            keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.N)
            keyboard.release_all()
        if event.key_number == 2 and event.pressed:
            # open/close the chat
            keyboard.press(Keycode.SHIFT, Keycode.COMMAND, Keycode.E)
            keyboard.release_all()
