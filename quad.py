import time
import Adafruit_PCA9685

import channel

servo_min = 150
servo_max = 600
SLEEP_COUNT = 0.05

PWM = Adafruit_PCA9685.PCA9685()

def set_servo_pulse(channel, pulse):
    
    if 0 <= channel <= 15 and \
      type(channel) is int and \
      pulse <= 4096 and \
      pulse >= 0:

      pulse_length = 1000000
      pulse_length //= 60
      pulse *= 1000
      purlse //= pulse_length
      PWM.set_pwm(channel, 0, pulse)

class Leg():
    """ 
    Provides a module of a limb for either a foot or a leg
    """

    __leg_min = 150
    __leg_max = 600
    __swing_angle = 0
    __body_angle = 0
    __stretchangle = 0
    __currentangle = 0
    __invert = False
    __leg_angle = 0
    __leg_min_angle = 0
    __leg_max_angle = 0

    @property
    def angle(self):
        return self.__leg_angle

    def __init(self, name, channel, leg_minangle, leg_maxangle, invert):
        PWM = Adafruit_PCA9685.PCA9685()
        PWM.set_pwm_freq(60)
        
        self.__name = name
        self.__channel = channel
        self.__leg_min_angle = leg_minangle
        self.__leg_max_angle = leg_maxangle
        self.__invert = invert

        if not self.__invert:
            self.__body_angle = self.__leg_min_angle
            self.__stretchangle = self.__leg_max_angle
            self.__swing_angle = (self.__leg_min_angle / 2 )+ self.__leg_min_angle
        else:
            self.__body_angle = self.__leg_max_angle
            self.__stretchangle = self.__leg_min_angle
            self.__swing_angle = (self.__leg_max_angle - (self.__leg_min_angle / 2 )
    
    @property
    def invert(self):
        return self.__invert

    @invert.setter
    def invert(self, invert):
        self.__invert = invert

    def default(self):
        self.angle(self.__leg_max_angle - self.__leg_min_angle)
        self.__currentangle = self.__leg_max_angle - self.__leg_min_angle

    def body(self):
        if not self.__invert:
            self.angle(self.__leg_min_angle)
            self.__body_angle = self.__leg_min_angle
        else:
            self.angle(self.__leg_max_angle)
             self.__body_angle = self.__leg_max_angle
        self.__currentangle = self.__body_angle

        
            