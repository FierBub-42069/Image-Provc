import csv
from PIL import Image, ImageFilter
import pytesseract
import cv2
import numpy as np
import pandas as pd

def rgb(imgName, imgExt):
	im = Image.open(imgName+"."+imgExt)
	rgb_im = im.convert('RGB')
	rgb_data = list(rgb_im.getdata())
	rgb_df = pd.DataFrame(rgb_data, columns=["R", "G", "B"])
	file_=imgName+"_rgb.csv"
	rgb_df.to_csv(file_, index=False)

def hsv(imgName, imgExt):
	image = Image.open(imgName+"."+imgExt)
	hsv_im = image.convert('HSV')
	hsv_data = list(hsv_im.getdata())
	hsv_df = pd.DataFrame(hsv_data, columns=["H", "S", "V"])
	file_=imgName+"_hsv.csv"
	hsv_df.to_csv(file_, index=False)

def gray(imgName, imgExt):
	im = Image.open(imgName+"."+imgExt)
	gray_im = im.convert("L")
	gray_data = list(gray_im.getdata())
	gray_df = pd.DataFrame(gray_data, columns=["gray"])
	file_=imgName+"_gray.csv"
	gray_df.to_csv(file_, index=False)

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
	print("\n1.RGB\n2.HSV\n3.Grayscale\n4.Apply Filter\n5.Exit")
	ch=int(input("\tEnter your choice:\t"))
	match ch:
		case 1:
			rgb(imgName, imgExt)
		case 2:
			hsv(imgName, imgExt)
		case 3:
			gray(imgName, imgExt)
		case 4:
			filter_(imgName, imgExt)
		case 5:
			exit()
main()
	
