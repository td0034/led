import board
import neopixel
import math
import random

numPixels = 100

pixel = neopixel.NeoPixel(board.D18, numPixels)

brightness = 50

deg0 = 0
deg90 = 135
deg180 = 225

while deg0 <= 360:

	rads1 = math.radians(deg0)
	rads2 = math.radians(deg90)
	rads3 = math.radians(deg180)
	sin1 = math.sin(rads1)
	sin2 = math.sin(rads2)
	sin3 = math.sin(rads3)
	red = int(round(sin1 * brightness))
	blue = int(round(sin2 * brightness))
	green = int(round(sin3 * brightness))

	if red < 0:
		red = 0
	if blue < 0:
		blue = 0
	if green < 0:
		green = 0
	
	deg0 += 1
	deg90 += 1
	deg180 += 1

	pixel.fill((green,red,blue))

	if deg0 == 360:
		deg0 = 0
	if deg90 == 360:
		deg90 = 0
	if deg180 == 360:
		deg180 = 0

