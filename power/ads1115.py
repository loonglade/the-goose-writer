#!/usr/bin/env /root/venv/bin/python3

import time, os, board, busio, buzzer
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Create single-ended inputs on channels
chan_battery = AnalogIn(ads, ADS.P0)
chan_ref = AnalogIn(ads, ADS.P1)

# Known voltage reference value
known_ref_voltage = 2.29  # Change this value based on your voltage reference IC

while True:
    # Measure the ADC value and voltage for reference
    adc_value_ref = chan_ref.value
    voltage_ref = chan_ref.voltage

    # Calibrate the ADC using the voltage reference
    calibration_factor = known_ref_voltage / voltage_ref

    # Measure the ADC value and voltage for the battery
    adc_value_battery = chan_battery.value
    voltage_battery = chan_battery.voltage * calibration_factor

    print(f"Reference Voltage: {voltage_ref:.4f}V, Calibrated Battery Voltage: {voltage_battery:.4f}V")
    if float(f"{voltage_battery:.4f}") < 2.9:
        print("Shutting down in 2 minutes...")
        play_fixed_frequency(700, 0.5, 2)
        time.sleep(120)
        os.system("shutdown -h now")
    else:
        print(f"{voltage_battery:.4f}V")
    time.sleep(10)
