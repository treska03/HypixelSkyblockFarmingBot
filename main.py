from packages import movement
from player import Player
from api import PlayerApi, Ghost
import time
import sys

def main(argument):
    CHECK_FOR_LOCATION = True
    if CHECK_FOR_LOCATION:
        user = PlayerApi()
    else:
        user = Ghost()

    Sugar_cane = Player(user=user,
                        Actions= movement.Actions("a", "s", ""),
                        plot_n=4,
                        speed=328,
                        angle=45)
    
    Cocoa = Player(user=user,
                  Actions= movement.Actions("w", "s", "d"),
                  plot_n=2,
                  speed=155,
                  angle=0)
    
    Pumpkin_Melon = Player(user=user,
                        Actions= movement.Actions("d", "d", ""),
                        plot_n=2,
                        speed=1,
                        angle=45)
    
    Nether_wart = Player(user=user,
                         Actions= movement.Actions("d", "a", "s"),
                         plot_n=5,
                         speed=380,
                         angle=90,
                         crouch=True,)
    
    Mushrooms = Player(user=user,
                         Actions= movement.Actions("d", "a", "s"),
                         plot_n=1,
                         speed=115,
                         angle=90,)
    
    time.sleep(4)
    if argument == 1:
        Sugar_cane.main_loop(use_api=CHECK_FOR_LOCATION)
    if argument == 2:
        Cocoa.main_loop(use_api=CHECK_FOR_LOCATION)
    if argument == 3:
        Pumpkin_Melon.main_loop(use_api=CHECK_FOR_LOCATION)
    if argument == 4:
        Nether_wart.main_loop(use_api=CHECK_FOR_LOCATION)
    if argument == 5:
        Mushrooms.main_loop(use_api=CHECK_FOR_LOCATION)
    else:
        print("Wrong input. Make sure to enter a digit between 1-5")
        print("TURNING ON LAST KNOWN KNOWN STATE")
        Sugar_cane.main_loop(use_api=CHECK_FOR_LOCATION)        

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Nothing to do. Add following:\n1 for Sugar cane\n2 for cocoa\n3 for pumpking\n4 for nether wart\n5 for mushrooms")
        main(1)
    main(sys.argv[1])