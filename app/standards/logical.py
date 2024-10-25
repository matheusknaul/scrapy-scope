import re
from padroes import list_of_patterns, list_of_yearpatterns, list_of_partpatterns, list_of_numberpatterns

def build_standard(standard):
    result = []
    main_tag, complementar_tag = detect_tag(standard)
    number = detect_number(standard)
    part = detect_part(standard)
    year = detect_year(standard)

    result.append([main_tag, complementar_tag])
    result.append(number)
    if part:
        result.append(part)
    result.append(year)

    return result

def detect_tag(standard):

    if "ABNT" in standard:
        main_tag = "ABNT"
        complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
        complementar_tag = complementar.group().replace("ABNT", "")
        return main_tag, complementar_tag

    if "ISO" in standard:
        main_tag = "ISO"
        complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
        complementar_tag = complementar.group().replace("ISO", "")
        return main_tag, complementar_tag
    
    if "ASTM" in standard:
        main_tag = "ASTM"
        complementar = re.search(r"([A-Z]{2,5}\s){1,4}", standard)
        complementar_tag = complementar.group().replace("ASTM", "")
        return main_tag, complementar_tag

def detect_number(standard):
    
    for pattern in list_of_numberpatterns:
        match = re.search(pattern, standard)
        if match:
            result = re.search(r"[A-Z]{1}\d{2,5}|\d{2,5}", match.group())
            if result: 
                return result.group()

def detect_part(standard):
    parts = []
    for pattern in list_of_partpatterns:
        match = re.search(pattern, standard)
        if match:
            number_part = re.finditer(r"\d{1}", match.group())
            if number_part:
                for number in number_part:
                    parts.append(number.group())
    return parts

def detect_year(standard):
    year_concatened = ""
    for pattern in list_of_yearpatterns:
        match = re.search(pattern, standard)
        if match:
            year_match = re.finditer(r"\d", match.group())
            if year_match:
                for year in year_match:
                    year_concatened = year_concatened + year.group()
    return year_concatened

def __init__(text):
    lista_resultados = search_patterns(text)
    lista_interval = set_interval(lista_resultados, text)
    format_standard(lista_interval)

def search_patterns(text):
    lista_de_matchs = []

    # Ordenar os padrões pela complexidade (padrões maiores primeiro)
    list_of_patterns_sorted = sorted(list_of_patterns, key=lambda p: -len(p))

    for pattern in list_of_patterns_sorted:
        resultados = re.finditer(pattern, text)
        for match in resultados:
            title, start, end = match.group(), match.start(), match.end()
            
            sobreposto = False

            # Verifica se a nova norma detectada está sobrepondo uma já existente
            for item in lista_de_matchs:
                start_anterior = item[1][0]
                end_anterior = item[1][1]

                # Verificar se há sobreposição com o intervalo de um item já detectado
                if start >= start_anterior and end <= end_anterior:
                    sobreposto = True
                    break

            # Se não houver sobreposição, adicionamos a nova norma
            if not sobreposto:
                lista_de_matchs.append([title, [start, end]])

    return lista_de_matchs

def set_interval(list_results, text):
    lista_ordenada = sort_list(list_results)
    result = []

    for i, norma_atual in enumerate(lista_ordenada):
        start_norma_atual = norma_atual[1][0]
        nome_norma_atual = norma_atual[0]

        # Determina o intervalo do texto anterior à norma atual
        if i == 0:
            # Se for a primeira norma, pegue o texto desde o início
            bloco_anterior = text[:start_norma_atual].strip()
        else:
            # Pegue o texto desde o final da norma anterior até o início da norma atual
            end_norma_anterior = lista_ordenada[i-1][1][1]
            bloco_anterior = text[end_norma_anterior:start_norma_atual].strip()

        # Adiciona o bloco de texto e a norma à lista de resultados
        result.append([bloco_anterior, nome_norma_atual])

    return result
    
def format_standard(list_results):
    for result in list_results:
        print(result[1])

def sort_list(list_results):
    lista_ordenada = sorted(list_results, key=lambda x: x[1][0])
    return lista_ordenada


print(build_standard("ABNT NBR ISO 17232 Partes 2, 3 e 4:2025"))