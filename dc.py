from nanpy import ArduinoApi
from time import sleep


class Motor:
    def __init__(self, en, in1, in2, a = ArduinoApi()):
        self.en = en
        self.in1 = in1
        self.in2 = in2
        self.a = a
        self.a.pinMode(en, a.OUTPUT)
        self.a.pinMode(in1, a.OUTPUT)
        self.a.pinMode(in2, a.OUTPUT)

    def moveDown(self, speed = 200):
        self.a.digitalWrite(self.in1, self.a.HIGH)
        self.a.digitalWrite(self.in2, self.a.LOW)
        self.a.analogWrite(self.en, speed)

    def moveUp(self,  speed = 200,):
        self.a.digitalWrite(self.in1, self.a.LOW)
        self.a.digitalWrite(self.in2, self.a.HIGH)
        self.a.analogWrite(self.en, speed)



class MotorController:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def moveUp(self, duration=2000):
        self.m1.moveUp()
        self.m2.moveUp()
        sleep(duration)

    def moveDown(self, duration=2000):
        self.m1.moveDown()
        self.m2.moveDown()
        sleep(duration)