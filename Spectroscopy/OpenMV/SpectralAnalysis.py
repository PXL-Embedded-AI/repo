# Spectral analysis - By: Eduardo L. Bemelmans - Tue Apr 28 2020

import sensor, image, time, pyb, json, os

print(os.getcwd())

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)

class spectroscopy:
    def __init__(self, boundary_x0, boundary_y0, boundary_x1, boundary_y1,
        boundary_x2, boundary_y2, boundary_x3, boundary_y3):
        self.x0 = boundary_x0
        self.y0 = boundary_y0
        self.x1 = boundary_x1
        self.y1 = boundary_y1
        self.x2 = boundary_x2
        self.y2 = boundary_y2
        self.x3 = boundary_x3
        self.y3 = boundary_y3



clock = time.clock()

spectrum = spectroscopy(90, 145, 220, 145, 220, 170, 90, 170)

f=open('spectrumHistogram.json','w')
f.write('[\n')
limit = 10
for i in range(limit):
    clock.tick()
    f.write('{\"spectrum\":%d,\"binaries\":' % i)
    img = sensor.snapshot()
    # print(clock.fps())
    spctrArea = img.draw_rectangle(spectrum.x0, spectrum.y0,
        spectrum.x1 - spectrum.x0,
        spectrum.y3 - spectrum.y0,
        color = (255, 255, 255), thickness = 1, fill = False)
    spctrHistogram = img.get_histogram(bins=8, roi=(spectrum.x0, spectrum.y0,
        spectrum.x1 - spectrum.x0,
        spectrum.y3 - spectrum.y0))
    print(spctrHistogram)
    Data = spctrHistogram

    jsonData = json.dumps(spctrHistogram)
    print(jsonData)
    f.write(jsonData)
    f.write('}')
    if (i is not limit-1):
        f.write(',')
        f.write('\n')
f.write('\n')
f.write(']')
f.close()
pyb.hard_reset()
# RGB: Space, assen definiëren
# Serial data
