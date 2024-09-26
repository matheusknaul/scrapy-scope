import re
from PyPDF2 import PdfReader

def pega_texto_pdf(pdf):
    """
    Essa função extrei o texto de todas as páginas do PDF
    escolhido.

    Args:
        pdf (str): Caminho do arquivo.

    Returns:
        list: Uma lista de strings, onde cada string é o texto de uma página do PDF.
    """
    pageList = []
    with open(pdf,'rb') as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            page_text = page.extract_text().replace('\n','')
            pageList.append(page_text)
    return pageList