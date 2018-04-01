import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    while (True):
        GPIO.output(18, True)
        print "Pin High"
        time.sleep(0.5)
        GPIO.output(18, False)
        print "Pin Low"
        time.sleep(0.5)
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    GPIO.cleanup()
