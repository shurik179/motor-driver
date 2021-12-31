from machine import Pin, I2C
from time import sleep
import pr_motor_controller
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)

# just for testing

driver = pr_motor_controller.controller(i2c)

print("Motor controller initialized.")
print("Firmware version: " + driver.fw_version()))
# driver.reverse_encoder(0)
driver.set_motors(500) #set speed of both motors to 50%
while True:
    driver.get_encoders()
    driver.get_speeds()
    print("Encoders: {} {}. Speeds: {} {}".format(driver.encoder[0],driver.encoder[1], driver.speed[0], driver.speed[1] ))
    sleep(0.5)
