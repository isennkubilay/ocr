from PIL import Image
import pytesseract


im = Image.open("/home/kubilay/Downloads/bill/12.png")

text = pytesseract.image_to_string(im, lang='eng')

print(text)