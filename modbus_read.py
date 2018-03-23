#!/usr/bin/python

from struct import *

from pymodbus.client.sync import ModbusTcpClient


def get_hr_float32(connection, start, qty, devaddr):
    lists = []
    rr = connection.read_holding_registers(start, qty, unit=devaddr)
    for i in range(0, len(rr.registers)-1, 2):
        if rr.registers[i] == 65535:
            fmt = ">l"
        elif rr.registers[i] > 10:
            fmt = ">f"
        else:
            fmt = ">l"

        if rr.registers[i] == 0:
            lists.append((rr.registers[i]*65536)+rr.registers[i+1])
        else:
            print("rr.registers[i]= ", rr.registers[i])
            print("rr.registers[i]= ", rr.registers[i+1])
            tup = (rr.registers[i], rr.registers[i+1])
            print("tup= ", tup)
            # print("hex(tup[i])= ", hex(tup[i]))
            # print("hex(tup[i+1])= ", hex(tup[i+1]))
            packed_data = pack('>HH', tup[0], tup[1])
            print("packed_data= ", packed_data)
            converted_value = unpack(fmt, packed_data)
            print("converted_value= ", converted_value[0])
            print("fmt= ", fmt)
            lists.append(converted_value[0])

    return lists


# ------- MAIN -------

client = ModbusTcpClient('172.17.251.32')
from_addr = 1001
for_qty = 28
device = 0xB

# from_addr = 3000
# for_qty = 8
# device = 0xA


field_list = get_hr_float32(client, from_addr-1, for_qty, device)
print(field_list)

client.close()
