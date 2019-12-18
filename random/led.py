import board
import neopixel

numleds = 100

pixels = neopixel.NeoPixel(board.D18, numleds)
pixels.fill ( (1, 5, 1))
