import board
import digitalio
import time

#only for pins 1 and 2 at the moment
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

#try            
#it will not use callback            
class Button():
    def __init__(self, pin):
        self.button = digitalio.DigitalInOut(mymapping[pin-1])
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.DOWN    
    def when_pressed(self):
        while not self.button.value:
            time.sleep(0.5)
    def if_pressed(self):
        return self.button.value
    
    
    
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
