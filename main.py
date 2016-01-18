import cv2
factor=int(input("Enter FPS:"))
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, factor, (640,480))
cap=cv2.VideoCapture(0)
print cap.get(5)
while(cap.isOpened()):
	ret,frame=cap.read()
	if ret:
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == 27:
			break
	else:
		break
		


		
print cap.get(5)		
cap.release()
out.release()
cv2.destroyAllWindows()