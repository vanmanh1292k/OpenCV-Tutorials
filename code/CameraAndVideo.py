import numpy as np
import cv2


cap = cv2.VideoCapture(0) # co the dat duong dan den tep vid muon tai len

while True:
	ret, frame = cap.read() # ret kiem tra camera , frame la hien thi tung khung hinh
	width = int(cap.get(3)) # 3 la thuoc tinh chieu cao
	height = int(cap.get(4)) # 4 la thuoc tinh chieu rong

	image = np.zeros(frame.shape, np.uint8)
	smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
	image[:height//2, :width//2] = smaller_frame # tren cung ben trai 
	image[height//2:, :width//2] = smaller_frame # duoi cung ben trai
	image[:height//2, width//2:] = smaller_frame # tren cung ben phai 
	image[height//2:, width//2:] = smaller_frame # duoi cung ben phai


	cv2.imshow('frame', image)

	if cv2.waitKey(1) == ord('q'): # an q de thoat khoi video
		break

cap.release()
cap.destroyAllWindows()