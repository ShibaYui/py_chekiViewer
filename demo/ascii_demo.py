##	Filename: ascii_demo.py
##	Author: yu1
##	Date: 2024-12-08 15:24:08 +0800
## 
##	Description:
## 


from PIL import Image
import numpy as np

def image_to_ascii(image_path, width=72):
	
	#read image, return PIL.Image（轉灰階）
    img = Image.open(image_path).convert('L')

	#確定並維持圖片長寬比
    aspect_ratio = img.height / img.width
    new_width = width
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))
    pixels = np.array(img)

	#定義灰階，以字元形式（字元左->右，對應暗->亮）
    chars = np.array(list(" .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"))
    #chars = np.array(list("$@B%8&WM#*oahkbpdqwZmO0QLCJUYXzcvunxrjft\\/|()1}{][?-_+~i!lI;:,\"^`'. "))
	
	#定義灰階，
	#1~3 (255/85)
	#1~5 (255/51)
	#1~7 (255/36)
    ascii_art = "\n".join("".join(chars[pixel // 51] for pixel in row) for row in pixels)
    print(ascii_art)

image_to_ascii("YahaUsagi.webp")
