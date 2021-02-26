try:
    import usocket as socket
except:
    import socket

import network
import esp
import uos

def run():
    uname = uos.uname()

    ap = network.WLAN(network.AP_IF)
    ap.active(True)

    ssid = "ssid"
    password = "password"
    ap.config(essid=ssid, password=password)

    while ap.active() == False:
        pass

    print('Access Point Active')
    print(ap.ifconfig())
    print("Connect to " + ssid + ":" + "password = " + password);
    print("Visit: " + ap.ifconfig()[2] + ":80")

    print('===== ===== =====')

    res_01 = """<html>
        <head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
        <body>
        <h1>Hello, MicroPython@ESP32!</h1>"""
    res_02 = """
        </body>
        </html>"""

    res_something = "sysname: " + uname.sysname + "<br/>" \
                                                  "nodename: " + uname.nodename + "<br/>" + \
                    "release: " + uname.release + "<br/>" + \
                    "version: " + uname.version + "<br/>" + \
                    "machine: " + uname.machine + "<br/>"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        youraddr = str(addr)
        request = conn.recv(1024)

        conn.send(res_01)
        conn.send(res_something)
        conn.send("<br/><br/>")
        conn.send(youraddr)
        conn.send("<br/><br/>")
        conn.send(request)
        conn.send(res_02)
        conn.close()

def main():
    run()
