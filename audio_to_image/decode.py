from PIL import Image
import scipy.io.wavfile as wave
import numpy as np
import sys

filename = sys.argv[1]
im = Image.open(filename)
left = []
right = []
value = im.getpixel((-1,-1))
ans = int(str(value[0])+str(value[1])+str(value[2]))

print("Enter Sampling Rate : ")
samplingRate = int(input())
if samplingRate != ans:
	raise "Error Matching the sampling rate"

amp = 10

for i in range(im.size[0]):
	for j in range(im.size[1]):
		pixel = im.getpixel((i, j))
		r = pixel[0]
		g = pixel[1]
		b = pixel[2]

		if (b == 64):
			r *= -1
			g *= -1

		elif (b == 128):
			r *= -1

		elif (b == 192):
			g *= -1

		r *= 4
		g *= 4

		left.append(r*amp)
		right.append(g*amp)


y = []
for i in range(len(left)):
	y.append([left[i], right[i]])

y = numpy.array(y, dtype='int16')
name = filename.split(".")[0]+"out.wav"
wave.write(name, samplingRate, y)
print("Output saved as", name)
