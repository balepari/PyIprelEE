#!/usr/bin/python

from pymodbus.client.sync import ModbusTcpClient
import logging
from struct import *

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


client = ModbusTcpClient('172.17.251.32')

UNIT = 0xA

log.debug("Read HR")
rr = client.read_holding_registers(45099, 2, unit=UNIT)

print rr.registers[0]
print rr.registers[1]
#print rr.registers[2]
#print rr.registers[3]

i1 = ((rr.registers[1]*65536) + rr.registers[0])/10000.0

print i1
print("Value: %8.2f" % i1)



tup=(rr.registers[0], rr.registers[1])

print hex(tup[0])
print hex(tup[1])

mypack = pack('>HH',tup[0],tup[1])
print `mypack`

f = unpack('>f', mypack)
print f



client.close()


