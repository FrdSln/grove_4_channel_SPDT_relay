# Créé le 19/10/2025 en MicroPython - F. SAULIN
# Test 4 Channel SPDT Relay pour carte micro:bit
# Modification de l'addresse I2C
from microbit import *
from mb_4SPDTRelay_grove import *
import time

relais = mb_4SPDTRelay_grove(0x11)
time.sleep(1)

scan = i2c.scan()
for i in range(len(scan)):
    print(hex(scan[i]))

relais.turn_on_channel(1)
time.sleep(2)
relais.turn_off_channel(1)
time.sleep(2)

relais.changeI2CAddress(0x11, 0x31)

relais = mb_4SPDTRelay_grove(0x31)
time.sleep(1)

scan = i2c.scan()
for i in range(len(scan)):
    print(hex(scan[i]))

relais.channel_control(0b0101)
time.sleep(2)
relais.channel_control(0b0000)
