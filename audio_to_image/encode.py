from PIL import Image
import scipy.io.wavfile as wave
import numpy as np
import math
import sys

audiofile = sys.argv[1]
samplingRate, audioChannels = wave.read(audiofile)

left = list(audioChannels[:, 0])
right = list(audioChannels[:, 1])

length = len(left)
size = int(math.sqrt(length)) + 10

mleft = max(map(abs, left))
mright = max(map(abs, right))

def divide(a):
	return (a / float(mleft)) * 255

left = list(map(divide, left))

def divide(a):
	return (a / float(mright)) * 255

right = list(map(divide, right))

im = Image.new("RGB", (size, size), "black")


ai = 0
done = False
for i in range(size):
	if done:
		break
	for j in range(size):
		if ai >= length:
			done = True
			break
		r = int(left[ai])
		g = int(right[ai])
		b = 0
		if (r == 0 and g == 0):
			b = 0
		elif (r < 0 and g < 0):
			b = 64
		elif (r < 0 and g >= 0):
			b = 128
		elif (r >= 0 and g < 0):
			b = 192
		else:
			b = 255
		im.putpixel((i, j), (r, g, b))
		ai += 1

temp = str(samplingRate)
im.putpixel((-1,-1), (int(temp[:2]),int(temp[2:4]),int(temp[4:])))

name = audiofile.split(".")[0]+".bmp"
im.save(name)

print("Image saved as "+name+"! Sampling rate to retrive image: ", samplingRate)
