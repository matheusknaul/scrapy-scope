import re

# ABNT E ISO
PATTERN_1 = r"([A-Z]{3,4}\s){1,4}\d{2,5}" #
PATTERN_2 = r"([A-Z]{2,4}\s){1,4}\d{2,5}" #
PATTERN_3 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}" #Ex ABNT NBR ISO 17025 / 2025 ()
PATTERN_4 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sParte\s\d" #Ex ABNT NBR ISO 17025 / 2025 - Parte 3 ()
PATTERN_5 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sPartes\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 2025 - Partes 3 e 4 ()
PATTERN_6 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sPartes\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 20 25 - Partes 3 e 4 ()
PATTERN_7 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\s-\sPartes\s\d+,\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 2025 - Partes 2, 3 e 4 ()
PATTERN_8 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{2}\s\d{2}\s-\sPartes\s\d+,\s\d\s+e\s+\d" #Ex ABNT NBR ISO 17025 / 20 25 - Partes 2, 3 e 4 ()
PATTERN_9 = r"([A-Z]{2,4}\s){1,4}\d{2,5}+-\d" # Ex ABNT NBR ISO 7206-4
PATTERN_10 = r"([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}" # Ex ABNT NBR ISO 7206-4:2024
PATTERN_11 = r"([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}\sEmenda\s\d{1}+:\d{2,4}" # Ex ABNT NBR ISO 7206-4:2012 Emenda 1:2016
PATTERN_12 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\s/\s\d{4}\sParte\s\d" #Ex ABNT NBR ISO 17025 / 2025 Parte 3 ()
PATTERN_13 = r"([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}" # Ex ABNT NBR ISO 7206-4:2024
PATTERN_14 = r"([A-Z]{2,4}\s){1,4}\d{2,5}+-\d+:\d{4}\sVersão\scorrigida+:\d{4}" # Ex ABNT NBR ISO 7206-4:2012 Versão corrigida:2016
PATTERN_15 = r"([A-Z]{3}/[A-Z]{2}\s\d{2,5}\s/\s\d{4})" # Ex ISO/TS 13498 / 2011
PATTERN_16 = r"([A-Z]{2,4}\s){1,4}\d{2,5}\sParte\s\d{1}:\d{4}" # Ex ABNT NBR 15669 Parte 1:2009
PATTERN_17 = r"([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}\sParte\s\d{1}" # Ex ABNT NBR 15669:2009 Parte 3
PATTERN_18 = r"([A-Z]{2,4}\s){1,4}\d{2,5}:\d{4}" # Ex ABNT NBR NM 88:2000
# ASTM
PATTERN_20 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}" # Ex ASTM E112
PATTERN_21 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}+:\d{2,4}" # Ex ASTM E112:2022
PATTERN_22 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}[a-z]{1}\d{1}" # Ex ASTM F1264 / 2016e1
PATTERN_23 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}\s[a-z]{1}\d{1}" # Ex ASTM F1264 / 2016 e1
PATTERN_24 = r"([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\s\(Reaprovada\s\d{4}\)" # Ex ASTM E112:2022 (Reaprovada 2020)
PATTERN_25 = r"([A-Z]{4}\s[A-Z]\d{2,5}):\d{4}\sReapproved\s\d{4}" # Ex ASTM E112:2013 Reapproved 2021

list_of_patterns = [
                    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4, PATTERN_5,
                    PATTERN_6, PATTERN_7, PATTERN_8, PATTERN_9, PATTERN_10,
                    PATTERN_11
                   ]

#Test

text = "Eu estou pensando em acreditar o laboratório na ABNT NBR NM 88:2000"

if re.search(PATTERN_18, text):
    print("Achei")
else:
    print("Não achei")

exemplos = [
    "ABNT NBR ISO 17025 / 2025",
    "ABNT NBR ISO 17025 / 2025 - Parte 3",
    "ABNT NBR ISO 17025 / 2025 - Partes 3 e 4",
    "ABNT NBR ISO 17025 / 2025 - Partes 2, 3 e 4",
    "ABNT NBR ISO"
]

