#!/usr/bin/env /root/venv/bin/python3
import os
import fileinput
import digitalio
import busio
import board
from datetime import datetime, time, timedelta
from PIL import Image
from adafruit_epd.ssd1680 import Adafruit_SSD1680
import logging

# Set up logging
logging.basicConfig(filename='/root/eink/eink.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # Change 'filename' value to reflect your home directory if needed

CONFIG_PATH = '/root/eink/config.txt' # Change to reflect your home directory if needed

def parse_date(date_str):
    month, day = map(int, date_str.split('_'))
    year = datetime.now().year
    return datetime(year, month, day)

def get_current_image_path():
    today = datetime.now()
    directory = '/root/eink/eink_images' # Change to reflect your home directory if needed
    logging.info(f"Listing files in directory: {directory}")
    logging.info(f"Files in directory: {os.listdir(directory)}")
    
    suitable_images = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            parts = filename.split('-', 2)
            if len(parts) < 3:
                logging.warning(f"Skipping {filename} due to incorrect naming format.")
                continue
            date_range, description = parts[0:2], parts[2]
            start_date, end_date = date_range
            try:
                start = parse_date(start_date)
                end = parse_date(end_date)
                logging.info(f"Parsed start date: {start}, end date: {end}")
                # from 00:00:00 of the start date to 23:59:59 of the end date
                start = datetime.combine(start.date(), time.min) if start.time() == time.min else start
                end = datetime.combine(end.date(), time.max) if end.time() == time.max else end
            except ValueError as e:
                logging.error(f"Error parsing dates in {filename}: {e}")
                continue
            # year wrap-around
            if end < start:
                end = end.replace(year=end.year + 1)
                logging.info(f"Adjusted end date to next year: {end}")
            end_inclusive = end + timedelta(days=1)
            if start <= today < end_inclusive:
                logging.info(f"Found suitable image for today: {filename}")
                suitable_images.append((os.path.join(directory, filename), start, end))
            else:
                logging.info(f"Skipping {filename} as today's date ({today}) is not within its date range ({start} to {end}).")
        else:
            logging.info(f"Skipping non-PNG file: {filename}")
    if suitable_images:
        suitable_images.sort(key=lambda x: x[1])
        logging.info(f"Selected image: {suitable_images[0][0]}")
        return suitable_images[0][0]
    else:
        logging.info("No suitable image found for display.")
        return None

def read_last_image():
    try:
        with open(CONFIG_PATH, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                if 'LastDisplayedImage=' in line:
                    return line.split('=')[1].strip()
    except FileNotFoundError:
        pass
    return None

def write_last_image(image_name):
    found = False
    for line in fileinput.input(CONFIG_PATH, inplace=True):
        if 'LastDisplayedImage=' in line:
            print(f'LastDisplayedImage={image_name}', end='\n')
            found = True
        else:
            print(line, end='')
    if not found:
        with open(CONFIG_PATH, "a") as file:
            file.write(f'LastDisplayedImage={image_name}\n')
    fileinput.close()

# E-ink PINout
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D25)
srcs = None
rst = digitalio.DigitalInOut(board.D17)
busy = digitalio.DigitalInOut(board.D24)
display = Adafruit_SSD1680(122, 250, spi,
    cs_pin=ecs,
    dc_pin=dc,
    sramcs_pin=srcs,
    rst_pin=rst,
    busy_pin=busy,
)
display.rotation = 1

image_path = get_current_image_path()
if image_path:
    image = Image.open(image_path)
    image_ratio = image.width / image.height
    screen_ratio = display.width / display.height
    if screen_ratio < image_ratio:
        scaled_width = image.width * display.height // image.height
        scaled_height = display.height
    else:
        scaled_width = display.width
        scaled_height = image.height * display.width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)
    x = scaled_width // 2 - display.width // 2
    y = scaled_height // 2 - display.height // 2
    image = image.crop((x, y, x + display.width, y + display.height)).convert("RGB")
    last_image = read_last_image()
    if last_image != os.path.basename(image_path):
        display.image(image)
        display.display()
        write_last_image(os.path.basename(image_path))
        logging.info(f"Updated display with {os.path.basename(image_path)}")
    else:
        logging.info("Image is the same as last displayed, skipping display.")
else:
    logging.info("No suitable image found for display.")
