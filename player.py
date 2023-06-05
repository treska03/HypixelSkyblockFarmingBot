from packages import direction, maths
from pynput.keyboard import Key
import time 
Direction = direction.Direction
primary = Direction.PRIMARY
secondary = Direction.SECONDARY
side = Direction.SIDE


class Player:

    def __init__(self, user, Actions, plot_n, speed, angle, crouch=False) -> None:
        self.user = user
        self.Actions = Actions
        
        self.direction = primary
        self.plot_n = plot_n
        self.speed = speed
        self.angle = angle
        self.crouch = crouch

        self.use_api = False
        self.location_counter = 0

    def swap(self):
        self.Actions.release_all_keys(kb=True, mouse=False)
        if self.Actions.sideway:
            self.Actions.go_sideways(1)
        if self.direction == primary:
            self.direction = secondary
            self.Actions.go_secondary()
        elif self.direction == secondary:
            self.direction = primary
            self.Actions.go_primary()
    
    def prepare(self):
        if self.crouch:
            self.Actions.do_action(action=Key.shift_l, seconds=None)
        self.Actions.hold_mouse()
        self.Actions.go_primary()

    def check_api(self):
        """
        Checks whether player is in garden island using Hypixel skyblock API
        """
        if self.use_api:
            self.location_counter += self.user.check_garden(self.location_counter)
            if self.location_counter != 0:
                self.Actions.go_garden()
                if self.location_counter >= 5:
                    exit("Exceeded safe limit for not being on garden island")

    def main_loop(self, use_api=False):
        self.use_api = use_api
        
        self.prepare()
        
        while True:
            if use_api:
                self.check_api()
            harvest_time = maths.Calculator.calculate_speed(
                plot_n=self.plot_n, 
                speed=self.speed, 
                crouch=self.crouch,
                angle=self.angle,
            )
            time.sleep(harvest_time+0.2)
            self.swap()

    
