import fitz # pyMuPDF

def extract_text_from_pdf(ruta_pdf:str) -> str:
    # Open the PDF file
    doc = fitz.open(ruta_pdf)
    
    # Initialize an empty string to hold the extracted text
    extracted_text = ""
    
    # Iterate through each page in the PDF
    
    for pagina in doc:
        extracted_text += pagina.get_text()  # Extract text and append to the result

    #for page_num in range(len(doc)):
    #    page = doc.load_page(page_num)  # Load the page
    #    extracted_text += page.get_text()  # Extract text and append to the result
    
    return extracted_text