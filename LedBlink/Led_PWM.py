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

# Led1 on my Board
led = 11
GPIO.setmode( GPIO.BOARD)
GPIO.setup( led, GPIO.OUT)
# 50Hz PWM Frequency
pwm_led = GPIO.PWM( led, 50)
# Full Brightness, 100% Duty Cycle
pwm_led.start(100)
try:
    while True:
        duty_s = raw_input("Enter Brightness Value (0 to 100):")
        # Convert into Integer Value
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    GPIO.cleanup()
