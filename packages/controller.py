from pynput import keyboard, mouse
import time

class Controller:

    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
        self.LMB = mouse.Button.left
    
    def write(self, msg):
        self.keyboard.type(msg)
        time.sleep(0.05)
    
    def tap(self, key):
        self.keyboard.tap(key)
        time.sleep(0.05)

    def press(self, *buttons):
        for button in buttons:
            if isinstance(button, mouse.Button):
                self.mouse.press(button)
            else:
                self.keyboard.press(button)
        time.sleep(0.1)
    
    def release(self, *buttons):
        for button in buttons:
            if button:
                if isinstance(button, mouse.Button):
                    self.mouse.release(button)
                else:
                    self.keyboard.release(button)
        time.sleep(0.1)
    
    def release_all(self, *buttons):
        for button in buttons:
            self.release(button)
        time.sleep(0.1)

    def press_for(self, button, seconds):
        self.press(button)
        time.sleep(seconds)
        self.release(button)
        time.sleep(0.05)
    
Controller = Controller()