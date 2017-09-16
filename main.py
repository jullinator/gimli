from nanpy import ArduinoApi
from dc import Motor, MotorController

a = ArduinoApi()

m1 = Motor(2,3,4,a)
m2 = Motor(5,6,7,a)
dc = MotorController(m1,m2)

dc.moveUp()
dc.moveDown()
