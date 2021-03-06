import json

import serial
from serial.tools import list_ports as lp

"""
The arduino code.

#include <ArduinoJson.h>
void setup() {
  Serial.begin(9600); 
  while(!Serial) {
  }
}

void loop() {
  int     size_ = 0;
  String  payload;
  while ( !Serial.available()  ){}
  if ( Serial.available() )
    payload = Serial.readStringUntil( '\n' );
  StaticJsonDocument<512> doc;

  DeserializationError   error = deserializeJson(doc, payload);
  if (error) {
    Serial.println(error.c_str()); 
    return;
  }
  if (doc["operation"] == "sequence") {
     Serial.println("{\"Success\":\"True\"}");
  }
  else {
      Serial.println("{\"Success\":\"False\"}");
   }
  delay(20);
}
"""

arduino_status_data_struct = {
    "sensor": {
        0: {
            "name": "custom_name",
            "relay": 0,
            "value": 0,
            "common": 0,
            "dir": 0,
            "period": 0,
            "work": 0,
            "left": 0,
            "timeout": 0
        },
    },
    "servo": {
        0: {
            "name": "custom_name",
            "relay": 0,
            "value": 0,
            "common": 0,
            "dir": 0,
            "period": 0,
            "work": 0,
            "left": 0,
            "timeout": 0
        },
    },
    "motor": {
        0: {
            "name": "custom_name",
            "relay": 0,
            "value": 0,
            "common": 0,
            "dir": 0,
            "period": 0,
            "work": 0,
            "left": 0,
            "timeout": 0
        },
    },
}

port_list = lp.comports()
if not port_list:
    print("ports not found!!!")
    exit(0)

count_port = 0
for port in port_list:
    print(f"{count_port} - {port}")
    count_port += 1

selected = int(input("Enter number of port: "))

if 0 <= selected < len(port_list):
    print("Ready...")
    ser = serial.Serial(
        port_list[selected][0],
        baudrate=9600,
        timeout=2.5,
        parity=serial.PARITY_NONE,
        bytesize=serial.EIGHTBITS,
        stopbits=serial.STOPBITS_ONE
    )
    data = {}
    data["operation"] = "sequence"

    data = json.dumps(data)
    print(data)
    if ser.isOpen():
        ser.write(data.encode('ascii'))
        ser.flush()
        try:
            incoming = ser.readline().decode("utf-8")
            print("incoming", incoming)
        except Exception as e:
            print(str(e))
        ser.close()
    else:
        print("Opening port error")
else:
    print("Do not have this port")
