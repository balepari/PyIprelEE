#!/usr/bin/python

from pymodbus.client.sync import ModbusTcpClient
import logging
from struct import *

loggami = 0

if loggami == 1:
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

client = ModbusTcpClient('172.17.251.32')

UNIT = 0xA
ADR_FROM = 45099
ADR_QTY = 2

if loggami == 1:
    log.debug('Read HR {0} going forward by {1}'.format(ADR_FROM, ADR_QTY))

rr = client.read_holding_registers(ADR_FROM, ADR_QTY, unit=UNIT)

if loggami == 1:
    print(rr.registers[0])
    print(rr.registers[1])

i1 = ((rr.registers[1] * 65536) + rr.registers[0]) / 10000.0

if loggami == 1:
    print(i1)
    print("Value: %8.2f" % i1)

tup = (rr.registers[0], rr.registers[1])

if loggami == 1:
    print(hex(tup[0]))
    print(hex(tup[1]))

pippo = pack('>HH', tup[0], tup[1])
if loggami == 1:
    print(pippo)

f = unpack('>f', pippo)
if loggami == 0:
    print(f[0])


client.close()
