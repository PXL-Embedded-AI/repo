import time, pyb, sensor, image, mjpeg

# Initialization code
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

# Global variables
gRedLed = pyb.LED(1)
gGreenLed = pyb.LED(2)
gBlueLed = pyb.LED(3)
gIrLed = pyb.LED(4)
gLed = 1
gUsb = pyb.USB_VCP()
gMjpeg = mjpeg.Mjpeg('video.mjpeg')
gClock = time.clock()

# Functions
# ... Here ...

# Run-once code
gRedLed.on()
sensor.skip_frames(time = 2000) # Give the user time to get ready.
gRedLed.off()

gBlueLed.on()
for i in range(200):
    gClock.tick()
    img = sensor.snapshot()
    gMjpeg.add_frame(img)
gMjpeg.close(gClock.fps())
gBlueLed.off()

# Main loop
while(True):
    time.sleep(1000)
