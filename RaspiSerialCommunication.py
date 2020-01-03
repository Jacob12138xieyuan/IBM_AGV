import serial
import time
PORT = "/dev/ttyACM0"

s = serial.Serial(PORT, 115200)
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

print("starting...")
for i in range(10):
  time.sleep(3)
  print(i)
  # get acoustic result here
  if(i == 3):
    s.write(b"route A\n")
    data = s.readline()
    print(data)
    continue
  s.write(b"waiting\n")
  data = s.readline()
  print(data)
  if(data == b'start route A                 \r\n'):
    break
  elif(data == b'start route B                 \r\n'):
    break

s.close()
