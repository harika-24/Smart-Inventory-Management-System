from PIL import Image
import pytesseract
import cv2
import numpy as np

img = cv2.imread("F:\\Final year project\\Images\\amul.jpeg")

text=pytesseract.image_to_string(img)
print(text)
