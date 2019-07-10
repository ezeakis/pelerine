import board
import digitalio
import time

mymapping = [board.A0, board.D2]

class LED():
    def __init__(self, pin):
        self.led = digitalio.DigitalInOut(mymapping[pin-1])
        self.led.direction = digitalio.Direction.OUTPUT
    def on(self):
        self.led.value = True
    def off(self):
        self.led.value = False
    #try    
    def blink(self):
        while True:
            self.on()
            time.sleep()
            self.off()
            time.sleep()

class Button():
    def __init__(self):
        pass

class RGB_LED():
    def __init__(self):
        pass   
    
class Servo():
    def __init__(self):
        pass    
    
class Distance_Sensor():
    def __init__(self):
        pass   
    
class Gas_Sensor():
    def __init__(self):
        pass    
    
class Buzzer():
    def __init__(self):
        pass    
