from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image_path = 'image_text.jpeg'
image = Image.open(image_path)

# Extract text from the image in multiple languages
text = pytesseract.image_to_string(image, lang='eng+fra+deu+esp+ita')

# Print the extracted text
print(text)