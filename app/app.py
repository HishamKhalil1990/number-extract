from utilities import get_IDs_from_img
import cv2

img_path = "img/two.jpg"
pytesseract_path = "C:\Program Files (x86)\Tesseract-OCR"
id, card_id = get_IDs_from_img(img_path, pytesseract_path)
print(id, card_id)
