get_CH340_mac:
	git clone https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver
micropython:
	git clone -b v1.13 --single-branch https://github.com/micropython/micropython.git
ports:
	dmesg | grep ttyS

# Prepare for micropiton
micropython_bin: # 1M of flash # other bin's: http://micropython.org/download/esp8266/
	wget http://micropython.org/resources/firmware/esp8266-1m-20210116-unstable-v1.13-268-gf7aafc062.bin
clear_esp:
	esptool.py --port /dev/ttyUSB0 erase_flash
burn_micro:	#default baud rate 115200
	esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 esp8266-1m-20210116-unstable-v1.13-268-gf7aafc062.bin
burn_micro_autoport:
	esptool.py --port /dev/$(ls /dev | grep cu.wchusbserial) erase_flash
