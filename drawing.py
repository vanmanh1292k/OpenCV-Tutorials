import numpy as np
import cv2

#recognizer=cv2.face.EigenFaceRecognizer_create()

cap = cv2.VideoCapture(0) # co the dat duong dan den tep vid muon tai len

while True:
	ret, frame = cap.read() # ret kiem tra camera , frame la hien thi tung khung hinh
	width = int(cap.get(3)) # 3 la thuoc tinh chieu cao (y)
	height = int(cap.get(4)) # 4 la thuoc tinh chieu rong (x)

	img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) # duong cheo \
	img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10) # duong cheo /
	img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5) # hinh chu nhat
	img = cv2.circle(img, (400, 400), 60, (0, 0, 255), 5) # hinh tron
	font = cv2.FONT_HERSHEY_SIMPLEX # set font
	img = cv2.putText(img, 'Manh dep trai', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA) # text

	cv2.imshow('frame', img)

	if cv2.waitKey(1) == ord('q'): # an q de thoat khoi video
		break

cap.release()
cap.destroyAllWindows()