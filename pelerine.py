import board
import digitalio

mymapping = [board.A0, board.D2]

class LED():
    def __init__(self, pin):
        self.led = digitalio.DigitalInOut(mymapping[pin-1])
        self.led.direction = digitalio.Direction.OUTPUT
    def on(self):
        self.led.value = True
    def off(self):
        self.led.value = False
