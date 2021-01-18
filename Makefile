#####################################################################
## --chip {auto, esp8266, esp32}]                                  ##
## --port PORT                                                     ##
## --baud BAUD                                                     ##
## --before {default_reset, no_reset, no_reset_no_sync}            ##
## --after {hard_reset, soft_reset, no_reset}                      ##
## --no-stub                                                       ##
## --trace                                                         ##
## --override-vddsdio [{1.8V, 1.9V, OFF}]                          ##
#####################################################################
## load_ram, dump_mem, read_mem, write_mem, write_flash, run,      ##
## image_info, make_image, elf2image, read_mac, chip_id, flash_id, ##
## read_flash_status, write_flash_status, read_flash,              ##
## verify_flash, erase_flash, erase_region, version                ##
#####################################################################

PORT = /dev/ttyUSB0
#PORT = /dev/ttyUSB1

#BAUDRATE = 460800
BAUDRATE = 115200
#BAUDRATE = 57600
#BAUDRATE = 9600

#CHIP = esp8266
CHIP = esp32

#FIRMWARE = esp8266-1m-20200902-v1.13.bin
#FIRMWARE = esp32spiram-idf3-20200902-v1.13.bin
FIRMWARE = esp32-idf3-20200902-v1.13.bin

setup_dev:
	sudo apt-get install git wget flex bison gperf python3 python3-pip python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util
	sudo apt-get install esptool
	sudo apt install picocom
	pip3 install -r requirements.txt

info:
	esptool --port $(PORT) --before default_reset --baud $(BAUDRATE) --after hard_reset read_flash_status


ports:
	dmesg | grep tty

permission:
	sudo chmod +x $(PORT)
	sudo chmod +x venv/lib/python3.8/site-packages/esptool.py

flash_info:
	esptool --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) read_flash_status

backup:
	esptool --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) 0x00000 0x400000 backup.bin


# Prepare for micropiton
micropython_bin: # 1M of flash # other bin's: http://micropython.org/download/esp8266/
	rm -rf $(FIRMWARE)
	wget http://micropython.org/resources/firmware/$(FIRMWARE)

erase_flash:
	esptool --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) erase_flash

repl:
	picocom $(PORT) -b$(BAUDRATE)
	#minicom --device $(PORT) -b $(BAUDRATE)

upload:
	ampy --port $(PORT) put main.py

run:
	ampy --port $(PORT) run main.py
get:
	ampy --port $(PORT) get main.py

burn_micro:	#default baud rate 115200
	esptool --chip $(CHIP) --port $(PORT) --baud 460800 write_flash -z 0x1000 $(FIRMWARE)

# Work with esp
burn:
	esptool --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) write_flash 0x00000 project.bin

#CH340 drivers
get_CH340_lin:
	wget https://sparks.gogo.co.nz/assets/_site_/downloads/CH340_LINUX.zip

get_CH340_win:
	wget https://sparks.gogo.co.nz/assets/_site_/downloads/CH34x_Install_Windows_v3_4.zip

get_CH340_mac:
	wget https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver/blob/master/CH34x_Install_V1.5.pkg
