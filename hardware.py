#Libraries
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Hardware:

    #GPIO Pins 
    #Motors
    self.MOTOR11 = 12 #1 - front
    self.MOTOR12 = 16 #1 - back
    self.MOTOR21 = 21 #2 - front
    self.MOTOR22 = 20 #2 - back

    #Ultrassonic sensor
    self.GPIO_TRIGGER = 4
    self.GPIO_ECHO = 17

    def make_setup(self):
        """
        Description
        
        Setup GPIO pins to IN and OUT
        """
        #Motors
        GPIO.setup(self.MOTOR11, GPIO.OUT)
        GPIO.setup(self.MOTOR12, GPIO.OUT)
        GPIO.setup(self.MOTOR21, GPIO.OUT)
        GPIO.setup(self.MOTOR22, GPIO.OUT)

        #UltrassonicSensor
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
    
    def distance(self):
        """
        Description

        Calculate the distance between the car and some object 
        """
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    
        return distance

    def stop(self):
        """
        Description

        When called, stop the robot.

        Parameters

        self: reference to the current instance of the class

        Return 

        Nothing :)
        """
        GPIO.output(self.MOTOR11, 0)
        GPIO.output(self.MOTOR12, 0)
        GPIO.output(self.MOTOR21, 0)
        GPIO.output(self.MOTOR22, 0)

    def forward(self):
        """
        Description

        When called, the robot moves forward

        Parameters

        self: reference to the current instance of the class

        Return 

        Nothing :)
        """
        GPIO.output(self.MOTOR11, 1)
        GPIO.output(self.MOTOR12, 0)
        GPIO.output(self.MOTOR21, 1)
        GPIO.output(self.MOTOR22, 0)

    def backward(self):
        """
        Description

        When called, the robot moves backward

        Parameters

        self: reference to the current instance of the class

        Return 

        Nothing :)
        """

        GPIO.output(self.MOTOR11, 0)
        GPIO.output(self.MOTOR12, 1)
        GPIO.output(self.MOTOR21, 0)
        GPIO.output(self.MOTOR22, 1)

    def left(self):
        """
        Description

        When called, the robot moves left

        Parameters

        self: reference to the current instance of the class

        Return 

        Nothing :)

        """
        
        GPIO.output(self.MOTOR11, 0)
        GPIO.output(self.MOTOR12, 1)
        GPIO.output(self.MOTOR21, 1)
        GPIO.output(self.MOTOR22, 0)
        
    def right(self):
        """
        Description

        When called, the robot moves right

        Parameters

        self: reference to the current instance of the class

        Return 

        Nothing :)
        """
        GPIO.output(self.MOTOR11, 1)
        GPIO.output(self.MOTOR12, 0)
        GPIO.output(self.MOTOR21, 0)
        GPIO.output(self.MOTOR22, 1)