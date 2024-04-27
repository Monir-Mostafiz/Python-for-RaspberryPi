rBut=40
gBut=36
bBut=38

rLed=7
gLed=8
bLed=10

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rBut,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gBut,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bBut,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rLed,GPIO.OUT)
GPIO.setup(gLed,GPIO.OUT)
GPIO.setup(bLed,GPIO.OUT)

rPwm=GPIO.PWM(rLed,100)
gPwm=GPIO.PWM(gLed,100)
bPwm=GPIO.PWM(bLed,100)

rDutyCycle = 100
gDutyCycle = 100
bDutyCycle = 100

rPwm.start(rDutyCycle)
gPwm.start(gDutyCycle)
bPwm.start(bDutyCycle)

Dummy = 0

from time import sleep

try:
	while True:
		readR=GPIO.input(rBut)
		readB=GPIO.input(bBut)
		readG=GPIO.input(gBut)

		if readR == True and rDutyCycle>=1:
			rDutyCycle=rDutyCycle-1
			if rDutyCycle==0:
				rDutyCycle=100
				while GPIO.input(rBut)==1: #break when value reached 100
					Dummy=0
		rPwm.ChangeDutyCycle(rDutyCycle)

		if readG == True and gDutyCycle>=1:
			gDutyCycle=gDutyCycle-1
			if gDutyCycle==0:
				gDutyCycle=100
				while GPIO.input(gBut)==1: #break when value reached 100
					Dummy = 0
		gPwm.ChangeDutyCycle(gDutyCycle)

		if readB == True and bDutyCycle>=1:
			bDutyCycle=bDutyCycle-1
			if bDutyCycle==0:
				bDutyCycle=100
				while GPIO.input(bBut)==1: #break when value raeched 100
					Dummy = 0

		bPwm.ChangeDutyCycle(bDutyCycle)

		print("Red=",100-rDutyCycle,"Green=",100-gDutyCycle,"Blue",100-bDutyCycle)
		sleep(.1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("programe is closed")
	rPwm.stop()






























