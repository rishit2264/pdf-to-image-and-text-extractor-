'''import re
from pdfminer.high_level import extract_pages, extract_text'''

'''for page_layout in extract_pages("sample-1.pdf"):
    for element in page_layout:
        print(element)'''
'''text = extract_text("s5.pdf")
print(text)

pattern = re.compile(r"[a-zA-Z]+")
matches = pattern.findall(text)
print(matches)

names = [n[:-2] for n in matches]
print(names)'''

'''import re
from pdfminer.high_level import extract_pages, extract_text

for page_layout in extract_pages("sample-1.pdf"):
    for element in page_layout:
        print(element)'''
'''text = extract_text("s5.pdf")
print(text)

pattern = re.compile(r"[a-zA-Z]+")
matches = pattern.findall(text)
print(matches)

pattern1 = re.compile(r"\(\d{3}\)-\d{3}-\d{4}|\d{10}")
matches1 = pattern1.findall(text)
print(matches1)'''
import re
import pandas as pd
from pdfminer.high_level import extract_text

try:
    # Extract text from PDF
    text = extract_text("s5.pdf")
    print("Extracted text preview:")
    print(text[:1000])  # Print only the first 1000 characters for a preview

    # Create a DataFrame for the entire text
    df_text = pd.DataFrame({'Text': [text]})
    df_text.to_csv('extracted_text.csv', index=False)

    # Find words
    pattern = re.compile(r"[a-zA-Z]+")
    words = pattern.findall(text)
    
    # Create a DataFrame for words
    df_words = pd.DataFrame({'Words': words})
    df_words.to_csv('words.csv', index=False)

    # Find phone numbers
    pattern1 = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    phone_numbers = pattern1.findall(text)
    
    # Create a DataFrame for phone numbers
    df_phone_numbers = pd.DataFrame({'Phone Numbers': phone_numbers})
    df_phone_numbers.to_csv('phone_numbers.csv', index=False)

    print("DataFrames have been saved to CSV files.")

except Exception as e:
    print(f"An error occurred: {e}")
