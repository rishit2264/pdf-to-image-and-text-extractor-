import fitz
import pandas as pd

def extract_text_from_pdf(pdf_path):
    """Extracts text from each page of the PDF."""
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def parse_inventory_text(text):
    """Parses the extracted text into a list of dictionaries."""
    lines = text.strip().split('\n')
    if not lines or len(lines) < 2:
        raise ValueError("The PDF does not contain enough data.")
    
    headers = lines[0].split()  # Assuming the first line is the header
    data = []
    
    for line in lines[1:]:
        if line.strip():  # Skip empty lines
            parts = line.split()
            # Ensure we have enough parts to match headers
            if len(parts) < len(headers):
                raise ValueError(f"Line does not match header format: {line}")
            item = {
                headers[0]: parts[0],  # Assuming first column is customer name
                headers[1]: int(parts[1]),  # Phone Number
                headers[2]: parts[2],  # Location
                headers[3]: parts[3],
            }
            data.append(item)
    return data

def create_excel_sheet(data, output_path):
    """Creates an Excel sheet from the inventory data."""
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)

# Path to your PDF file
pdf_path = 's5.pdf'
pdf_text = extract_text_from_pdf(pdf_path)

# Parse the extracted text
inventory_data = parse_inventory_text(pdf_text)

# Create an Excel sheet
output_path = 'inventory.xlsx'
create_excel_sheet(inventory_data, output_path)

print(f'Inventory data has been written to {output_path}')