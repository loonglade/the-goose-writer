# <div align="center"> The Goose Writer </div>

| ![Front](https://github.com/loonglade/the-goose-writer/blob/main/front.png) | ![Side](https://github.com/loonglade/the-goose-writer/blob/main/side.png) |
|---|---|

### Features

- A 7" LCD Display as the main display
- Runs on a Raspberry Pi Zero W for ease of configuration and low power consumption
- 14,000 mAh battery pack (4x 18650 3500mAh)
- 2.13" ePaper display that displays the image that reflects the current [microseason](https://hinodeya-japan.com/blogs/a-glimpse-of-yesterday/discovering-the-sekki-a-comprehensive-list-of-japans-24-mini-seasons) as traditionally observed by Japan
- A button for safe shutdowns, another for cloud syncing and one last for complete power cut off
- ADC module that detects low battery voltage and initiates a safe shutdown
- Piezo buzzer that alerts the user to different things
- And a few more little things...

I like to build things, it tickles the part of my brain that likes to solve problems that sometimes don't even need answers. My spouse knows that about me more than anyone else. She, on the other hand, enjoys reading and writing her heart out. That's her way of tickling that part of her brain.

I feel that the best way, in my experience, to learn is to jump straight into a project. I've always been interested in technology, especially computers and in the recent years I've discovered the ultimate rabbit hole of Electronics, Micro-controllers and Single-board computers. I wanted to learn about this newly discovered world by creating something.

I thought, how could I create something useful and at the same time learn about electronics. Building something for someone I love has always given me the most ambition to build it and finish it to the best of my abilities. So that's when the idea of creating a Distraction-Free Writing Device came about.

In short, this little device does what it's named after. It's a device used as a tool to write without distractions. Somewhere between a full-fledge computer and a typewriter. 

5. It's quicker than writing with pen and paper
6. Doesn't require paper like a typewriter would
7. No distractions from an internet-enabled computer

As you may have guessed, this device doesn't have internet, or at least not in the conventional sense. That's by design. There are a few brands that offer those devices, hence why they can charge absurdly high prices for what it actually does; Monopoly, exclusively, novelty. Here's a short list of some of them, to give you an idea:

**Commercial**
- [Pomera DM250](https://www.kingjim.co.jp/pomera/dm250/)
- [Alphasmart devices](https://en.wikipedia.org/wiki/AlphaSmart)
- [FreeWrite devices](https://getfreewrite.com/)

**Other Writing Devices**

- [FeatherQuill](https://www.instructables.com/FeatherQuill-34-Hours-of-Distraction-Free-Writing/)
- [Kobo Writer](https://github.com/olup/kobowriter)
- [Mythic Computer](https://www.mythic.computer/)
- [Scripto](https://cl5944.myportfolio.com/product-service-scripto)
- [ZeroWriter](https://hackaday.io/project/193902-zerowriter)
- [Pikensu](https://penkesu.computer/)
- [Celestia](https://github.com/DPHAD/Celestia-Retro-PC)

The Alphasmart company was defunct in 2005, and the domain name was bought by FreeWrite, which as it seems, have a market monopoly of Distraction-Free Writing Devices. I thought of simply buying an Alphasmart, but I, nor my spouse, enjoy typing on a rubber-dome keyboard (your usual cheap, mushy/spongy keys). I found someone [on youtube](https://www.youtube.com/watch?v=fsmo3oOSj0U) that succeeded in replacing an Alphasmart Neo keyboard for a mechanical keyboard. I thought about it for a while, but I didn't have the know-how to do such an operation at the time. I also feel like I wanted to build something from scratch, to see and feel the entire process. Processes from start to finish have their own flavours that makes you feel something special. It changes you in some sense. I wanted to go through it and feel that process.

Below is a list of components I bought and used. I've also included a list of the tools I used for the project.

### Components list (prices in CAD)

| Components                               | Price (Taxes and shipping included) | Link                                                                  | Notes                                                                   |
| ---------------------------------------- | ----------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Raspberry Pi Zero W                      | 21                                  | [link](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)<br> | From this link, select your region and a list of suppliers will show up |
| 7" LCD Display with control board        | 33.85                               | [link](https://www.aliexpress.com/item/1005004205792259.html)         |                                                                         |
| BMS                                      | 3.49                                | [link](https://www.aliexpress.com/item/4001132144039.html)            |                                                                         |
| Foldable laptop stand                    | 5.04                                | [link](https://www.aliexpress.com/item/1005005562013232.html)         | 2 pcs                                                                   |
| DS3231 RTC module                        | 3.14                                | [link](https://www.aliexpress.com/item/1005003750606506.html)         |                                                                         |
| Battery holders                          | 6.78                                | [link](https://www.aliexpress.com/item/1005004607036729.html)         | Pack of 100 pcs                                                         |
| Metal button                             | 1.84                                | [link](https://www.aliexpress.com/item/1005004636725995.html)         |                                                                         |
| LiitoKala 18650 batteries 3.7V @ 3500mAh | 34.59                               | [link](https://www.aliexpress.com/item/32810252344.html)              | Ended up using only 4                                                   |
| USB-A to Micro-USB                       | 3.88                                | [link](https://www.aliexpress.com/item/1005003745142322.html)         | Male-to-Male - 90 degrees angled - 2 pcs                                |
| USB-C to USB-C                           | 5.31                                | [link](https://www.aliexpress.com/item/1005005373420180.html)         | Male-to-Male - Short 5cm long                                           |
| Micro-USB Male to USB-C Female           | 7.90                                | [link](https://www.aliexpress.com/item/1005004622194467.html)         | 2 pcs                                                                   |
| Mini-HDMI to Mini-HDMI                   | 12.99                               | [link](https://www.aliexpress.com/item/4000014554460.html)            | Male-to-male - Built using different parts in that listing              |
| WeAct 2.13" ePaper display               | 9.95                                | [link](https://www.aliexpress.com/item/1005004644515880.html)         | Black, White and Red capable                                            |
| ADS1115 ADC Module                       | 3.41                                | [link](https://www.aliexpress.com/item/32817162654.html)              |                                                                         |
| NC push buttons                          | 2.71                                | [link](https://www.aliexpress.com/item/1005004066208352.html)         | 6 pcs - Only used 2                                                     |
| Micro SD extension cable                 | 3.72                                | [link](https://www.aliexpress.com/item/1005004149375152.html)         | 25cm                                                                    |
| Piezo Buzzer                             | 3.30                                | [link](https://www.aliexpress.com/item/4000148640191.html)            | 10 pcs - Only used 1                                                    |
*TL;DR: You can build one for around $120 USD if you already have a keyboard*

### Tools and consumables

- USB Power meter
- Multimeter
- Micro-SD to USB-A/USB-C adapter
- Soldering iron, solder, flux and iron tip cleaner
- Breadboard (for testing wire connections)
- Computer repair screwdriver set
- Drill + drill bits
- Gorilla glue
- Perforated boards
- Saw blades
- Electrical tape or heat shrink tubing
- Velcro
- Bolts and Screws

<br>

## Hardware
*Step-by-step guide on how to wire every component*

Direction of wiring in this section is from the component's PIN to the corresponding Raspberry Pi's PIN.
	e.g.: SPEAKER PIN -> RPI PIN

### Batteries
I will directly quote [Cameron Coward](https://serialhobbyism.com/) in his [FeatherQuill](https://www.instructables.com/FeatherQuill-34-Hours-of-Distraction-Free-Writing/) build to preface this battery section:

**Li-ion batteries are potentially dangerous! They can catch fire or explode! I am not even the slightest bit liable if you kill yourself or burn down your house. Don't take my word for how to safely do this—do your research!**

1. Scratch the Positive and Negative terminals of each of the 18650 battery cell as it facilitates the binding of solder and flux.
2. Apply Flux to each terminal and solder all the positive terminals together and all the negative terminals together using at least awg22 gauge wire. This ensures that the voltage of the now battery bank remains at 3.7v but adds up all the separate cell's current. In my case, I'd get the theoretical 17500mAh (5x 3500mA) at 3.7v. Make sure you use a broad solder tip and apply high heat for the shortest amount of time. (Proceed with extreme care as this is very dangerous. If you don't know what you're doing or you hesitate, then don't proceed. I'm not responsible for any of the damage you may cause from this procedure). Make sure all your solders are strong and solid.
3. Solder the positive terminal of the battery bank to the positive terminal of the BMS. Solder the negative terminal of the battery bank to the negative terminal of the BMS.
4. Charge up your new battery pack to 100% and monitor each cell's temperature. 

### ePaper display (ssd1680)

	BUSY -> GPIO 24 (PIN 18)
	RES (Reset) -> GPIO 17 (PIN 11)
	D/C (Data/Command) -> GPIO 25 (PIN 22)
	CS (Chip Select) -> GPIO 8 (SPI0_CE0 - PIN 24)
	SCL (Clock) -> GPIO 11 (SPI0_SCLK - PIN 23)
	SDA (Data) -> GPIO 10 (SPI0_MOSI - PIN19)
	GND (Ground) -> GND (Any Ground PIN)  
	VCC (3.3-5V) -> Any 3.3V PIN

### [ADS1115](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython)

	Diagram (ADS1115 to RPI):
		VDD (3.3v) -> 3.3v power (PIN 1)
		GND -> GND (Any Ground PIN)
		SCL -> GPIO 3 (PIN 5)
		SDA ->  - GPIO 2 (PIN 3)
		Connect the **10kΩ resistor** to the **positive terminal of the battery pack.**
		Connect the **other end** of the **10kΩ resistor** to **A0 on the ADS1115**.
		Also at this junction (where the 10kΩ resistor meets A0), connect one end of the **6.8kΩ resistor**.
		Connect the **other end** of the **6.8kΩ resistor** to the **negative terminal (ground)** of the battery pack.
	*Quick tip: If you accidentally mix up the resistors and can't remember which is which, you can identify them by comparing the stripe patterns on each resistor to others in the same batch.

### Switch #1 (clean shutdown)

	One PIN -> GPIO 27 (PIN 13)
	The other PIN -> GND (Any Ground PIN)

### Switch #2 (Upload to cloud)

	One PIN -> GPIO 22 (PIN 15)
	The other PIN -> GND (Any Ground PIN)

### Fan (tiny 1cm x 1cm)

	1. Attach a 150 ohm resistor at the end of the power wire (Resistance will depend on the model you bought and at what speed you want the blades to spin)
	2. Solder the other end of that resistor to any 3.3v pin on the RPI
	3. Solder ground wire to any ground pin on the RPI

### [DS3231](https://tinyurl.com/shj22d9t)

	VDD (3.3v) -> 3.3v power (PIN 17)
	GND -> GND (Any Ground PIN)
	SCL (C) -> GPIO 16 (PIN 36)
	SDA (D) -> GPIO 26 (PIN 37)

### Buzzer
	Any of the two PINs of the buzzer > GPIO 12 (PIN 32)
	The other PIN > GND (Any Ground PIN)
	
### Case

I made mine out of thin plywood, so I don't have 3D models made but the dimensions that my case came out to was *8.5 x 7.5 x 1.25 (in inches)*. It can definitely be a thinner, lighter and prettier case, but I didn't mind it for my first go at a project like this.

<br>

## Software
*Instructions on all Software related parts*

[Install DietPi](https://dietpi.com/docs/install/)
The commands in this section assumes you're logged as root. If you're NOT logged as root, you may need to prefix each command with "sudo" or opening a new shell as root using "sudo -i" (recommended for the installation process).**

### DietPi setup

1. WiFi
	1. dietpi-config > Network Options: Adapters > Onboard WiFi: ON
	2. dietpi-config > Network Options: Adapters > WiFi > 
		1. Scan (this will allow you to configure your network)
		2. Auto Reconnect: OFF (keep off)
		3. Apply > OK (Applies all changes)
	3. dietpi-config > Network Options: Misc > Boot wait for network: OFF
3. Go through the initial DietPi setup installation
4. Update system using the "dietpi-update" command
5. Adjust time to your timezone
	- dietpi-config > Language/Regional Options > Timezone
6. Auto-login (optional)
	- dietpi-config > AutoStart Options > Automatic login (under Local Terminal) > Choose your user (Root is not recommended)
7. Enable SPI and I2C
	- dietpi-config > Advanced Options > change SPI State and I2C State to ON
8. Bluetooth off (if you're not using a bluetooth keyboard)
	- dietpi-config > Advanced Options > Bluetooth: OFF
9. Add or uncomment "hdmi_force_hotplug=1" in /boot/config.txt

### Pre-Requisites

1. apt install python3-venv
2. apt-get install python3-pip
3. apt install --upgrade python3-setuptools pip
4. python3 -m venv venv
5. source venv/bin/activate
6. cd ~
7. apt-get install -y build-essential
8. pip3 install --upgrade adafruit-python-shell
9. wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
10. pip3 install adafruit-blinka
11. apt-get install python3-dev
12. venv/bin/python3 raspi-blinka.py
13. pip3 install RPi.GPIO


### Git repository

1. Install Git if you haven't done so already
	- sudo apt install git-all
2. clone repo
	- git clone https://github.com/loonglade/the-goose-writer.git
3. cd the-goose-writer


### [Tmux](https://github.com/tmux/tmux/wiki) (optional -> only needed if you get the ePaper display)

In this project, Tmux is mainly used, at least by me, for its status bar to show the time on the right and the current microseason in the center. The `.tmux.conf` file should sit in either the root folder or your home folder, [depending on which route you choose](https://www.linux.org/threads/when-to-work-as-root-when-to-work-as-a-system-user.4136/). It is generally not recommended to work as root. However, this is a simple writing device that is not connected to the internet for the most part (besides when syncing of files is in process). Nevertheless, if you choose to use this device as root - tread carefully.

### [ePaper display](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

I got the 2.13" ePaper display (SSD1680) working using CircuitPython's [Blinka](https://github.com/adafruit/Adafruit_Blinka) and its [EPD](https://github.com/adafruit/Adafruit_CircuitPython_EPD), [DisplayIO](https://github.com/adafruit/Adafruit_Blinka_Displayio) and [ssd1680 drivers](https://github.com/adafruit/Adafruit_CircuitPython_SSD1680). I've followed [this guide](https://docs.circuitpython.org/projects/ssd1680/en/latest/index.html) and [this guide](https://learn.adafruit.com/2-13-in-e-ink-bonnet/usage) to get started. If you chose to use the device as root, you won't have to change the paths. Otherwise, you will need to change the `filename` and `directory` variable values to reflect your home directory.

*make sure SPI is enabled in configs (dietpi-config > Advanced options > SPI State (ON)*
	apt-get install -y libjpeg-dev zlib1g-dev libpng-dev libtiff-dev libopenjp2-7 libopenjp2-7-dev libxcb1
	pip3 install pillow
	pip3 install adafruit-circuitpython-epd

Create a Cron job:
	crontab -e
	add this line:
		@reboot /root/the-goose-writer/venv/bin/python3 /root/the-goose-writer/eink/eink.py # Change to your venv dir and eink.py location to reflect your user's home path

If you aren't logged in as root, add the current user to the GPIO and SPI groups:
	sudo usermod -aG i2c,spi,gpio $USER

*logout, log back in for permissions to take effect

### [Wordgrinder](http://cowlark.com/wordgrinder/index.html) (loads on boot)

	1. nano ~/.bashrc
	2. paste this after the tmux code: wordgrinder
	3. save and exit
	4. next time you reboot, wordgrinder will open automatically

### ADS1115

*make sure I2C is enabled in configs (dietpi-config > Advanced options > I2C State (ON)*
- pip3 install adafruit-circuitpython-ads1x15
- You'll have to use a multimeter to calibrate the output. Change the line "known_ref_voltage = 2.29" in the file ads1115.py in order to get the true output value. After changing the value, run the ads1115.py script and check the returned value. It will be trial and error until you get a value that's very close to the actual voltage measurement.
1. chmod +x /root/the-goose-writer/power/ads1115.py # change path for where your ads1115.py is
2. nano /etc/systemd/system/low_battery.service
3. paste this in there:
```
[Unit]
Description=Shutdown on low battery
After=multi-user.target

[Service]
Type=simple
ExecStart=/root/the-goose-writer/venv/bin/python3 /root/the-goose-writer/power/ads1115.py # Change this accordingly
StandardOutput=journal
StandardError=journal
Restart=always
# User=Dietpi # Uncomment and change username if you're NOT running this service as root

[Install]
WantedBy=multi-user.target
```
4. systemctl enable low_battery.service
5. systemctl start low_battery.service
6. reboot
7. test the button


### [TLP (Battery Optimization)](https://linrunner.de/tlp/index.html)

1. apt install tlp && tlp start
2. tlp true
3. systemctl enable tlp.service
4. systemctl start tlp.service

### DS3231

1. apt-get install i2c-tools
2. nano /boot/config.txt
3. add this line: dtoverlay=i2c-gpio,bus=3,i2c_gpio_sda=26,i2c_gpio_scl=16
4. save and close
5. reboot
6. after rebooted: ls /dev/i2c*
	you should see the new I2C bus listed
7. nano /etc/rc.local
8. paste this:
	#!/bin/sh
	modprobe rtc-ds1307
	sleep 2
	echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-3/new_device
	hwclock -s
9. nano /etc/systemd/system/rc-local.service
10. paste the following:
```
[Unit]
Description=/etc/rc.local Compatibility
ConditionPathExists=/etc/rc.local

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99

[Install]
WantedBy=multi-user.target
```
11. save and exit
12. chmod +x /etc/rc.local
13. systemctl daemon-reload
14. systemctl enable rc-local
15. systemctl start rc-local
16. reboot
17. set the time with this command: date 101814002023.00
	The format should be MMDDhhmmYYYY.ss (Month, Day, Hour, Minute, Year, Second)
18. hwclock -w
19. Verify that the current date and time on both the system time and the hardware clock (ds3231) match by typing:
	1. date
	2. hwclock -r
20. Install tmux (apt install tmux)
21. nano ~/.bashrc
22. paste this:
```
if [ -z "$TMUX" ]; then
 exec tmux
fi
```
23. save and exit
24. source ~/.bashrc
25. reboot and you should see the time at the bottom

### Switch #1 (clean shutdown - GPIO27) 

1. chmod +x /root/the-goose-writer/power/shutdown_button.py # change path for where your shutdown_button.py is if needed
2. nano /etc/systemd/system/shutdown_button.service
3. paste this in there:
```
[Unit]
Description=Shutdown button service
After=multi-user.target

[Service]
Type=simple
ExecStart=/root/the-goose-writer/venv/bin/python3 /root/the-goose-writer/power/shutdown_button.py # Change this accordingly
StandardOutput=journal
StandardError=journal
Restart=always
# User=Dietpi # Uncomment and change username if you're NOT running this service as root

[Install]
WantedBy=multi-user.target
```
4. systemctl enable shutdown_button.service
5. systemctl start shutdown_button.service
6. reboot
7. Test out the button


### Switch #2 (upload to google drive)

1. Install [rclone](https://rclone.org/):
	curl https://rclone.org/install.sh | bash
2. configure rclone:
	1. rclone config
	2. n/s/q> n         # New
	3. name>gdrive      # Gdrive is an example name
	4. Storage>drive        # for google drive
	5. client_id>       # Can be left blank
	6. client_secret>   # Can be left blank
	7. scope> 3          # Select the scope use used in step 2
	8. root_folder_id>  # Can be left blank
	9. y/n> n            # Edit advanced config, n
	10. y/n> n            # authenticate rclone with remote
	11. Copy the `rclone authorize "drive"` link and paste it into your main computer's terminal.
	12. Copy the link (e.g.: http://127.0.0.1:53682/auth?state=NUMBER) and paste it into your main computer's browser (it might automatically open the browser to that page for you). You must login or be logged into the google drive account you wish to upload your writings to.
	13. Follow the prompts in the browser. Once you get the message that says: "Success! All done. Please go back to rclone." go back to your main computer's terminal and copy the long code between the "--->" and "<---End paste".
	14. Go to your Pi's terminal and paste the long code.
	15. y/n> n          # Configure as shared drive
	16. y/e/d> y       # Keep (name of remote) remote?
	17. e/n/d/r/c/s/q> q       # Quit configuration. You're done!

3. chmod +x /root/the-goose-writer/sync.py # change path for where your sync.py is
	1. Modify the `local_folder` and `remote_folder` path inside the sync.py file if needed
4. nano /etc/systemd/system/sync.service
5. paste this in there:
```
[Unit]
Description=Sync button service
After=multi-user.target

[Service]
Type=simple
ExecStart=/root/the-goose-writer/venv/bin/python3 /root/the-goose-writer/sync.py # Change these accordingly
StandardOutput=journal
StandardError=journal
Restart=always
# User=Dietpi # Uncomment and change username if you're NOT running this service as root

[Install]
WantedBy=multi-user.target
```
6. systemctl enable sync.service
7. systemctl start sync.service
8. reboot
9. Test out the button


And that's it! You should now have a functional writing device! If there are any issues, please file a github issues and I'll do my best to help.

---

<br>

### Lessons learned from this build:
- I think that give or take 7 hours of battery life is good, but not great. I'd probably try to spend more time on increasing it in the next build.
- I'd use a 4 or 5" display instead of 7" or perhaps even an ePaper display or those old Monochrome TFT LCD
- Raspberry Pis are notorious for draining power even when the power is off, so knowing that I've researched extensively on how I would implement a solution to negate this as knowing ultimately very little about electronics, I didn't know how to do that. I ended up picking up a latching relay, which act basically like a switch to turn on/off your entire setup. It wasn't until I received all shipments and trying to put pieces together that I realized that the BMS, onto which everything is passing through, already did that on its own. I didn't need the latching relay. Simply holding the button of the BMS will completely cut off power and double pressing it will start it up. I've spent an ungodly amount of time figuring this out...
- Tiny SSD > MicroSD card (corruption avoidance)
	- https://www.amazon.ca/Adapter-ELUTENG-Converter-Portable-External/dp/B07VP2WH73/ref=pd_bxgy_img_sccl_1/144-2949718-3884752?psc=1
	- https://www.amazon.ca/Dogfish-Msata-Internal-Solid-SSD/dp/B07GNYZDPW/ref=sr_1_7?keywords=16gb%2Bssd
	- https://www.amazon.ca/Aceele-Extended-Thunderbolt-Compatible-More-Black/dp/B07VPTRXN1/ref=sr_1_6?keywords=usb+hub+micro+usb

### References 
- [Prose: The distraction-free, e-ink laptop that should exist](https://medium.com/this-should-exist/prose-a-distraction-free-e-ink-laptop-for-thinkers-writers-4182a62d63b2)
- [How to build a low-tech internet](https://solar.lowtechmagazine.com/2015/10/how-to-build-a-low-tech-internet)
- [The computer built to last 50 years](https://ploum.net/the-computer-built-to-last-50-years/)
- [Saving power on the Raspberry Pi Zero](https://www.jeffgeerling.com/blogs/jeff-geerling/raspberry-pi-zero-conserve-energy)


#### <img src="https://www.file-extensions.org/imgs/app-icon/128/10409/bitcoin-core-icon.png" width="20" height="20"> Donations </img>
If this guide helped you build a writing device of your own, please consider donating some Bitcoin :)

bitcoin:bc1q6nu6347k3n077sscjntk949namnulrrpshz4j4
