import fitz  # PyMuPDF


def extraer_texto(ruta_pdf: str) -> str:
    doc = fitz.open(ruta_pdf)
    texto = ""

    for pagina in doc:
        texto += pagina.get_text()

    return texto