#pip install fitz

# Importing required modules
import fitz

# Opening the PDF file
doc = fitz.open('./pdf_reader/islp_sample.pdf')

# Extracting text from all pages
all_text = []
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    all_text.append([page_num + 1, text])