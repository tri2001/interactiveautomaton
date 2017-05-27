import time
import wiringpi

# Init
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

while True:
    for pulse in range(50,200,1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(0.1)
    for pulse in range(200,50,-1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(0.1)
