from sys import argv
import serial, time
import zbar
import serial
import time

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]

proc.init(device)

# enable the preview window
proc.visible = True

# read at least one barcode (or until window closed)
proc.process_one()

# hide the preview window
proc.visible = False

for symbol in proc.results:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data,
             
      
ser = serial.Serial(
               port='/dev/serial0',
               #port='/dev/ttyAMA0',
              # port='/dev/ttyUSB0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
)
#counter=0
          
      
while 1:
    
       ser.write(symbol.data)
       x=ser.readline()
       
       print x
