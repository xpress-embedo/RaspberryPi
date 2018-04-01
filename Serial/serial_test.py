'''
01 - 3.3V       02 - 5V
03 - SDA(2)     04 - 5V
05 - SCL(3)     06 - GND
07 - (4)        08 - TXD(14) TXD0
09 - GND        10 - RXD(15) RXD0
11 - (17)       12 - (18)
13 - (27)       14 - GND
15 - (22)       16 - (23)
17 - 3.3V       18 - (24)
19 - MOSI(10)   20 - GND
21 - MISO(9)    22 - (25)
23 - SCKL(11)   24 - (8)
25 - GND        26 - (7)
'''

import time
import serial

print "Starting program"

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
    ser.write('Hello World\r\n')
    ser.write('Serial Communication Using Raspberry Pi\r\n')
    ser.write('By: Embedded Laboratory\r\n')
    print 'Data Echo Mode Enabled'
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            print (data)
        
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    ser.close()
    pass
