import numpy as np
import cv2


cap = cv2.VideoCapture(0) # co the dat duong dan den tep vid muon tai len
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True:
	ret, frame = cap.read() # ret kiem tra camera , frame la hien thi tung khung hinh
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 20)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 4)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 20)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 4)

	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'): # an q de thoat khoi video
		break

cap.release()
cap.destroyAllWindows()