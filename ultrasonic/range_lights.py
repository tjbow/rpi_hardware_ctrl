import RPi.GPIO as GPIO
import time

def getDistance():

	# Configuration
	print("Setting up...")
	GPIO.setmode(GPIO.BCM)

	# 330 Ohm resisters from ground rail to the short side of leds
	# wires from pin n on RPi to the long side of leds
	
	TRIG = 27
	ECHO = 22
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	GREEN = 18
	YLW = 23
	RED = 24
	GPIO.setup(GREEN, GPIO.OUT)
	GPIO.setup(YLW, GPIO.OUT)
	GPIO.setup(RED, GPIO.OUT)

	ALARM = 17
	GPIO.setup(ALARM, GPIO.OUT)
	
	GPIO.output(TRIG,False)
	time.sleep(2)
	print("Ready!")

	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			pass
		pulse_start = time.time()

		while GPIO.input(ECHO) == 1:
			pass
		pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150

		if distance <= 15.0:
			print("BACK AWAY!")
			GPIO.output(RED, GPIO.HIGH)
			GPIO.output(YLW, GPIO.LOW)
			GPIO.output(GREEN, GPIO.LOW)
			GPIO.output(ALARM, GPIO.HIGH)
		elif distance <= 40.0:
			GPIO.output(YLW, GPIO.HIGH)
			GPIO.output(RED, GPIO.LOW)
			GPIO.output(GREEN, GPIO.LOW)
			GPIO.output(ALARM, GPIO.LOW)
		else:
			GPIO.output(GREEN, GPIO.HIGH)
			GPIO.output(YLW, GPIO.LOW)
			GPIO.output(RED, GPIO.LOW)
			GPIO.output(ALARM, GPIO.LOW)

		print ("Distance: %.1f cm" % distance)
		time.sleep(0.4)

if __name__ == '__main__':
	try:
		getDistance()
 
	except KeyboardInterrupt:
		GPIO.cleanup()
