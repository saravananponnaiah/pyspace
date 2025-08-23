import cv2

cap = cv2.VideoCapture(0)
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray.tofile("D:\\Workspace\\Pycharm\\pyspace\\opencv\\capture_image.jpg")