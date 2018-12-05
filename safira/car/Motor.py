from safira.sensors.infrared import Infrared
from . import State
import main


class Motor:
    # current terminal pin
    pin = 0

    # Motor related infrared pin
    infrared_pin = 0

    # Motor alias for LOG propose
    alias = None

    # Current state
    state = State.ON | State.OFF

    # Vision state
    vision_state = State.ON | State.OFF

    # RPi Library
    rpi = None

    # Infrared instance
    infrared = None


    def __init__(self, pin, infrared_pin, alias = None):
        self.pin = pin
        self.infrared_pin = infrared_pin
        self.infrared = Infrared.Infrared(self)
        self.alias = alias

    # Set RPi Library into current motor instance including infrated
    def setRpi(self, rpi):
        self.rpi = rpi
        self.infrared.setRpi(rpi)
        self.setupRpi()

    # Make the motor run
    def run(self):
        self.vision_state = State.ON
        if self.infrared.canRun():
            self.state = State.ON
        else:
            self.state = State.OFF
        self.log()
        self.exportToGPIO()


    # Make the motor stop
    def stop(self):
        self.vision_state = State.OFF
        self.state = State.OFF
        self.log()
        self.exportToGPIO()


    # make the setup of RPi library
    def setupRpi(self):
        self.rpi.GPIO.setup(self.pin, self.rpi.GPIO.OUT)

    def exportToGPIO(self):
        if self.rpi is not None:
            self.rpi.gpio.output(self.pin, self.state)

    # export curretn state of motor
    def log(self):
        if main.TESTING:
            print("---------------")
            print("MOTOR - " + str(self.alias))
            print("----")
            print("PIN_NUM: " + str(self.pin))
            print("INFRARED_STATE: " + str(self.infrared.canRun()))
            print("VISION_STATE: " + str(self.vision_state))
            print("IS_RASPBERRY: " + str(self.rpi is not None))
            print("---------------")

