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
            time.sleep(1)
            self.off()
            time.sleep(1)

#it will not use callback            
#it is UP, so everything is reversed
class Button():
    def __init__(self, pin):
        self.button = digitalio.DigitalInOut(mymapping[pin-1])
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.UP    
    def when_pressed(self):
        while self.button.value:
            time.sleep(0.5)
    def is_pressed(self):
        return not self.button.value
    
    
    
class RGB_LED():
    def __init__(self):
        pass   

#High Level Servo Control
#Before continuing make sure your board's lib folder has the adafruit_motor folder copied over.		
#board.D5
#min, mid, max?
class Servo():
    def __init__(self, pin):
        import pulseio
		import adafruit_motor.servo
        pwm = pulseio.PWMOut(pin, frequency=50)
        self.servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2250)
    def turn(angle):
        self.servo.angle = angle
    
class Distance_Sensor():
    def __init__(self):
        pass   
    
class Gas_Sensor():
    def __init__(self):
        pass    
    
class Buzzer():
    def __init__(self):
        pass    
