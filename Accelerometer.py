from machine import Pin, I2C
import time

# Set up the I2C bus
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Set up the device address and register addresses
device_address = 0x68
power_mgmt_1 = 0x6b
gyro_xout_h = 0x43
gyro_yout_h = 0x45
gyro_zout_h = 0x47

# Wake up the device
i2c.writeto_mem(device_address, power_mgmt_1, b'\x00')

while True:
    # Read the raw gyroscope data from the registers
    gyro_xout = i2c.readfrom_mem(device_address, gyro_xout_h, 2)
    gyro_yout = i2c.readfrom_mem(device_address, gyro_yout_h, 2)
    gyro_zout = i2c.readfrom_mem(device_address, gyro_zout_h, 2)

    # Convert the raw data to degrees per second
    gyro_x = (gyro_xout[0] << 8 | gyro_xout[1]) / 131.0
    gyro_y = (gyro_yout[0] << 8 | gyro_yout[1]) / 131.0
    gyro_z = (gyro_zout[0] << 8 | gyro_zout[1]) / 131.0

    # Print the gyroscope data
    print("Gyroscope data: X = %.2f, Y = %.2f, Z = %.2f" % (gyro_x, gyro_y, gyro_z))

    # Delay before reading again
    time.sleep(0.1)
