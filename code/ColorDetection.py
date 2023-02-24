import numpy as np
import cv2


cap = cv2.VideoCapture(0) # co the dat duong dan den tep vid muon tai len

while True:
	ret, frame = cap.read() # ret kiem tra camera , frame la hien thi tung khung hinh
	width = int(cap.get(3)) # 3 la thuoc tinh chieu cao (y)
	height = int(cap.get(4)) # 4 la thuoc tinh chieu rong (x)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # chuyen anh dang BGR sang hsv
	lower_blue = np.array([90, 50, 50]) # chon khoang mau blue duoi
	upper_blue = np.array([130, 255, 255]) # chon klhoang mau blue tren

	mask = cv2.inRange(hsv, lower_blue, upper_blue) # tao mat na gioi han cac mau blue trong khoang da chon

	result = cv2.bitwise_and(frame, frame, mask=mask) # su dung bitwise giu lai cac pixel mau bule trong khoang da chon

	cv2.imshow('frame', result)
	cv2.imshow('mask', mask) # neu co mau bule trong khoang thi mask hien thi bit 1 (mau trang), neu ko phai blue trong khoang thi hien thi 0 (mau den)


	if cv2.waitKey(1) == ord('q'): # an q de thoat khoi video
		break

cap.release()
cap.destroyAllWindows()