import re

# ABNT E ISO
PATTERN_1 = r"\s([A-Z]{3,4}\s){1,4}\d{2,5}" #
PATTERN_2 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}" #
PATTERN_3 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}" #Ex ABNT NBR ISO 17025 / 2025 ()
PATTERN_4 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sParte\s\d" #Ex ABNT NBR ISO 17025 / 2025 - Parte 3 ()
PATTERN_5 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sPartes\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 2025 - Partes 3 e 4 ()
PATTERN_6 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sPartes\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 20 25 - Partes 3 e 4 ()
PATTERN_7 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sPartes\s\d+,\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 2025 - Partes 2, 3 e 4 ()
PATTERN_8 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sPartes\s\d+,\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 20 25 - Partes 2, 3 e 4 ()
PATTERN_9 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d" # Ex ABNT NBR ISO 7206-4
PATTERN_10 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}" # Ex ABNT NBR ISO 7206-4:2024
PATTERN_11 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}\sEmenda\s\d{1}+:\d{2,4}" # Ex ABNT NBR ISO 7206-4:2012 Emenda 1:2016
PATTERN_12 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\sParte\s\d{1}" #Ex ABNT NBR ISO 17025 / 2025 Parte 3 
PATTERN_13 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}" # Ex ABNT NBR ISO 7206-4:2024
PATTERN_14 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}\sVersão\scorrigida+:\d{4}" # Ex ABNT NBR ISO 7206-4:2012 Versão corrigida:2016
PATTERN_15 = r"\s([A-Z]{3}/[A-Z]{2}\s\d{2,5}\s/\s\d{4})" # Ex ISO/TS 13498 / 2011
PATTERN_16 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\sParte\s\d{1}:\d{4}" # Ex ABNT NBR 15669 Parte 1:2009
PATTERN_17 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}\sParte\s\d{1}" # Ex ABNT NBR 15669:2009 Parte 3
PATTERN_18 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}" # Ex ABNT NBR NM 88:2000
PATTERN_19 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d/\d{4}" # Ex ABNT NBR ISO 7206-4/2024
PATTERN_20 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+/\d{4}" # Ex ABNT NBR ISO 7206/2024
PATTERN_21 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\d{1}\s+/\s\d{4}" # Ex ABNT NBR ISO 7206-4 / 2024
PATTERN_22 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}+-\s\d{1}+:\d{4}" # Ex ABNT NBR ISO 7206- 4:2024
PATTERN_23 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\s\d{4}" # Ex ABNT NBR NM 88: 2000
PATTERN_24 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}\sErrata\s\d{1}+:\d{4}" # Ex ABNT NBR NM 87:2000 Errata 2:2004
PATTERN_25 = r"\s([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s+-\sParte\d{1}" #Ex ABNT NBR ISO 17025 / 2025 - Parte3 
PATTERN_26 = r"\s([A-Z]{2,4}\s){1,4}/[A-Z]{2,5}\s\d{2,5}+:\d{4}" #Ex ABNT NBT IEC /CISPR 25:2010 
PATTERN_27 = r"\s([A-Z]{2,4}\s){1,4}[A-Z]{2,5}/[A-Z]{2,5}\s\d{2,5}:\d{4}" #Ex ABNT NBT IEC/CISPR 25:2010
# ASTM
PATTERN_28 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}" # Ex ASTM E112
PATTERN_29 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}+:\d{2,4}" # Ex ASTM E112:2022
PATTERN_30 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}[a-z]{1}\d{1}" # Ex ASTM F1264 / 2016e1
PATTERN_31 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}\s[a-z]{1}\d{1}" # Ex ASTM F1264 / 2016 e1
PATTERN_32 = r"\s([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\s\(Reaprovada\s\d{4}\)" # Ex ASTM E112:2022 (Reaprovada 2020)
PATTERN_33 = r"\s([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\s\(Reaprovada\s\d{4}\)[a-z]{1}\d{1}" # Ex ASTM E112:2022 (Reaprovada 2020)e1
PATTERN_34 = r"\s([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\sReapproved\s\d{4}" # Ex ASTM E112:2013 Reapproved 2021
PATTERN_35 = r"\s([A-Z]{4}\s)[A-Z]{1}\d{2,5}+:\d{2,4}[a-z]{1}" # Ex ASTM E112:2022a

list_of_patterns = [
                    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4, PATTERN_5,
                    PATTERN_6, PATTERN_7, PATTERN_8, PATTERN_9, PATTERN_10,
                    PATTERN_11, PATTERN_12, PATTERN_13, PATTERN_14, PATTERN_15,
                    PATTERN_16, PATTERN_17, PATTERN_18, PATTERN_19, PATTERN_20,
                    PATTERN_21, PATTERN_22, PATTERN_23, PATTERN_24, PATTERN_25,
                    PATTERN_26, PATTERN_27, PATTERN_28, PATTERN_29, PATTERN_30,
                    PATTERN_31, PATTERN_32, PATTERN_33, PATTERN_34, PATTERN_35
                   ]

#Test

text = "Cara estou aqui pensando em fazer um teste kkkk ABNT NBR ISO 17025 Eu estou pensando em acreditar o laboratório na ABNT NBT IEC/CISPR 25:2010 A AAAAAAAAAAAAAAAAAAA"

lista_de_resultados = []
for pattern in list_of_patterns:
    resultado = re.finditer(pattern, text)
    lista_de_resultados.append(resultado)

resultado_dos_resultados = []
for resultado in lista_de_resultados:
    for match in resultado:
        resultado_final = []
        print(match)

#Pegar apenas o último
#IF MATCH OTHER PATTERN TEXT = ""
