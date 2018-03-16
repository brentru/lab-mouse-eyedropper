"""
GCode Sender for Python3 + PySerial + Marlin Firmware

---
derivative of simplestream.py for GRBL firmware (https://github.com/grbl/grbl/blob/master/doc/script/simple_stream.py)

The MIT License

Copyright (c) 2018 Brent Rubell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
import os
import serial
import time

# machine serial port
PORT = '/dev/cu.wchusbserial14210'
BAUD = 250000

# serial setup
s = serial.Serial(PORT, BAUD)

# wake up the serial
s.write(("\n\r\n\r\n\r".encode()))
time.sleep(3)
startup_data = s.readline()
# check for startup data on the serial
if s is not None:
    print("* DBG, data on serial, flushing...")
    s.flushInput()
else:
    s.close()

l = "G0 X30"

l = l + "\n"
print('Sending: ' + l + "...")
s.write(l.encode())
# wait for marlin response
machine_out = s.readline()
print ('* DBG, MACHINE OUTPUT:' + machine_out.decode())

# close serial port
s.close()
