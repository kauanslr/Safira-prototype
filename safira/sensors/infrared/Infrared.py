import random


class Infrared:
    # Current Control motor
    motor = None

    # rpi library
    rpi = None

    # Contructor
    def __init__(self, motor):
        self.motor = motor

    # Set the RPi library
    def setRpi(self, rpi):
        # Make the setup of infrared pin
        rpi.GPIO.setup(self.motor.infrared_pin, rpi.GPIO.IN)  # IR out
        self.rpi = rpi

    # Check if car can run
    def canRun(self):
        # If RPi library is set, so check with ir hardware if it can run
        if self.rpi is not None:
            return self.rpi.gpio.input(self.motor.infrared_pin) is True
        # If has not RPi library, so you does not have IR sensor installed, so lets return random states for testing
        else:
            return bool(random.getrandbits(1))

