"""
1-enable I2C
2-sudo apt-get install i2c-tools #address of the LCD
3-sudo apt-get install python-smbus #install smbus which gives python library
4-i2cdetect -y #to get the i2c address (3f)
5-create a i2c_LCD_driver.py file and modify I2CBUS=0 and address = 0x3f
6-create another file lcd.py and then run it
"""
import i2c_LCD_driver
from time import *

mylcd = i2c_LCD_driver.lcd()

mylcd.lcd_display_string("SECURITY", 1, 4)
mylcd.lcd_display_string("SYSTEM", 2, 5)
sleep(6)

mylcd.lcd_clear()