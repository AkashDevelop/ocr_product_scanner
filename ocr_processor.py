import easyocr
from text_cleaner import clean_product_text, extract_keywords
import re

def extract_info(image_path):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path, detail=0)
    raw_text = " ".join(results)
    
    # Clean and extract the info we did
    clean_text = clean_product_text(raw_text)
    brand, product_name = extract_keywords(clean_text)
    
    # Barcode detection
    barcodes = re.findall(r'\b(\d{12,13})\b', raw_text)
    
    return {
        "raw_text": raw_text,
        "clean_text": clean_text,
        "brand": brand,
        "product_name": product_name,
        "barcodes": barcodes
    }