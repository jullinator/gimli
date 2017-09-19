from nanpy import Servo as _Servo
from time import sleep

serv = _Servo()

class Servo():
    def __init__(self, pin):
        self.servo = _Servo()
        self.servo.attach(pin)

    def moveBy(self, amount):
        pos = self.servo.read()
        pos+=amount
        self.servo.write(pos)
    def moveTo(self, pos):
        self.servo.write(pos)


class ServoController():
    def __init__(self, fleft, fright):
        self.fleft = fleft
        self.fright = fright

