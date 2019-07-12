# pelerine
pelerine is a wrapper for circuit-python intended to behave just like gpiozero
This is intended for educational purposes. It can be used for children who have just learnt to use gpiozero with RPi and need to proceed to microcontrollers with the same commands. This could evolve to circuitpython itself later.

It is a fitting educational solution when a code club has just learnt how to program a Raspberry Pi to control devices through Python and gpiozero module and needs to move on to microcontrollers.

The same commands format just like gpiozero is used but circuitpython is executed under the hood.

gpiozero and circuitpython have not been combined until now because there are some differences.

gpiozero is very good at callbacks and threads which circuitpython cannot support.

circuitpython handles I2C, SPI etc interfaces very well.

So I needed a partial gpiozero-type wrapper to use for my lessons.

And of course I share it to everyone that needs to use it as well.
