import cv2
import numpy as np
from collections import deque

pts = deque(maxlen=100)
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

img1 = cv2.imread('map.jpg')
img1 = cv2.resize(img1, (589, 479))
img2 = cv2.imread('map2.jpg')
img2 = cv2.resize(img2, (589, 479))
win = cv2.imread('youwin.jpg')
win = cv2.resize(win, (639, 479))
lose1 = cv2.imread('youlose1.jpg')
lose1 = cv2.resize(lose, (639, 479))
lose2 = cv2.imread('youlose2.jpg')
lose2 = cv2.resize(lose, (639, 479))
lose3 = cv2.imread('youlose3.jpg')
lose3 = cv2.resize(lose, (639, 479))
new = cv2.imread('new.jpg')
new = cv2.resize(new, (639, 479))

ms = 1
g1 = 0
g1win = 0
g1lose = 0
g2 = 0
g2win = 0
g2lose = 0

ret, frame = cap.read()
rowsFrame,colsFrame,channelsFrame = frame.shape

def InsertLogo(img1, img2, i, j):
	if(i+cols < colsFrame and j+rows < rowsFrame):
		# I want to put logo on top-left corner, So I create a ROI
		roi = img1[j:j+rows, i:i+cols]
		# Now create a mask of logo and create its inverse mask also
		img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
		ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
		mask_inv = cv2.bitwise_not(mask)
		# Now black-out the area of logo in ROI
		img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
		# Take only region of logo from logo image.
		img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
		# Put logo in ROI and modify the main image
		dst = cv2.add(img1_bg,img2_fg)
		img1[j:j+rows, i:i+cols] = dst
	return img1

