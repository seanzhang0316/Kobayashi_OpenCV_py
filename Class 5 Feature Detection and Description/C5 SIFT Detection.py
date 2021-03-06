import cv2
import numpy as np

img = cv2.imread('Mavic Air Fly.jpeg')

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(grayImg, None)
_, des = sift.compute(grayImg, kp)
# kp, des = sift.detectAndCompute(grayImg, None)

# cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.drawKeypoints(img, kp, img)
cv2.imshow('Key Points', img)


cv2.waitKey()
cv2.destroyAllWindows()
