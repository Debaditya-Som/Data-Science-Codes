#write a python script to enhance the grey scale image using simple histogram equalization technique and display the equalized histogram along with the result image
import cv2
import numpy
from matplotlib import pyplot as plt
inpImg = 'enhance.jpg'
img = cv2.imread(inpImg)
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv,cv2.COLOR_YUV2BGR)
outputImg = 'result.jpg'
cv2.imwrite(outputImg, hist_equalization_result)
inpImg = 'result.jpg'
img = cv2.imread(inpImg, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Result',img)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for the image')
plt.show()
while True:
	k = cv2.waitKey(0) & 0xFF
	if k == 27: break
cv2.destroyAllWindows()
