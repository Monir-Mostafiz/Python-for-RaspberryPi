import RPi.GPIO as GPIO

cont = 'y'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

while cont == 'y':
	GPIO.output(7,0)
	GPIO.output(8,0)
	GPIO.output(10,0)
	GPIO.output(11,0)
	decimal = int(input("Enter Your Decimal Number: "))
	if decimal<16:
		if decimal>=8:
			decimal=decimal-8
			GPIO.output(7,1)
		if decimal>=4:
			decimal=decimal-4
			GPIO.output(8,1)
		if decimal>=2:
			decimal=decimal-2
			GPIO.output(10,1)
		if decimal>=1:
			GPIO.output(11,1)
	else:
		print("The number is greater than 4 bit")

	cont = input("DO you want to continue: ")

GPIO.cleanup()
