import re
from PyPDF2 import PdfReader

#finalizado

def __build__(pdf):
    builded_text = concatena_paginas(pega_texto_pdf(pdf))
    return builded_text

def concatena_paginas(lista_de_paginas):
    """Essa função pega todos os itens da lista (lista de páginas) e concatena e uma string, ou seja
    em um único texto.

    Args:
        lista_de_paginas (list): lista das páginas

    Returns:
        string: Texto total do pdf.
    """
    lista_de_paginas_concatenadas = ''
    for item in lista_de_paginas:
        lista_de_paginas_concatenadas = lista_de_paginas_concatenadas + item
    return lista_de_paginas_concatenadas

def pega_texto_pdf(pdf):
    """
    Essa função extrai o texto de todas as páginas do PDF
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
