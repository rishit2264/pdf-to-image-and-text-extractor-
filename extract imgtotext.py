import pytesseract
from PIL import Image

# Set the path to the Tesseract executable if it's not in your system PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image_path = 'image_text.jpeg'
img = Image.open(image_path)

# Extract text from the image
text = pytesseract.image_to_string(img,lang = 'eng+fra+tam+hin+bel')

# Print the extracted text
print(text)

# Optionally, save the text to a file
with open('extracted_text.txt', 'w') as file:
    file.write(text)

print("Text extraction complete. Check 'extracted_text.txt' for the result.")