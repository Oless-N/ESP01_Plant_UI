try:
  import usocket as socket
except:
  import socket

from main import main
# import network
import esp
import gc
gc.collect()
esp.osdebug(None)

#
# ssid = 'Plant_01'
# password = 'yourplant'
#
# station = network.WLAN(network.STA_IF)
#
# station.active(True)
# station.connect(ssid, password)
#
# while station.isconnected() == False:
#   pass
#
# print('Connection successful')
# print(station.ifconfig())

gc.collect()
main()
