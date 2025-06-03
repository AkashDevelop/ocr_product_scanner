import re

def clean_product_text(text):
    # Remove quantities 
    text = re.sub(r'\d+\s*(ml|g|kg|oz|l|lb|fl\.?)\b', '', text, flags=re.IGNORECASE)
    
    # Remove special characters 
    text = re.sub(r'[^\w\s]', '', text)
    
    text = re.sub(r'\b\d+\b', '', text)
    
    # Remove non-product words
    stop_phrases = ['net wt', 'net weight', 'volume', 'best before', 'expiry']
    for phrase in stop_phrases:
        text = text.replace(phrase, '')
    
    # whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def extract_keywords(text):
    # extract brand and product details
    words = text.split()
    if not words:
        return "", ""
    
    # assign the first word is brand 
    brand = words[0]
    
    # Find longest  product name
    product_phrase = ""
    current_phrase = ""
    
    for word in words[1:]:
        if word.isupper() or len(word) > 3:
            current_phrase += f"{word} "
        else:
            if len(current_phrase) > len(product_phrase):
                product_phrase = current_phrase
            current_phrase = ""
    
    # Fial checking 
    product_phrase = product_phrase or current_phrase or " ".join(words[1:min(4, len(words))])
    
    return brand, product_phrase.strip()