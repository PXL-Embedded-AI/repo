# Spectral analysis - By: Eduardo L. Bemelmans - Tue Apr 28 2020

import sensor, image, time, pyb

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

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

spectrum = spectroscopy(100, 135, 220, 135, 220, 147, 135, 147)

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
    img.draw_rectangle(spectrum.x0, spectrum.y0,
        spectrum.x1 - spectrum.x0,
        spectrum.y3 - spectrum.y0,
        color = (255, 255, 255), thickness = 1, fill = False)

