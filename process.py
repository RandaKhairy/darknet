import cv2
import numpy as np


img = cv2.imread('predictions.jpg',1)
f=open("prediction.txt", "r")
if f.mode != 'r':
	print("Error Readin File")

lines = f.readlines()
for l in lines:
	[x, y, w, h] = l.split()
	x = int(float(x))
	y = int(float(y))
	w = int(float(w))
	h = int(float(h))
	starty = int(y - h/2)
	startx = int(x - w/2)
	crop_img = img[starty:starty+h, startx:startx+w]
 
	red = np.mean(crop_img[:, :, 2])
	green = np.mean(crop_img[:, :, 1])
	print("Red mean = ", red)
	print("Green mean = ", green)
	if(red > green):
		print("Red")
	else:
		print("Green")

	
	cv2.imshow('image',crop_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
