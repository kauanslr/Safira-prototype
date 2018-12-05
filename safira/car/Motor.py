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
        if self.infrared.canRun():
            self.status = Status.ON
        else:
            self.status = Status.OFF
            print("MOTOR_PIN: " + str(self.pin) + ", STOP DUE TO INFRARED")
        self.export()
        self.exportToGPIO()


    # Make the motor stop
    def stop(self):
        self.status = Status.OFF
        self.export()
        self.exportToGPIO()


    # make the setup of RPi library
    def setupRpi(self):
        self.rpi.GPIO.setup(self.pin, self.rpi.GPIO.OUT)

    def exportToGPIO(self):
        if self.rpi is not None:
            print "Exported, and loaded to GPIO"
            self.rpi.gpio.output(self.pin, self.status)
        else:
            print "Exported, but not loaded to GPIO"
        print ""

    # export curretn status of motor
    def export(self):
        if main.TESTING:
            print("PIN: " + str(self.pin) + ", INFRARED_STATUS: " + str(self.infrared.canRun()))

