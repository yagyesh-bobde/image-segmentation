import cv2
import matplotlib.pyplot as plt
import numpy as np

# write code to read and show image file using cv2
# set the window dimensions to 800x600


img = cv2.imread('map.jpg')
nemo = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_nemo)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()


cv2.imshow('image', img)
cv2.imshow('nemo', nemo)
cv2.waitKey(0)