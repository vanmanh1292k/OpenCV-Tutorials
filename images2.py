import cv2
import random

img = cv2.imread('../code/new_img.jpg', -1)

print(img.shape) # in chieu cao, chieu rong, va so chieu dai mau dai dien cho moi pixel(do, xanh la cay, xanh lam)
# blue, green,  red
# [128, 0, 0] : mau xanh nhat
# 0-255


#thay doi pixel trong anh
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


#sao chep va dan 1 phan hinh anh
tag = img[200:300, 500:700]
img[50:150, 100:300] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


