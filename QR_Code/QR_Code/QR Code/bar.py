import io
import time
from PIL import Image
import zbar

# Create the in-memory stream
stream = io.BytesIO()
with cv2.cv2() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
pil = Image.open(stream)
#
#########################################
#
# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

pil = pil.convert('L')
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
scanner.scan(image)

# extract results
for symbol in image:
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
del(image)
