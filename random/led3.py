
import board
import neopixel
import time

numleds = 50

i = 0
r = 0
g = 0
b = 0

pixels = neopixel.NeoPixel(board.D18, numleds)
pixels.fill ( (0, 0, 0))

while i < numleds:
#	pixels[i] = (24,83,89) 
#	pixels[i] = (70,39,76)
#	pixels[i] = (35,186,128)
#	pixels[i-1] = (0,0,0)

	pixels[i] = (g,r,b)

#	time.sleep(0.6)

	i += 1
	g += 7
	r += 11
	b += 13

	if i >= numleds:
		i = 0
	if g >= 55:
		g = 0
	if r >= 55:
		r = 0
	if b >= 55:
		b = 0
