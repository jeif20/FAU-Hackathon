import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

pwm = GPIO.PWM(7, 50)
pwm1 = GPIO.PWM(8, 50)

pwm.start(7.5)
pwm1.start(7.5)

while True:
        pwm.ChangeDutyCycle(7.5)
        pwm1.ChangeDutyCycle(7.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(12.5)
        pwm1.ChangeDutyCycle(12.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(2.5)
        pwm1.ChangeDutyCycle(2.5)
        time.sleep(1)

