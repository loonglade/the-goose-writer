#!/usr/bin/env /root/the-goose-writer/venv/bin/python3
# Change the above line to reflect your home directory if needed

import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BCM)

BUTTON_PIN = 27

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shutdown(channel):
	os.system("shutdown -h now")

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=shutdown, bouncetime=200)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
