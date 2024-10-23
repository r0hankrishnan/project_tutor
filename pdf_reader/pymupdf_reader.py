import pymupdf
import numpy as np
import pandas as pd

doc = pymupdf.open("./pdf_reader/data/islp_sample.pdf") # open a document

all_text = []
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    all_text.append([page_num + 1, text])


for page_num, text in all_text[0:2]:
    print(page_num)
