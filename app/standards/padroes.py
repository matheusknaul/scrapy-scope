import re

# Pattern Tag

PATTERN_ABNT = r"ABNT"
PATTERN_ISO = r"ISO"
PATTERN_ASTM = r"ASTM"

list_of_tagpatterns = [
                    PATTERN_ABNT, PATTERN_ISO, PATTERN_ASTM
]

# Pattern Number

PATTERN_NUMBER_1 = r"[A-Z]{2,5}\s\d{2,5}" # Ex ISO 17025
PATTERN_NUMBER_2 = r"[A-Z]{1}\d{2,5}" # Ex E112

list_of_numberpatterns = [
                    PATTERN_NUMBER_1, PATTERN_NUMBER_2
]

# Pattern Part

PATTERN_PART_1 = r"Parte\d{1}" # Ex Parte3 
PATTERN_PART_2 = r"-\s\d{1}" # Ex 7206- 4
PATTERN_PART_3 = r"-\d{1}" # Ex 7206-4
PATTERN_PART_4 = r"Parte\s\d{1}" # Ex Parte 3
PATTERN_PART_5 = r"Partes\s\d{1},\s\d{1}\se\s\d{1}" # Ex Partes 2, 3 e 4
PATTERN_PART_6 = r"Partes\s\d{1}\se\s\d{1}" # Ex Partes 3 e 4

list_of_partpatterns = [
                    PATTERN_PART_1, PATTERN_PART_2, PATTERN_PART_3, PATTERN_PART_4,
                                    PATTERN_PART_5, PATTERN_PART_6
                   ]

# Pattern Year

PATTERN_YEAR_1 = r"/\s\d{4}" # Ex / 2023
PATTERN_YEAR_2 = r"/\d{4}" # Ex /2023
PATTERN_YEAR_3 = r":\d{4}" # Ex :2023
PATTERN_YEAR_4 = r":\s\d{4}" # Ex : 2023
PATTERN_YEAR_5 = r"/\s\d{2}\s\d{2}" # Ex / 20 20
PATTERN_YEAR_6 = r"/\d{2}\s\d{2}" # Ex /20 20
PATTERN_YEAR_7 = r":\d{2}\s\d{2}" # Ex :20 20
PATTERN_YEAR_8 = r":\s\d{2}\s\d{2}" # Ex : 20 20

list_of_yearpatterns = [
                    PATTERN_YEAR_1, PATTERN_YEAR_2, PATTERN_YEAR_3, PATTERN_YEAR_4,
                    PATTERN_YEAR_5, PATTERN_YEAR_6, PATTERN_YEAR_7, PATTERN_YEAR_8
                   ]

# ABNT E ISO

PATTERN_1 = r"\s([A-Z]{3,4}\s){1,4}\d{2,5}" #
PATTERN_2 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}" #
PATTERN_3 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}" #Ex ABNT NBR ISO 17025 / 2025 ()
PATTERN_4 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sParte\s\d" #Ex ABNT NBR ISO 17025 / 2025 - Parte 3 ()
PATTERN_5 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sPartes\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 2025 - Partes 3 e 4 ()
PATTERN_6 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sPartes\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 20 25 - Partes 3 e 4 () 
PATTERN_7 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sParte\s\d{1}" #Ex ABNT NBR 15712 / 20 09 - Parte 3
PATTERN_8 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sPartes\s\d+,\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 2025 - Partes 2, 3 e 4 ()
PATTERN_9 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sPartes\s\d+,\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 20 25 - Partes 2, 3 e 4 ()
PATTERN_10 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d" # Ex ABNT NBR ISO 7206-4
PATTERN_11 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}" # Ex ABNT NBR ISO 7206-4:2024
PATTERN_12 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}\sEmenda\s\d{1}+:\d{2,4}" # Ex ABNT NBR ISO 7206-4:2012 Emenda 1:2016
PATTERN_13 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\sParte\s\d{1}" #Ex ABNT NBR ISO 17025 / 2025 Parte 3 
PATTERN_14 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}" # Ex ABNT NBR ISO 7206-4:2024
PATTERN_15 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}\sVersão\scorrigida+:\d{4}" # Ex ABNT NBR ISO 7206-4:2012 Versão corrigida:2016
PATTERN_16 = r"\s([A-Z]{3}/[A-Z]{2}\s\d{2,5}\s/\s\d{4})" # Ex ISO/TS 13498 / 2011
PATTERN_17 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\sParte\s\d{1}:\d{4}" # Ex ABNT NBR 15669 Parte 1:2009
PATTERN_18 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}\sParte\s\d{1}" # Ex ABNT NBR 15669:2009 Parte 3
PATTERN_19 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}" # Ex ABNT NBR NM 88:2000
PATTERN_20 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d/\d{4}" # Ex ABNT NBR ISO 7206-4/2024
PATTERN_21 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+/\d{4}" # Ex ABNT NBR ISO 7206/2024
PATTERN_22 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d{1}\s+/\s\d{4}" # Ex ABNT NBR ISO 7206-4 / 2024
PATTERN_23 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\s\d{1}+:\d{4}" # Ex ABNT NBR ISO 7206- 4:2024
PATTERN_24 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\s\d{4}" # Ex ABNT NBR NM 88: 2000
PATTERN_25 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}\sErrata\s\d{1}+:\d{4}" # Ex ABNT NBR NM 87:2000 Errata 2:2004
PATTERN_26 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s+-\sParte\d{1}" #Ex ABNT NBR ISO 17025 / 2025 - Parte3 
PATTERN_27 = r"\s([A-Z]{2,4}\s){1,4}/[A-Z]{2,5}\s\d{2,5}+:\d{4}" #Ex ABNT NBT IEC /CISPR 25:2010 
PATTERN_28 = r"\s([A-Z]{2,4}\s){1,4}[A-Z]{2,5}/[A-Z]{2,5}\s\d{2,5}:\d{4}" #Ex ABNT NBT IEC/CISPR 25:2010

