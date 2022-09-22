#set parameters
input = 0.02
MAX_SENT = 0xFFF
MAX_RECEIVE = 0x3FF
MAX_VOLTAGE = 12


#converted to a fraction out of 4095
voltHex = round(input * MAX_SENT / MAX_VOLTAGE)

print(voltHex)
#converted to a 0x000 Hex Value
voltHex ="%0.3X" % voltHex
print(voltHex)

voltHex = int(voltHex,16)
#sent off to the glassman
#glassman coverts n/4095 to m/1023
voltHex = round(voltHex * (MAX_RECEIVE/MAX_SENT))
print(voltHex)

#glassman send data back to user
voltRead = voltHex * MAX_VOLTAGE / MAX_RECEIVE


print(voltRead)
