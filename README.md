## 🛒  OCR Product Scanner

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![EasyOCR](https://img.shields.io/badge/OCR-EasyOCR-00BFFF)](https://github.com/JaidedAI/EasyOCR)
[![Open Food Facts](https://img.shields.io/badge/API-Open%20Food%20Facts-green)](https://world.openfoodfacts.org/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

An intelligent OCR-based solution that scans product labels and retrieves detailed product information from the Open Food Facts database. Perfect for health-conscious consumers and food enthusiasts!

[demo video](https://github.com/user-attachments/assets/9800f808-36dd-4342-9b39-f6d146e2d2b2)

##  Features

- **Smart OCR Processing**: Advanced text extraction with noise removal
- **Multi-Search Strategy**: Barcode + text search with 4-tier fallback
- **Nutrition Insight**: Key nutritional facts display
- **Error-Resilient**: Handles poor quality images and missing products
- **User-Friendly UI**: Simple drag-and-drop interface

##  How I Solved the Problem

### Approach to Requirements
| Requirement | Our Solution |
|-------------|--------------|
| **OCR Module** | EasyOCR with text cleaning & barcode extraction |
| **Data Retrieval** | 4-tier API search strategy with fallbacks |
| **Output Interface** | Streamlit web app with detailed product display |
| **Error Handling** | Graceful degradation with user guidance |
| **Edge Cases** | Multi-stage matching for partial information |

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.comAkashDevelop/ocr_product_scanner.git
cd ocr_scanner


