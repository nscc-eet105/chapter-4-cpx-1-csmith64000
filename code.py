from adafruit_circuitplayground import cp
import time
import touchio
import board
import neopixel

#list_of_pads
touch_pads=[
touchio.TouchIn(board.A1),
touchio.TouchIn(board.A2),
touchio.TouchIn(board.A3),
touchio.TouchIn(board.A4),
touchio.TouchIn(board.A5),
touchio.TouchIn(board.A6)
]


#setup
pixels = cp.pixels
num_pixels = 10
pixels.brightness = 0.3
pixels.auto_write = False

#on_and_off
def turn_on_pixels():
    for i in range(num_pixels):
        pixels[i] = (0,255,0)
    pixels.show()

def turn_off_pixels():
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
    pixels.show()

while True:
    if any(pad.value for pad in touch_pads):
        turn_on_pixels()

    else:
        turn_off_pixels()

    time.sleep(0.1)

