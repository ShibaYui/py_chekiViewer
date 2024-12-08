##	Filename: view_demo.py
##	Author: yu1
##	Date: 2024-12-08 13:52:13 +0800
## 
##	Description:
## 

import cv2

img_source=["demo.jpg"]

for i, path in enumerate(img_source):
	img=cv2.imread(path)
	window_name = f"Image {i+1}"
	cv2.imshow(window_name, img)


## key for close pic
cv2.waitKey(0)
cv2.destoryAllWindows()
