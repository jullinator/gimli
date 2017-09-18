from nanpy import ArduinoApi, SerialManager
from time import sleep

conn = SerialManager(device='/dev/ttyACM0')

a = ArduinoApi(connection = conn)
ledpin = 13
a.pinMode(ledpin, a.OUTPUT)

def blink():
	a.digitalWrite(ledpin, a.HIGH)
	sleep(0.2)
	a.digitalWrite(ledpin, a.LOW)
	sleep(0.2)	




