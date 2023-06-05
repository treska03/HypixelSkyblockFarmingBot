import math

class Calculator:
    """
    Angles:
    0* --> 500 speed (shrooms)
    0* --> 400 speed (shrooms)
    0* --> 155 speed (coco)
    45* --> 328 speed (cane)  /// 10b/s
    90* --> 93 speed (wheat, wart, carrot, potato)
    90* --> 115 speed (wheat, wart, carrot, potato)
    90* --> 400 speed (cacti)
    90* --> 500 speed (cacti)
    """
    PLOT_LENGTH = 96
    
    @staticmethod
    def calculate_speed(plot_n, speed, crouch=False, sprint=False, angle=180):
        blocks_per_s = Calculator._get_movement_speed(speed, crouch, sprint)
        if angle==45:
            if speed == 328:
                blocks_per_s = 10.1
            elif speed == 325:
                blocks_per_s = 7.45
        return (plot_n*Calculator.PLOT_LENGTH)/blocks_per_s

    @staticmethod
    def _get_movement_speed(speed, crouch, sprint):
        if crouch:
            return 1.3*speed/100
        if sprint:
            return 5.6*speed/100
        return 4.3*speed/100
    
    
Calculator = Calculator()    