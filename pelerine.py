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


#to be added in the future
class RGB_LED():
    def __init__(self):
        pass

#High Level Servo Control
#https://learn.adafruit.com/using-servos-with-circuitpython/high-level-servo-control
#https://circuitpython.readthedocs.io/en/2.x/shared-bindings/pulseio/__init__.html
#Before continuing make sure your board's lib folder has the adafruit_motor folder copied.		
#if there is capacity issue, copy only servo part
#board.D5 is used in original tutorial, I use board.D2 in my example
#in gpiozero there were min, mid, max methods, not sure If they are needed to be recreated here
class Servo():
    def __init__(self, pin):
        import pulseio
        import adafruit_motor.servo
        pwm = pulseio.PWMOut(mymapping[pin-1], frequency=50)
        self.servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2250)
    def turn(self, angle):
        self.servo.angle = angle

#to be added in the future
class Distance_Sensor():
    def __init__(self):
        pass

#to be added in the future
class Gas_Sensor():
    def __init__(self):
        pass

#to be added in the future
class Buzzer():
    def __init__(self):
        pass
