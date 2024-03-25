import sys
import time
import RPi.GPIO as GPIO

leds=5
osc1=23
osc2=22
osc3=25
pwm=12
pwm_freq=10
pwm_duty=80

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

if len(sys.argv) > 1:
	if sys.argv[1] == 'leds_on':
		GPIO.setup(leds, GPIO.OUT)
		GPIO.output(leds, GPIO.LOW)
	elif sys.argv[1] == 'leds_off':
		GPIO.setup(leds, GPIO.OUT)
		GPIO.output(leds, GPIO.HIGH)
	elif sys.argv[1] == 'osc1_on':
		GPIO.setup(osc1, GPIO.OUT)
		GPIO.output(osc1, GPIO.HIGH)
	elif sys.argv[1] == 'osc1_off':
		GPIO.setup(osc1, GPIO.OUT)
		GPIO.output(osc1, GPIO.LOW)
	elif sys.argv[1] == 'osc2_on':
		GPIO.setup(osc2, GPIO.OUT)
		GPIO.output(osc2, GPIO.HIGH)
	elif sys.argv[1] == 'osc2_off':
		GPIO.setup(osc2, GPIO.OUT)
		GPIO.output(osc2, GPIO.LOW)
	elif sys.argv[1] == 'osc3_on':
		GPIO.setup(osc3, GPIO.OUT)
		GPIO.output(osc3, GPIO.HIGH)
	elif sys.argv[1] == 'osc3_off':
		GPIO.setup(osc3, GPIO.OUT)
		GPIO.output(osc3, GPIO.LOW)
	elif sys.argv[1] == 'vib_on':
		GPIO.setup(pwm, GPIO.OUT)
		vib = GPIO.PWM(pwm, pwm_freq)
		vib.start(pwm_duty)
	elif sys.argv[1] == 'vib_off':
		GPIO.setup(pwm, GPIO.OUT)
		GPIO.output(pwm, GPIO.LOW)
	else:
		print("INVALID ARGUMENT")
else:
	print("INVALID ARGUMENT")
