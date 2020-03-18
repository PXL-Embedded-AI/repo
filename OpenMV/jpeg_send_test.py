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
gUart = pyb.UART(3, 115200, timeout_char=1000)

# Functions
# ... Here ...

# Run-once code
gRedLed.on()
sensor.skip_frames(time = 2000)
gRedLed.off()

gBlueLed.on()
for i in range(200):
    gUart.write('snap')
    img = sensor.snapshot().compressed(quality=40)
    gUart.write(img.size().to_bytes(4, 'little'))
    gUart.write(img)
gBlueLed.off()

# Main loop
while(True):
    time.sleep(1000)
