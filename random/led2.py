
import board
import neopixel
import time

numleds = 50

i = 0

pixels = neopixel.NeoPixel(board.D18, numleds)
pixels.fill ( (0, 0, 0))

while i < numleds:
#	pixels[i] = (24,83,89) 
	pixels[i] = (70,39,76)
#	pixels[i] = (35,186,128)
	pixels[i-1] = (0,0,0)
	time.sleep(0.6)
	i += 1
	if i >= numleds:
		i = 0
