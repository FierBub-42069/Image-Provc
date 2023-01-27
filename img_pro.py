import csv
from PIL import Image, ImageFilter
import pytesseract
import cv2
import numpy as np

def rgb(imgName, imgExt):
	image = Image.open(imgName+"."+imgExt)
	width, height = image.size
	data = []
	for y in range(height):
    		for x in range(width):
    			pixel = image.getpixel((x, y))
    			data.append(pixel)

	file_=imgName+"_rgb.csv"
	with open(file_, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["Red", "Green", "Blue"])
		writer.writerows(data)

def ocr_hsv(imgName, imgExt):
	image = Image.open(imgName+"."+imgExt)
	gray = image.convert('L')
	ocr_text = pytesseract.image_to_string(gray)
	hsv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
	data = []
	height, width, _ = hsv.shape
	for y in range(height):
    		for x in range(width):
    			h, s, v = hsv[y, x]
    			data.append([ocr_text, h, s, v])
	
	file_=imgName+"_ocr_hsv.csv"
	with open(file_, "w", newline="") as f:
    		writer = csv.writer(f)
    		writer.writerow(["OCR", "Hue", "Saturation", "Value"])
    		writer.writerows(data)

def filter_(imgName, imgExt):
	img = Image.open(imgName+"."+imgExt)
	
	img_sharpen = img.filter(ImageFilter.SHARPEN)
	img_sharpen.save(imgName+"_sharpen."+imgExt)
	
	img_blur = img.filter(ImageFilter.BLUR)
	img_blur.save(imgName+"_blur."+imgExt)
	
	img_contour = img.filter(ImageFilter.CONTOUR)
	img_contour.save(imgName+"_contour."+imgExt)
	
	img_edges = img.filter(ImageFilter.FIND_EDGES)
	img_edges.save(imgName+"_edges."+imgExt)
	
	img_bw = img.convert('L')
	img_bw.save(imgName+"_bw."+imgExt)

def main():
	imgName=input("Enter image name:\t")
	imgExt=input("Enter image extension:\t")
	print("\n1.RGB\n2.OCR and CSV\n3.Apply Filter\n4.Exit")
	ch=int(input("\tEnter your choice:\t"))
	match ch:
		case 1:
			rgb(imgName, imgExt)
		case 2:
			ocr_hsv(imgName, imgExt)
		case 3:
			filter_(imgName, imgExt)
		case 4:
			exit()
main()
	
