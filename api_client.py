import requests

def fetch_product(info):
    """Multi-step search strategy"""
    # barcode search first
    for barcode in info['barcodes']:
        product = fetch_by_barcode(barcode)
        if product:
            return product
    
    # incase Try brand + product name search
    if info['brand'] and info['product_name']:
        product = fetch_by_query(f"{info['brand']} {info['product_name']}")
        if product:
            return product
    
    # Trying product name only
    if info['product_name']:
        product = fetch_by_query(info['product_name'])
        if product:
            return product
    
    # Fallback to brand search
    if info['brand']:
        return fetch_by_query(info['brand'])
    
    return None

def fetch_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()
    return data.get('product') if data.get('status') == 1 else None

def fetch_by_query(query):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&sort_by=unique_scans_n&json=1"
    response = requests.get(url)
    products = response.json().get('products', [])
    return products[0] if products else None