from safira.sensors.infrared import Infrared
from . import Status
import main


class Motor:
    # current terminal pin
    pin = 0

    # Motor related infrared pin
    infrared_pin = 0

    # Current status
    status = Status.ON | Status.OFF

    # RPi Library
    rpi = None

    # Infrared instance
    infrared = None

    def __init__(self, pin, infrared_pin, rpi = None):
        self.pin = pin
        self.infrared_pin = infrared_pin
        self.infrared = Infrared.Infrared(self)

    # Set RPi Library into current motor instance including infrated
    def setRpi(self, rpi):
        self.rpi = rpi
        self.infrared.setRpi(rpi)
        self.setupRpi()

    # Make the motor run
    def run(self):
        self.status = Status.ON
        self.export()
        if self.infrared.canRun():
            self.exportToGPIO()


    # Make the motor stop
    def stop(self):
        self.status = Status.OFF
        self.export()
        if self.infrared.canRun():
            self.exportToGPIO()


    # make the setup of RPi library
    def setupRpi(self):
        self.rpi.GPIO.setup(self.pin, self.rpi.GPIO.OUT)

    def exportToGPIO(self):
        if self.rpi is not None:
            self.rpi.gpio.output(self.pin, self.status)
        else:
            print "Exported,"

    # export curretn status of motor
    def export(self):
        if main.TESTING:
            print("PIN: " + str(self.pin) + ", VISION_STATUS: " + str(self.status) + "INFRARED_STATUS: " + str(self.infrared.canRun()))

