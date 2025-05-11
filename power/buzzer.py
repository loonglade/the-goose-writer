import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define pin number and frequency for the piezo buzzer
BUZZER = 12
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2)
    waves = int(duration * noteFreq)
    for i in range(waves):
        GPIO.output(BUZZER, True)
        time.sleep(halveWaveTime)
        GPIO.output(BUZZER, False)
        time.sleep(halveWaveTime)

def play_fixed_frequency(frequency, duration, burst_count):
    """
    Function to create a burst of beeps at the specified frequency and duration.

    Args:
    - frequency (int): Frequency of the beep in Hz.
    - duration (float): Duration of each beep in seconds.
    - burst_count (int): Number of beeps in a burst.
    """
    for _ in range(burst_count):
        buzz(frequency, duration)
        time.sleep(0.2)  # delay between bursts

def main():
    try:
        # Create a burst of beeps that rings for three times, each 0.2 seconds long.
        play_fixed_frequency(700, 0.2, 3)

    except Exception as e:
        print("Exception:", str(e))
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
