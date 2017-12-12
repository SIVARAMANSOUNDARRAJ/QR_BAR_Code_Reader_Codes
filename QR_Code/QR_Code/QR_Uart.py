from sys import argv
import zbar
import serial

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]

#proc.request_size(800,480)

proc.init(device)

# enable the preview window
proc.visible = True

# read at least one barcode (or until window closed)
proc.process_one()

# hide the preview window
proc.visible = False

# extract results
for symbol in proc.results:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

ser = serial.Serial(
        port='/dev/serial0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

print "Serial is open: " + str(ser.isOpen())

print "Now Writing"
ser.write(symbol.data)

print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

ser.close()


#pi Camera link: #link:http://techblog.saurabhkumar.com/2015/09/scanning-barcodes-using-raspberry-pi.html

#UART Link: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=158856&p=1032763#p1032763
