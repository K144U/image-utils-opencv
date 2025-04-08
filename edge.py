import os 
import cv2
import numpy as np

img = cv2.imread("bala.png")
img_edge = cv2.Canny(img, 100, 200)

img_dil = cv2.dilate(img_edge , np.ones((5,5), dtype=np.uint8))
img_erode = cv2.erode(img_edge , np.ones((5,5), dtype=np.uint8))


cv2.imshow ('img_edge', img_edge)
cv2.imshow ('img_dil', img_dil)
cv2.imshow ('img_erode', img_erode)

cv2.waitKey(0)
cv2.destroyAllWindows()