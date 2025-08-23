import cv2

img = cv2.imread('sarav_img_1.jpg')

cv2.imshow('Image - Saravanan', img)

window_name = 'Rotated Image'
img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, img_rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()