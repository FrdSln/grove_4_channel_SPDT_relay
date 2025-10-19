# Créé le 19/10/2025 en MicroPython - F. SAULIN
# Bibliothèque 4 Channel SPDT Relay pour carte micro:bit V2

from microbit import *
import time

class mb_4SPDTRelay_grove():
    # initialisation
    def __init__(self, address):
        self.I2CADDR = address
        self.CHANNEL_CTRL = 0x10
        self.SAVE_I2C_ADDR = 0x11
        self.READ_I2C_ADDR = 0x12
        self.READ_FIRMWARE_VERSION = 0x13
        self.channel_state = 0
        i2c.init(freq=100000, sda=pin20, scl=pin19)

    def getFirmwareVersion(self):
        buf = bytearray(1)
        buf[0] = self.READ_FIRMWARE_VERSION
        i2c.write(self.I2CADDR, buf)
        version = i2c.read(self.I2CADDR, 1)
        return version[0]

    def changeI2CAddress(self, old_addr, new_addr):
        buf = bytearray(2)
        buf[0] = self.SAVE_I2C_ADDR
        buf[1] = new_addr
        i2c.write(old_addr, buf)
        self.I2CADDR = new_addr

    def turn_on_channel(self, channel):
        self.channel_state |= (1 << (channel - 1))
        buf = bytearray(2)
        buf[0] = self.CHANNEL_CTRL
        buf[1] = self.channel_state
        i2c.write(self.I2CADDR, buf, repeat=False)

    def turn_off_channel(self, channel):
        self.channel_state &= ~(1 << (channel - 1))
        buf = bytearray(2)
        buf[0] = self.CHANNEL_CTRL
        buf[1] = self.channel_state
        i2c.write(self.I2CADDR, buf, repeat=False)

    def channel_control(self, state):
        self.channel_state = state
        buf = bytearray(2)
        buf[0] = self.CHANNEL_CTRL
        buf[1] = state
        i2c.write(self.I2CADDR, buf, repeat=False)

