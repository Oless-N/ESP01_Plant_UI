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
#PORT = /dev/cu.usbserial-0001

#BAUDRATE = 460800
BAUDRATE = 115200
#BAUDRATE = 57600
#BAUDRATE = 9600

CHIP = esp8266
#CHIP = esp32

FIRMWARE = esp8266-1m-20200902-v1.13.bin
#FIRMWARE = esp32spiram-idf3-20200902-v1.13.bin
#FIRMWARE = esp32-idf3-20200902-v1.13.bin

.PHONY: esptool
esptool: esptool.py

frameworks:
	sudo rm -rf micropython
	sudo rm -rf MicroWebSrv2
	sudo rm -rf mpython-docs
	git clone https://github.com/micropython/micropython.git
	git clone https://github.com/jczic/MicroWebSrv2.git
	git clone https://github.com/labplus-cn/mpython-docs.git

setup_dev:
	sudo apt-get install git wget flex bison gperf python3 python3-pip python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util
	sudo apt-get install esptool
	sudo apt install picocom
	pip3 install -r requirements.txt
	make frameworks

setup_dev_mac:
	brew install esptool
	brew install picocom
	pip install -r requirements.txt
	make frameworks

ports:
	 dmesg | grep tty

ports_mac:
	ls /dev/tty.*
	ls /dev/cu.*

permission:
	groups ${USER}
	sudo gpasswd --add ${USER} dialout
	sudo chmod 666 $(PORT)
	sudo chmod +x venv/lib/python3.8/site-packages/ampy
	sudo chmod +x venv/lib/python3.8/site-packages/esptool.py

info:
	esptool --chip $(CHIP) --port $(PORT) --before default_reset --baud $(BAUDRATE) --after hard_reset read_flash_status

backup:
	esptool --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) 0x00000 0x400000 backup.bin


# Prepare for micropiton
download_micro_bin: # 1M of flash # other bin's: http://micropython.org/download/esp8266/
	rm -rf $(FIRMWARE)
	wget http://micropython.org/resources/firmware/$(FIRMWARE)

erase_flash:
	esptool.py --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) erase_flash

burn_micro:	#default baud rate 115200
	esptool.py --chip $(CHIP) --port $(PORT) --baud $(BAUDRATE) write_flash -z 0x00000 $(FIRMWARE)

repl:
	picocom $(PORT) -b$(BAUDRATE)

# Work with file at device
PRJ_DIR = app/
upload:
	@for file in $(shell ls $(PRJ_DIR)); do ampy --port $(PORT) --baud $(BAUDRATE) put ${PRJ_DIR}$${file}; done

ls:
	ampy --port $(PORT) --baud $(BAUDRATE) ls

run:
	ampy --port $(PORT) --baud $(BAUDRATE) run main.py

getboot:
	ampy --port $(PORT) --baud $(BAUDRATE) get boot.py
