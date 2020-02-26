import cv2

cam = cv2.VideoCapture(0)

while True:
	ret, frame = cam.read()
	cv2.imshow('frame', frame)
	wait = cv2.waitKey(1)
	
	if wait == 27:
		break

cv2.destroyAllWindows()
cam.release()
