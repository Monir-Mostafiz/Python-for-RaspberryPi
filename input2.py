inPin = 40
x=[7,8,10,11]

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin,GPIO.IN)
for i in x:
	GPIO.setup(i,GPIO.OUT)

from time import sleep

try:
	while True:
		inVal=GPIO.input(inPin)
		print(inVal)
		sleep(.5)
		if inVal==1:
			for i in x:
				GPIO.output(i,True)
				print(i)
				sleep(1)
		for i in x:
			GPIO.output(i,False)

except KeyboardInterrupt:
	GPIO.cleanup()

