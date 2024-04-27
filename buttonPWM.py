inPin1 = 40
inPin2 = 38
outPin = 7

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(inPin1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(inPin2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

from time import sleep

pwm1=GPIO.PWM(7,100)
pwm1.start(0)
dutyCycle=100
try:
	while True:
		button1 = GPIO.input(inPin1)
		button2 = GPIO.input(inPin2)
		print(button1)
		print(button2)
		if button1==True and dutyCycle>8:
			dutyCycle=dutyCycle-5
		elif button1==True and dutyCycle<8 :
			print('Lowest point reached')
		if button2==True and dutyCycle<100:
			dutyCycle=dutyCycle+5
		elif button2==True and dutyCycle>=100 :
			print('Highest point reached')
		pwm1.ChangeDutyCycle(dutyCycle)
		sleep(.1)


except KeyboardInterrupt:
	pwm1.stop()
	GPIO.cleanup()

