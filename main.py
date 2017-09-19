from nanpy import ArduinoApi, SerialManager
from dc import Motor, MotorController
from servo import Servo, ServoController

conn = SerialManager(device='/dev/ttyACM0')

a = ArduinoApi(connection = conn)

m1 = Motor(2,3,4,a)
m2 = Motor(5,6,7,a)
dc = MotorController(m1,m2)

#s1 = Servo(8)
#s2 = Servo(9)

#serv = ServoController(s1, s2)
