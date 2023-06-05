from .controller import Controller
from pynput.keyboard import Key

class Actions:

    def __init__(self, primary, secondary, sideway):
        self.primary = primary
        self.secondary = secondary
        self.sideway = sideway
    
    def release_all_keys(self, kb=True, mouse=False):
        Controller.release_all(self.primary, self.secondary, self.sideway)
    
    def hold_mouse(self, seconds=0):
        self.do_action(Controller.LMB, seconds)

    def go_sideways(self, seconds=0):
        self.do_action(self.sideway, seconds)

    def go_primary(self, seconds=0):
        self.do_action(self.primary, seconds)

    def go_secondary(self, seconds=0):
        self.do_action(self.secondary, seconds)
    
    def go_garden(self):
        Controller.tap("/")
        Controller.write("warp garden")
        Controller.tap(Key.enter)

    def do_action(self, action, seconds):
        if not seconds:
            Controller.press(action)
        else:
            Controller.press_for(action, seconds)
