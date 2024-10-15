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
# ASTM
PATTERN_15 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}" # Ex ASTM E112
PATTERN_16 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}+:\d{2,4}" # Ex ASTM E112:2022
PATTERN_17 = r"([A-Z]{4}\s)[A-Z]{1}\d{2,5}\s/\s\d{4}[a-z]{1}\d{1}"

list_of_patterns = [
                    PATTERN_1, PATTERN_2, PATTERN_3, PATTERN_4, PATTERN_5,
                    PATTERN_6, PATTERN_7, PATTERN_8, PATTERN_9, PATTERN_10,
                    PATTERN_11
                   ]

#Test

text = "Eu estou pensando em acreditar o laboratório na ASTM F1264 /2016e1"

if re.search(PATTERN_17, text):
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

