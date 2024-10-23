import pytesseract
import PIL

img = PIL.Image.open("./pdf_reader/data/islp_sample.png")

text = pytesseract.image_to_string(img)

print(text)