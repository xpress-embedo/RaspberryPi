'''
01 - 3.3V       02 - 5V
03 - SDA(2)     04 - 5V
05 - SCL(3)     06 - GND
07 - (4)        08 - TXD(14)
09 - GND        10 - RXD(15)
11 - (17)       12 - (18)
13 - (27)       14 - GND
15 - (22)       16 - (23)
17 - 3.3V       18 - (24)
19 - MOSI(10)   20 - GND
21 - MISO(9)    22 - (25)
23 - SCKL(11)   24 - (8)
25 - GND        26 - (7)
'''

import RPi.GPIO as GPIO
import time

# Trigger Pin
Trigger = 15
Echo = 16
GPIO.setmode( GPIO.BOARD)
GPIO.setup( Trigger, GPIO.OUT)  # Trigger Pin is Output for RPi
GPIO.setup( Echo, GPIO.IN)      # Echo Pin is Input for RPi
print "Starting program"
try:
    while True:
        GPIO.output( Trigger, False)    # Reset pin State to Low
        time.sleep(2)                   # 2 Second Delay

        # Send Trigger Pulse to Module
        GPIO.output(Trigger, True)      # Trigger High
        time.sleep(0.00001)             # 10usec
        GPIO.output(Trigger, False)     # Trigger Low

        while GPIO.input(Echo)==0:      # Wait for Return Pulse
            start_time = time.time()    # Save Start Time

        while GPIO.input(Echo)==1:      # Wait for Pulse to End
            end_time = time.time()      # Save the Pulse End Time

        tof = end_time - start_time    # Time of Flight
	print "Time of Flight = ", tof, " sec"

	# Speed of Sound 34300 cm/sec
	distance = (tof * 34300.0) / 2.0
	# The above expression is divided by two,
	# because sound waves has travelled twice distance
	# from Module to Object and then back.

	distance = round(distance, 2)
	
	print " Object Distance = ", distance, " cm"	
        
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    GPIO.cleanup()
