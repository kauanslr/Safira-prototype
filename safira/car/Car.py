import pkgutil
from importlib import import_module
from safira.sensors.vision import Vision

from . import Motor


# safira model
class Car:

    # Left Motor - Motor Pin, IR Pin, IRTerminal A, IRTerminal B
    left = Motor.Motor(pin=16, infrared_pin=26, alias='LEFT')

    # Right Motor - Motor Pin, IR Pin, IRTerminal A, IRTerminal B
    right = Motor.Motor(pin=18, infrared_pin=28, alias='RIGHT')

    # Vision module
    vision = None

    # Constructor
    def __init__(self):
        self.vision = Vision.Vision(self)
        if self.has_rpi_lib():
            rpi = import_module('RPi')
            rpi.gpio.setmode(rpi.gpio.BOARD)
            self.left.rpi = rpi
            self.right.rpi = rpi
            self.rpi = rpi
            self.vision.usePiCamera()
        else:
            self.vision.useOcvCamera()

    @staticmethod
    # Verify the existence of RPi library, present only in raspberry
    def has_rpi_lib():
        rpi_loader = pkgutil.find_loader('rpi')
        found = rpi_loader is not None
        return found

    # Turn on the motors
    def run(self):
        self.left.run()
        self.right.run()

    # Turn off motors
    def stop(self):
        self.left.stop()
        self.right.stop()

    # Start the main processing
    def start(self):
        # Load vision module
        self.vision.load()
        # Start Vision detection
        self.vision.startDetection()