# ASTM

PATTERN_29 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}" # Ex ASTM E112
PATTERN_30 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}+:\d{2,4}" # Ex ASTM E112:2022
PATTERN_31 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}[a-z]{1}\d{1}" # Ex ASTM F1264 / 2016e1
PATTERN_32 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}" # Ex ASTM F1264 / 2016
PATTERN_33 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}\s[a-z]{1}\d{1}" # Ex ASTM F1264 / 2016 e1
PATTERN_34 = r"\s([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\s\(Reaprovada\s\d{4}\)" # Ex ASTM E112:2022 (Reaprovada 2020)
PATTERN_35 = r"\s([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\s\(Reaprovada\s\d{4}\)[a-z]{1}\d{1}" # Ex ASTM E112:2022 (Reaprovada 2020)e1
PATTERN_36 = r"\s([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\sReapproved\s\d{4}" # Ex ASTM E112:2013 Reapproved 2021
PATTERN_37 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}+:\d{2,4}[a-z]{1}" # Ex ASTM E112:2022a

list_of_patterns = [
                    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4, PATTERN_5,
                    PATTERN_6, PATTERN_7, PATTERN_8, PATTERN_9, PATTERN_10,
                    PATTERN_11, PATTERN_12, PATTERN_13, PATTERN_14, PATTERN_15,
                    PATTERN_16, PATTERN_17, PATTERN_18, PATTERN_19, PATTERN_20,
                    PATTERN_21, PATTERN_22, PATTERN_23, PATTERN_24, PATTERN_25,
                    PATTERN_26, PATTERN_27, PATTERN_28, PATTERN_29, PATTERN_30,
                    PATTERN_31, PATTERN_32, PATTERN_33, PATTERN_34, PATTERN_35,
                    PATTERN_36, PATTERN_37
                   ]

#Test

text = " Determinação da resistência à compressão - até 100 kN ABNT NBR 15712 / 2014 - Partes 1 e 2  ASTM F2077:2022 - item 6.3, 8 e 9  Determinação da resistência ao cisalhamento - até 100 kN ABNT NBR 15712 / 2014 - Partes 1 e 2  ASTM F2077:2022 – item 6.4, 8 e 9  Determinação da resistência à torção - até 200 Nm ABNT NBR 15712 / 2014 - Partes 1 e 2  ASTM F2077:2022 – item 6.5, 8 e 9  Resistência à penetração devido à compressão axial - até 100 kN  ABNT NBR 15712 / 20 09 - Parte 3 ASTM F2267:2022 BARRAS DE COLUNA"

def build_standard(standard):
    result = []
    main_tag, complementar_tag = detect_tag(standard)
    number = detect_number(standard)
    part = detect_part(standard)
    year = detect_year(standard)

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
            result = re.search(r"\d{2,5}", match.group())
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

print(detect_tag("ABNT NBR ISO 17025 Parte 2 :2220"))