while(1):

	# Take each frame
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of blue color in HSV
	lower_blue = np.array([110, 50, 50], dtype=np.uint8)
	upper_blue = np.array([130,255,255], dtype=np.uint8)

	# define range of skin color in HSV
	#lower_blue = np.array([0, 48, 80], dtype=np.uint8)
	#upper_blue = np.array([20, 255, 255], dtype=np.uint8)

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# apply a series of erosions and dilations to the mask
	# using an elliptical kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
	mask = cv2.erode(mask, kernel, iterations = 2)
	mask = cv2.dilate(mask, kernel, iterations = 2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = ((int(M["m10"] / M["m00"])), (int(M["m01"] / M["m00"])))
		cx = int(M["m10"] / M["m00"])
		cy = int(M["m01"] / M["m00"])
		if(cx > 25 and cx < 75 and cy > 250 and cy < 300 and ms == 1):
			g1 = 1
			ms = 0
			g1win = 0
			g1lose = 0
			flag = 0
		if(g1 == 1 and g1win == 0 and g1lose == 0):
			if(cx > 50 and cx < 125 and cy > 21 and cy < 134):
				flag = 1
			if(flag == 1):
				if(cx > 50 and cx < 356 and cy > 0 and cy < 20):
					g1lose = 1
					flag = 0
				if(cx > 356 and cx < 640 and cy > 0 and cy < 326):
					g1lose = 1
					flag = 0
				if(cx > 50 and cx < 156 and cy > 136 and cy < 480):
					g1lose = 1
					flag = 0
				if(cx > 213 and cx < 640 and cy > 440 and cy < 480):
					g1lose = 1
					flag = 0
		if(cx > 550 and cx < 640 and cy > 330 and cy < 440 and g1 == 1):
			g1win = 1
		if(cx > 125 and cx < 225 and cy > 400 and cy < 450 and g1win == 1):
			ms = 1
			g1win = 0
			g1 = 0
		if(cx > 125 and cx < 225 and cy > 400 and cy < 450 and g1lose == 1):
			ms = 0
			g1lose = 0
			g1 = 1

		if(cx > 325 and cx < 375 and cy > 250 and cy < 300 and ms == 1):
			g2 = 1
			ms = 0
			g2win = 0
			g2lose = 0
			flag = 0
		if(g2 == 1 and g2win == 0 and g2lose == 0):
			if(cx > 50 and cx < 100 and cy > 27 and cy < 88):
				flag = 1
			if(flag == 1):
				if(cx > 50 and cx < 640 and cy > 0 and cy < 25):
					g2lose = 1
					flag = 0
				if(cx > 610 and cx < 640 and cy > 27 and cy < 247):
					g2lose = 1
					flag = 0
				if(cx > 538 and cx < 640 and cy > 250 and cy < 333):
					g2lose = 1
					flag = 0
				if(cx > 396 and cx < 506 and cy > 92 and cy < 165):
					g2lose = 1
					flag = 0
				if(cx > 50 and cx < 134 and cy > 92 and cy < 104):
					g2lose = 1
					flag = 0
				if(cx > 50 and cx < 328 and cy > 462 and cy < 480):
					g2lose = 1
					flag = 0
				if(cx > 327 and cx < 640 and cy > 425 and cy < 480):
					g2lose = 1
					flag = 0
				if(cx > 365 and cx < 431 and cy > 342 and cy < 425):
					g2lose = 1
					flag = 0
				if(cx > 137 and cx < 538 and cy > 250 and cy < 277):
					g2lose = 1
					flag = 0
				if(cx > 134 and cx < 396 and cy > 92 and cy < 105):
					g2lose = 1
					flag = 0
				a = 137
				for y in range(106, 164, 1):
					for x in range(a, 395, 1):
						if(cx == x and cy == y):
							g2lose = 1
							flag = 0
					a += 4
				b = 383
				for y in range(246, 182, -1):
					for x in range(b, 137, -1):
						if(cx == x and cy == y):
							g2lose = 1
							flag = 0
					b -= 4
				if(cx > 137 and cx < 287 and cy > 278 and cy < 346):
					g2lose = 1
					flag = 0
				c = 255
				for y in range(363, 349, -1):
					for x in range(c, 137, -1):
						if(cx == x and cy == y):
							g2lose = 1
							flag = 0
					c -= 8
				for y in range(458, 423, -4):
					for x in range(152, 327, 1):
						if(cx == x and cy == y):
							g2lose = 1
							flag = 0
		if(cx > 593 and cx < 640 and cy > 335 and cy < 422 and g2 == 1):
			g2win = 1
		if(cx > 125 and cx < 225 and cy > 400 and cy < 450 and g2win == 1):
			ms = 1
			g2win = 0
			g2 = 0
		if(cx > 125 and cx < 225 and cy > 400 and cy < 450 and g2lose == 1):
			ms = 0
			g2lose = 0
			g2 = 1

		# only proceed if the radius meets a minimum size
		if (radius > 10):
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (cx, cy), 10,(0, 0, 0), -1)

	# update the points queue
	pts.appendleft(center)

	if(ms == 1):
		rows,cols,channels = new.shape
		InsertLogo(frame, new, 0, 0)
		cv2.putText(frame,"Electric Current Avoider",(125,100), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.putText(frame,"Touch Red to choose level",(50,200), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.putText(frame,"Level 1",(100,275), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(25, 250),(75,300),(0,255,0),-1)
		cv2.putText(frame,"Level 2",(400,275), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(325, 250),(375,300),(0,255,0),-1)

	if(ms == 0 and g1 == 1 and g1win == 0 and g1lose == 0):
		x = 50
		y = 0
		rows,cols,channels = img1.shape
		InsertLogo(frame, img1, x, y)
	if(g1win == 1 and g1lose == 0 and ms == 0):
		rows,cols,channels = new.shape
		InsertLogo(frame, new, 0, 0)
		rows,cols,channels = win.shape
		InsertLogo(frame, win, 0, 0)
		cv2.putText(frame,"Return Menu",(275,430), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(125, 400),(225,450),(0,255,0),-1)
	if(g1win == 0 and g1lose == 1 and ms == 0):
		rows,cols,channels = new.shape
		InsertLogo(frame, new, 0, 0)
		rows,cols,channels = lose.shape
		InsertLogo(frame, lose1, 0, 0)
		cv2.putText(frame,"Restart",(275,430), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(125, 400),(225,450),(0,255,0),-1)

	if(ms == 0 and g2 == 1 and g2win == 0 and g2lose == 0):
		x = 50
		y = 0
		rows,cols,channels = img2.shape
		InsertLogo(frame, img2, x, y)
	if(g2win == 1 and g2lose == 0 and ms == 0):
		rows,cols,channels = new.shape
		InsertLogo(frame, new, 0, 0)
		rows,cols,channels = win.shape
		InsertLogo(frame, win, 0, 0)
		cv2.putText(frame,"Return Menu",(275,430), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(125, 400),(225,450),(0,255,0),-1)
	if(g2win == 0 and g2lose == 1 and ms == 0):
		rows,cols,channels = new.shape
		InsertLogo(frame, new, 0, 0)
		rows,cols,channels = lose.shape
		InsertLogo(frame, lose2, 0, 0)
		cv2.putText(frame,"Restart",(275,430), font, 1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(125, 400),(225,450),(0,255,0),-1)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.imshow('frame',frame)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
