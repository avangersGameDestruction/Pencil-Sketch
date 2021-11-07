import cv2

# Load the image
image = cv2.imread('imgs/cat.png')

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image invert
inv = 255 - gray

# use gausian filter
gaus = cv2.GaussianBlur(inv, (5, 5), 0)

# invert te blur to the image
final = 255 - gaus

# divide the image 
div = cv2.divide(gray, final, scale=255.0)

# show the image edited 
cv2.imshow('image', div)

# wait for the key to be pressed
cv2.waitKey(0)