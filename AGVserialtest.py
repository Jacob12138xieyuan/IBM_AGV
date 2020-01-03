import serial

PORT = "/dev/ttyACM0"
##
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE


while True:
    s.readline()
    s.write("from pc".encode('utf-8'))

s.close()
