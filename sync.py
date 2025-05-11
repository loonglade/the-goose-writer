#!/usr/bin/env /root/venv/bin/python3

import subprocess, os, time
import RPi.GPIO as GPIO
from power.buzzer import *

GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 22
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def copy(channel):
    local_folder = "/root/writings" # change for your local folder path
    remote_folder = "gdrive:writings" # change for your remote folder path

    command = f"rclone copy {local_folder} {remote_folder}"

    try:
        os.system("ifup wlan0")
        subprocess.run(command, shell=True, check=True)
        play_fixed_frequency(650, 0.01, 3)
        os.system("ifdown wlan0")
    except subprocess.CalledProcessError:
        print("An error occurred during sync.")

GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=copy, bouncetime=200)

try:
    while True:
        time.sleep(1)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()
