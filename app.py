import streamlit as st
from ocr_processor import extract_info
from api_client import fetch_product

def main():
    st.title("🛒 Advanced OCR Product Scanner")
    uploaded_file = st.file_uploader("Upload product image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        #  saving the img and process further
        with open("temp_img.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Extract information
        info = extract_info("temp_img.jpg")
        
        # Display extraction results
        st.subheader("🔍 Extracted Information")
        st.info(f"**Raw OCR Text:** {info['raw_text']}")
        st.success(f"**Cleaned Text:** {info['clean_text']}")
        st.write(f"**Detected Brand:** {info['brand']}")
        st.write(f"**Detected Product Name:** {info['product_name']}")
        st.write(f"**Barcodes:** {info['barcodes'] or 'None'}")
        
        # Fetch product data 
        product_data = fetch_product(info)
        display_product_info(product_data)

def display_product_info(product):
    if not product:
        st.error("Product not found in database")
        st.markdown("**Tip:** Try a clearer image or different product")
        st.markdown("Contribute to Open Food Facts: [Add Product](https://world.openfoodfacts.org/add-product)")
        return
    
    # Handle missing datas 
    st.subheader("📦 Product Information")
    st.write(f"**Name:** {product.get('product_name', 'N/A')}")
    st.write(f"**Brand:** {product.get('brands', 'N/A')}")
    st.write(f"**Ingredients:** {product.get('ingredients_text', 'N/A')[:300]}...")
    
    if 'nutriments' in product:
        st.write("**Nutrition Facts (per 100g):**")
        nutrients = product['nutriments']
        st.write(f"- Calories: {nutrients.get('energy-kcal_100g', 'N/A')} kcal")
        st.write(f"- Fat: {nutrients.get('fat_100g', 'N/A')}g")
        st.write(f"- Carbs: {nutrients.get('carbohydrates_100g', 'N/A')}g")
        st.write(f"- Protein: {nutrients.get('proteins_100g', 'N/A')}g")
    
    st.write(f"**Categories:** {product.get('categories', 'N/A')}")


if __name__ == "__main__":
    main()