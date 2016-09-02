#!/usr/bin/env python

import serial
import syringepump

import time



conn = serial.Serial('/dev/ttyUSB0', 19200)
pump = syringepump.Pump(conn)

while conn.inWaiting():
    print pump.get_response()

pump.set_diameter(26.59)
pump.set_phase(1)
pump.set_function("RAT")
pump.set_rate(20.0, 'MM')
pump.set_volume_units('ML')
pump.set_volume(0.02)
pump.set_direction('INF')
pump.buzz()
pump.run()
time.sleep(1)
while conn.inWaiting():
    print pump.get_response()

pump.buzz()
pump.run()
while conn.inWaiting():
    print pump.get_response()

pump.buzz(0.1)
