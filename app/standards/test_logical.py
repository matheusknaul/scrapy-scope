from standard_features import build_standard
from separate_text import __separate__
from openpyxl import load_workbook

workbook = load_workbook('tabela_ensaio.xlsx')
worksheet = workbook['Sheet']

# print(build_standard("ABNT NBR ISO 17232:2025"))

lista = []
for cell in worksheet['B']:
    print(cell)
    if cell.value:
        lista.append(__separate__(cell.value))

for 

print(lista)