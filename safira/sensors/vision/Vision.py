import cv2
import numpy as np
from importlib import import_module

import main


# Class Vision
class Vision:
    # PiCamera Library
    picamera = None

    # Cascade of trained object
    CASCADE_PATH = main.CASCADE_LOCATION

    # Use capture provided by OpenCV
    useCvCapture = True

    # Capture interface
    capture = None

    # Parent Car - Provide the run and stop functions
    car = None

    # Loaded cascade
    cascade = None

    # Control the infine loop of capturations
    run = True

    # Colors
    colors = {
        'red': [
            np.array([2, 67, 100]),
            np.array([0, 100, 100])
        ],
        "green": [
            np.array([136, 84, 91]),
            np.array([126, 86, 74])
        ]
    }

    # Constructor
    def __init__(self, car):

        self.car = car
        self.loadCascade()
        if self.useCvCapture:
            self.useOcvCamera()

    # Set current capture method to RaspberryPi Module
    def usePiCamera(self):

        self.useCvCapture = False
        picamera = import_module('picamera')
        with picamera.PiCamera() as camera:
            self.capture = camera
            self.picamera = picamera
            self.capture = picamera.PiCamera()
            self.capture.resolution = (1024, 768)
            self.capture.framerate = 30
            self.capture.rotate = 180

    # Set current capture method to OpenCV
    def useOcvCamera(self):

        self.useCvCapture = True
        if main.TESTING is True and main.TESTING_FILE is not None:
            self.capture = cv2.VideoCapture(main.TESTING_FILE)
        else:
            self.capture = cv2.VideoCapture(0)

    # Load CASCADE_PATH file into self.cascade
    def loadCascade(self):

        self.cascade = cv2.CascadeClassifier(self.CASCADE_PATH)

    # Get one frame from capture interface
    def grabFrame(self):
        if self.useCvCapture:
            return self.capture.read()
        else:
            with self.picamera.array.PiRGBArray(self.capture.capture) as stream:
                self.capture.capture(stream, format='bgr')
                return stream.array

    # Detect objects using self.cascade and providaded grayscale frame
    def getObjects(self, gray):

        return self.cascade.detectMultiScale(gray, 1.01, 5)

    # Get grayscale version of frame
    def getGray(self, frame):

        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Segment the detected object from frame
    def getSegment(self, objects, img):

        frame = None
        for (x, y, w, h) in objects:
            frame = img[y:y + h, x:x + w]
        return frame

    # Find Contours in some mask and return True if founded an area > tha 300
    def trackColor(self, mask):
        # track red color
        (_, contours, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        founded = False

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 300:
                founded = True
        return founded

    # Detect the Green and Red colors in the image
    def detectColors(self, img):
        # Convert the HSV colorspace
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        green_mask = cv2.inRange(hsv, self.colors['green'][0], self.colors['green'][1])
        red_mask = cv2.inRange(hsv, self.colors['red'][0], self.colors['red'][1])

        # define kernel size
        kernel = np.ones((5, 5), "uint8")

        # dilatate the red color
        red_mask = cv2.dilate(red_mask, kernel)

        # dilatate the green color
        green_mask = cv2.dilate(green_mask, kernel)

        # track colors
        has_green = self.trackColor(green_mask)
        has_red = self.trackColor(red_mask)

        return {"hasRed": has_red, "hasGreen": has_green}

    # Take an action based on
    def takeAction(self, lights):
        if lights is not None:
            data = self.detectColors(lights)
            print("Founded")

            if data["hasRed"] is True:
                print("Har Red")
                self.car.stop()

            elif data["hasGreen"] is True:
                self.car.run()
                print("Har Green")

            else:
                self.car.run()
                print("Lights are off")

        # If no lights detected run the car
        else:
            self.car.run()
            print("Not Found")

    # Start the detection
    def startDetection(self):

        if self.capture is not None:
            while self.run:
                ret, frame = self.grabFrame()
                gray = self.getGray(frame)
                objects = self.getObjects(gray)
                segment = self.getSegment(objects, frame)

                self.takeAction(segment)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.run = False

    # Load modules
    def load(self):

        self.loadCascade()
