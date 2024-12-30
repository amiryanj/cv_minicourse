import cv2

img = "C:/workspace/cat.jpg"
img = cv2.imread(img, 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow("original", img)
cv2.imshow("edges", edges)
cv2.waitKey(0)