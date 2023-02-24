import cv2

img = cv2.imread("../code/window.jpg", -1)
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2) # thay doi kich thuoc size anh
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) # xoay anh

cv2.imwrite('new_img.jpg', img) # luu anh moi

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()